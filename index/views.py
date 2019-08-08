from django.shortcuts import render
from django.views import View
# Create your views here.
from .models import ProjectDone, Experience


class IndexView(View):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        featured_projects = ProjectDone.objects.filter(featured=True).order_by('timestamp')
        other_projects = ProjectDone.objects.filter(featured=False).order_by('timestamp')
        experience = Experience.objects.order_by('-timestamp')
        if not featured_projects and other_projects:
            return render(request, 'index.html', {})
        else:
            context = {
                'featured': featured_projects,
                'other': other_projects,
                'experience': experience,
            }

            return render(request, 'index.html', context)


