from django.urls import path

# from . import views

from .views import home,service_details,starter_page,blog,blog_details,portfolio_details 
urlpatterns = [
     path('',home,name='home' ),
    path('service/',service_details, name='service'),
    path('starter/',starter_page,name='starter'),
    path('blog_details/', blog_details,name='blog_details'),
    path('blog/', blog,name='blog'),
    path('portfolio/',portfolio_details, name='portfolio'),
]
