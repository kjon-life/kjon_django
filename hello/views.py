from django.shortcuts import render
from .constants import MY_LINKEDIN_PROFILE_URL, MY_GITHUB_PROFILE_URL

# Create your views here.
def index(request):
    context = {
        'MY_LINKEDIN_PROFILE_URL': MY_LINKEDIN_PROFILE_URL,
        'MY_GITHUB_PROFILE_URL': MY_GITHUB_PROFILE_URL,
    }
    return render(request, 'hello/index.html', context)

def health_hi(request):
    return HttpResponse("Hi", status=200)