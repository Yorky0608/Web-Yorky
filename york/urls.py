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
    path('blogs/', views.blogs, name='blogs'),
    # Detail page for a single topic.
    path('blogs/<int:blog_id>/', views.posts, name='posts'),
    # Page for adding a new topic.
    path('new_blog/', views.new_blog, name='new_blog'),
    # Page for adding a new entry.
    path('new_post/<int:blog_id>/', views.new_post, name='new_post'),
    # Page for editing an entry.
    path('edit_post/<int:post_id>/', views.edit_post, name='edit_post'),
    ]

urlpatterns += staticfiles_urlpatterns()