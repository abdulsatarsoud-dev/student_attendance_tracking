from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "home.html"


class StudentListView(TemplateView):
    template_name = "about.html"
