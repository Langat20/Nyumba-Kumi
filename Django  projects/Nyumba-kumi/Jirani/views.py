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

