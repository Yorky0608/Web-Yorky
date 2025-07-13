from django.urls import path

from . import views
from  django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'york'
urlpatterns = [
    #Home page
    path('', views.index, name='index'),
    # Page that shows all topics.
    path('asian/', views.asian, name='asian'),
    path('interests/', views.interests, name='interests'),
    ]

urlpatterns += staticfiles_urlpatterns()