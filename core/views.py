from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import AddressForm
from .models import Address, AssessmentOrder

# Create your views here.

def home(request):
    return render(request, 'core/home.html')

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'core/signup.html', {'form':form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'core/login.html', {'form':form})
    
def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def list_addresses(request):
    addresses = Address.objects.filter(user=request.user)
    return render(request, 'core/list_addresses.html', {'addresses': addresses})


@login_required
def create_order(request, address_id):
    address = get_object_or_404(Address, id=address_id, user=request.user)
    AssessmentOrder.objects.create(address=address)
    return redirect('home')  # or to a "thank you" page


@login_required
def create_address(request):
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            address_data = form.cleaned_data
            address, created = Address.objects.get_or_create(
                user=request.user,
                street=address_data['street'],
                city=address_data['city'],
                state=address_data['state'],
                zip_code=address_data['zip_code'],
            )
            return redirect('list_addresses')  # or go straight to create_order
    else:
        form = AddressForm()
    return render(request, 'core/create_address.html', {'form': form})
