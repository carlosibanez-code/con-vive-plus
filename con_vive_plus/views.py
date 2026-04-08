from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import House, Person, Expense, ContactMessage
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import ContactMessageForm
def home(request):
    success_message = ""

    if request.method == "POST":
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            form.save()
            success_message = f'Gracias {name}, hemos recibido tu mensaje correctamente.'
            form = ContactMessageForm()
    else:
        form = ContactMessageForm()        

    
    return render(
        request, "con_vive_plus/home.html",
        {'form': form,
         'success_message' : success_message})


def houses_list(request):
    city = request.GET.get('city')
    houses = House.objects.all().order_by("-is_available", "name")
    text = ", ".join([house.name for house in houses])
    
    if city:
        houses = houses.filter(city__icontains = city)
    return render(request, "con_vive_plus/houses_list.html", {"houses": houses})

def persons_list(request):
    persons = Person.objects.all()
    return render(request, "con_vive_plus/persons_list.html", {"persons": persons})

def expenses_list(request):
    expenses = Expense.objects.all()
    return render (request, "con_vive_plus/expenses_list.html", {"expenses": expenses})

@login_required
def my_account(request):
    return render(request, 'con_vive_plus/my_account.html')

def logout_user(request):
    logout(request)
    return redirect("/")

def register_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/login/")
    else:
            form = UserCreationForm()
        
    return render(request, 'con_vive_plus/register.html',{'form': form})

