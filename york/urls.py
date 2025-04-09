from django.urls import path

from . import views
from  django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'york'
urlpatterns = [
    #Home page
    path('', views.index, name='index'),
    # Page that shows all topics.
    path('questions/', views.questions, name='questions'),
    # Detail page for a single topic.
    path('questions/<int:question_id>/', views.responses, name='responses'),
    # Page for adding a new topic.
    path('new_question/', views.new_question, name='new_question'),
    # Page for adding a new entry.
    path('new_response/<int:question_id>/', views.new_response, name='new_response'),
    # Page for editing an entry.
    path('edit_entry/<int:response_id>/', views.edit_response, name='edit_response'),
    path('asian/', views.asian, name='asian'),
    path('about_me/', views.about_me, name='about_me'),
    path('interests/', views.interests, name='interests'),
    ]

urlpatterns += staticfiles_urlpatterns()