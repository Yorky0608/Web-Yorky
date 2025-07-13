from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Video
from plotly.offline import plot
import plotly.express as plt
import pandas as pd


# Create your views here.
def index(request):
    """The home page for Learning Log."""
    return render(request, 'york/index.html')

def asian(request):
    videos = Video.objects.filter(category='York')
    video = videos.filter(title='Emotional Damage').first()
    if not video:
        return redirect('/')

    return render(request, 'york/asian.html', context={'video' : video})


def interests(request):
    return render(request, 'york/interests.html')