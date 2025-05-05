from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Question, Response, Video, Blog, Post
from .forms import QuestionForm, ResponseForm, BlogForm, PostForm
from plotly.offline import plot
import plotly.express as plt
import pandas as pd


# Create your views here.
def index(request):
    return render(request, 'york/index.html')

def questions(request):
    questions = Question.objects.order_by('text')
    context = {'questions': questions}
    return render(request, 'york/questions.html', context)

def responses(request, question_id):
    question = Question.objects.get(id=question_id)
    responses = question.response_set.order_by('-date_added')
    context = {'question': question, 'responses': responses}

    return render(request, 'york/responses.html', context)



@login_required
def new_question(request):
    if request.method != 'POST':
        form = QuestionForm()
    else:
        form = QuestionForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect('york:questions')

    context = {'form': form}
    return render(request, 'york/new_question.html', context)

@login_required
def new_response(request, question_id):
    question = Question.objects.get(id=question_id)

    if request.method != 'POST':
        form = ResponseForm()
    else:
        form = ResponseForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.owner = request.user
            new_entry.question = question
            new_entry.save()
            return redirect('york:responses', question_id=question_id)

    context = {'question': question, 'form': form}
    return render(request, 'york/new_response.html', context)

@login_required
def edit_response(request, response_id):
    response = Response.objects.get(id=response_id)
    question = response.question

    if response.owner != request.user:
        return redirect('york:index')
    else:
        if request.method != 'POST':
            form = ResponseForm(instance=question)
        else:
            form = ResponseForm(instance=question, data=request.POST)
            if form.is_valid():
                form.save
                return redirect('york:responses', question_id=question.id)

        context = {'response': response, 'question': question, 'form': form}
        return render(request, 'york/edit_response.html', context)


def blogs(request):
    blogs = Blog.objects.order_by('text')
    context = {'blogs': blogs}
    return render(request, 'york/blogs.html', context)

def posts(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    posts = blog.post_set.order_by('-date_added')
    context = {'blog': blog, 'posts': posts}

    return render(request, 'york/posts.html', context)



@login_required
def new_blog(request):
    if request.method != 'POST':
        form = BlogForm()
    else:
        form = BlogForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect('york:blogs')

    context = {'form': form}
    return render(request, 'york/new_blog.html', context)

@login_required
def new_post(request, blog_id):
    blog = Blog.objects.get(id=blog_id)

    if request.method != 'POST':
        form = PostForm()
    else:
        form = PostForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.owner = request.user
            new_entry.blog = blog
            new_entry.save()
            return redirect('york:posts', blog_id=blog_id)

    context = {'blog': blog, 'form': form}
    return render(request, 'york/new_post.html', context)

@login_required
def edit_post(request, post_id):
    post = Post.objects.get(id=post_id)
    blog = post.blog

    if post.owner != request.user:
        return redirect('york:index')
    else:
        if request.method != 'POST':
            form = PostForm(instance=post)
        else:
            # POST data submitted; process data.
            form = PostForm(instance=post, data=request.POST)
            if form.is_valid():
                form.save
                return redirect('york:posts', blog_id=blog.id)

        context = {'post': post, 'blog': blog, 'form': form}
        return render(request, 'york/edit_post.html', context)


def asian(request):
    videos = Video.objects.filter(category='York')
    video = videos.filter(title='Emotional Damage').first()
    if not video:
        return redirect('/')

    return render(request, 'york/asian.html', context={'video' : video})

def about_me(request):

    df = pd.read_csv('york/sleep.csv')

    title = 'Sleeping Habits'
    fig = plt.bar(df, x='Month', y='Hours', title=title)

    fig.update_layout(
        font_family="Monospace",
        font_color="black",
        title_font_family="Monospace",
        title_font_color="black",
        title=dict(text=title, font=dict(size=32), automargin=True)
    )
    plt_div = plot(fig, output_type='div')

    return render(request, 'york/about_me.html', context={'plot_div': plt_div})

def interests(request):
    return render(request, 'york/interests.html')