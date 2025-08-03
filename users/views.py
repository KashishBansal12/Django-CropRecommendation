# users/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import RecommendationHistory
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

@login_required # This decorator ensures only logged-in users can see this page
def recommendation_history(request):
    # Get all the recommendation history objects for the current logged-in user
    history = RecommendationHistory.objects.filter(user=request.user).order_by('-date_recommended')
    
    context = {
        'history': history
    }
    return render(request, 'users/history.html', context)

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login') # Redirect to the login page after successful signup
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})