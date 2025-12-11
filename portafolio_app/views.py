from django.views.generic import TemplateView, DetailView
from .models import Project, Skill


class HomeView(TemplateView):
    template_name = "portafolio/home.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["featured_projects"] = Project.objects.filter(is_featured=True)
        ctx["projects"] = Project.objects.filter(is_featured=False)
        ctx["skills"] = Skill.objects.all()
        return ctx


class ProjectDetailView(DetailView):
    model = Project
    template_name = "portafolio/project_detail.html"
    context_object_name = "project"
