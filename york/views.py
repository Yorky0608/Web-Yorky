from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import Question, Response, Video
from .forms import QuestionForm, ResponseForm


# Create your views here.
def index(request):
    """The home page for Learning Log."""
    return render(request, 'york/index.html')

def questions(request):
    """Show all topics."""
    questions = Question.objects.order_by('text')
    context = {'questions': questions}
    return render(request, 'york/questions.html', context)

def responses(request, question_id):
    """Show a single topic and all its entries."""
    question = Question.objects.get(id=question_id)
    responses = question.response_set.order_by('-date_added')
    context = {'question': question, 'responses': responses}

    return render(request, 'york/responses.html', context)



@login_required
def new_question(request):
    """Add a new topic."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = QuestionForm()
    else:
        # POST data submitted; process data.
        form = QuestionForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect('york:questions')

    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'york/new_question.html', context)

@login_required
def new_response(request, question_id):
    """Add a new entry for a particular topic."""
    question = Question.objects.get(id=question_id)

    if request.method != 'POST':
    # No data submitted; create a blank form.
        form = ResponseForm()
    else:
        # POST data submitted; process data.
        form = ResponseForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.owner = request.user
            new_entry.question = question
            new_entry.save()
            return redirect('york:responses', question_id=question_id)

        # Display a blank or invalid form.
    context = {'question': question, 'form': form}
    return render(request, 'york/new_response.html', context)

@login_required
def edit_response(request, response_id):
    """Edit an existing entry."""
    response = Response.objects.get(id=response_id)
    question = response.question

    if response.owner != request.user:
        return redirect('york:index')
    else:
        if request.method != 'POST':
            # Initial request; pre-fill form with the current entry.
            form = ResponseForm(instance=question)
        else:
            # POST data submitted; process data.
            form = ResponseForm(instance=question, data=request.POST)
            if form.is_valid():
                form.save
                return redirect('york:responses', question_id=question.id)

        context = {'response': response, 'question': question, 'form': form}
        return render(request, 'york/edit_response.html', context)


def asian(request):
    videos = Video.objects.filter(category='York')
    video = videos.filter(title='Emotional Damage').first()
    if not video:
        return redirect('/')

    return render(request, 'york/asian.html', context={'video' : video})

def about_me(request):
    music_videos = Video.objects.filter(category='Musc')
    video = music_videos.filter(title='Lofi').first()
    if not video:
        return redirect('/')

    return render(request, 'york/about_me.html', context={'video' : video})

def interests(request):
    return render(request, 'york/interests.html')