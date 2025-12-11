from django.db import models


class Project(models.Model):
    title = models.CharField("Título", max_length=150)
    slug = models.SlugField(unique=True)
    short_description = models.CharField("Descripción corta", max_length=300)
    description = models.TextField("Descripción detallada")
    tech_stack = models.CharField(
        "Tecnologías",
        max_length=200,
        help_text="Ej: Django, DRF, PostgreSQL, Docker",
    )
    image = models.ImageField(upload_to="projects", blank=True, null=True)
    repo_url = models.URLField("Repositorio", blank=True)
    live_url = models.URLField("Deploy / Demo", blank=True)
    is_featured = models.BooleanField("Destacado", default=False)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title


class Skill(models.Model):
    LEVEL_CHOICES = (
        (1, "Básico"),
        (2, "Intermedio"),
        (3, "Avanzado"),
        (4, "Experto"),
    )

    name = models.CharField("Skill", max_length=100)
    category = models.CharField(
        "Categoría",
        max_length=100,
        help_text="Backend, Frontend, DevOps, Data, etc.",
    )
    level = models.PositiveSmallIntegerField("Nivel", choices=LEVEL_CHOICES, default=2)

    class Meta:
        ordering = ["-level", "name"]

    def __str__(self):
        return self.name
