from django.views import generic


class HomepageView(generic.TemplateView):
    template_name = 'core/home.html'


class WorkInProgressView(generic.TemplateView):
    template_name = 'core/wip.html'
