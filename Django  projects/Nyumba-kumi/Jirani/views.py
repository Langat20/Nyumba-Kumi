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

def neighbourhood_details(request,pk):
    neighbourhood = Neighbourhood.objects.filter(id=pk)
    businesses = Business.objects.filter(neighbourhood=pk)
    alerts = Alerts.objects.filter(neighbourhood=pk)
    if request.method == 'POST':
        form = CreateAlertForm(request.POST)
        
        if form.is_valid():
            alert = form.save(commit=False)
            alert.owner = request.user.profile
            alert.neighbourhood = request.user.profile.neighbourhood
            alert.save()
            return redirect('neighbourhood_details',pk)
    else:
        form = CreateAlertForm()
    context ={
      'neighbourhood':neighbourhood,
      'businesses': businesses,
      'alerts': alerts,
      'form': form,
    }
    return render(request, 'neighbourhoods/neighbourhood_details.html', context)
  
def create_business(request, pk):
    if request.method == 'POST':
        b_form = CreateBusinessForm(request.POST, request.FILES)
        if b_form.is_valid:
            business = b_form.save(commit=False)
            business.owner = request.user
            business.neighbourhood = request.user.profile.neighbourhood
            b_form.save()

            messages.success(request, f'Your business has been created successfully')
            return redirect('neighbourhood_details',pk)

    else:
        b_form = CreateBusinessForm(instance=request.user)
        

    context = {
      'b_form':b_form,
    }
    return render(request,'business/create_business.html', context)
