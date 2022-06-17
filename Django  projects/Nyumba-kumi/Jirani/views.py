from django.shortcuts import render

# Create your views here.
import profile
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from .models import Alerts, Business, Neighbourhood, Profile
from .forms import CreateAlertForm, CreateBusinessForm, CreateNeighbourhoodForm
from django.contrib import messages
from django.views.generic import CreateView

# Create your views here.
@login_required()
def index(request):
  return render(request,'index.html')

def search_results(request):
    '''
    Function to search for businesses
    
    Args: search term
    '''

    if 'business' in request.GET and request.GET["business"]:
        search_term = request.GET.get("business")
        searched_businesses = Business.search_business(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"businesses": searched_businesses})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

def create_neighbourhood(request):
    if request.method == 'POST':
        form = CreateNeighbourhoodForm(request.POST, request.FILES)
        if form.is_valid():
            neighbourhood = form.save(commit=False)
            neighbourhood.admin = request.user.profile.pk
            neighbourhood.save()
            return redirect('neighbourhoods')
    else:
        form = CreateNeighbourhoodForm()
    return render(request, 'neighbourhoods/create_neighbourhood.html', {'form':form})

def join_neighbourhood(request,pk):
    neighbourhood = get_object_or_404(Neighbourhood, id=pk)
    user = request.user
    user.profile.neighbourhood = neighbourhood
    user.profile.save()
    return redirect('neighbourhood_details', pk)

def change_neighbourhood(request, pk):
    neighbourhood = get_object_or_404(Neighbourhood, id=pk)
    user = request.user
    user.profile.neighbourhood = None
    user.profile.save()
    return redirect('neighbourhoods')

def neighbourhoods(request):
    neighbourhoods = Neighbourhood.objects.all()
    return render(request, 'neighbourhoods/neighbourhoods.html', {'neighbourhoods':neighbourhoods})

