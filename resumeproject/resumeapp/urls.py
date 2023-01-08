from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('courses/',views.courses,name='courses'),
    path('education/',views.education,name='education'),
    path('skills/',views.skills,name='skills'),
    path('projects/',views.projects,name='projects'),
    path('exp/',views.exp,name='exp'),
    path('contact/',views.contact,name='contact'),
    path('thanks/',views.thanks,name='thanks'),
]