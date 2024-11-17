from django.shortcuts import render
from .models import Team
from .models import Analytic
# Create your views here.

   

# Create your views here.

def home(request):
    
    context = {}
    analytics = Analytic.objects.all()
    teams = Team.objects.all()
    context['teams'] = teams
    context['analytics'] = analytics
    return render(request, 'index.html', context)
   

def blog(request):
    return render(request,'blog.html')


def blog_details(request):
    return render(request,'blog-details.html')

def portfolio_details(request):
    return render(request, 'portfolio-details.html')

def service_details(request):
    return render(request,'service-details.html')

def starter_page(request):
    return render(request,'starter-page.html')