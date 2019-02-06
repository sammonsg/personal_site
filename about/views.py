from django.views import generic


class AboutMeView(generic.TemplateView):
    template_name = 'about/about.html'
