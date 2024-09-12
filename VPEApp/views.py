from django.shortcuts import render
from VPEApp.models import EvaluationType, UsersList
from django.http import HttpResponseRedirect
from rest_framework import generics

# Function for Homepage
def home(request):
    return render(request, "home.html")

def evaluations(request):
    return render(request, "evaluations.html")

def add_evaluations(request):
    if request.method == 'POST':
        if request.POST.get('GlobalId') \
            and request.POST.get('Name'):
            userslist = UsersList()
            userslist.GlobalId = request.POST.get('GlobalId')
            userslist.Name = request.POST.get('Name')
            userslist.save()
            return HttpResponseRedirect('evaluations')
    else:
        return render(request, "add_user.html")

def userslist(request):
    all_users = UsersList.objects.all().order_by('Name')
    return render(request, "userslist.html", {"UsersList":all_users})

def add_user(request):
    if request.method == 'POST':
        if request.POST.get('GlobalId') \
            and request.POST.get('Name'):
            userslist = UsersList()
            userslist.GlobalId = request.POST.get('GlobalId')
            userslist.Name = request.POST.get('Name')
            userslist.save()
            return HttpResponseRedirect('userslist')
    else:
        return render(request, "add_user.html")

def vendorlist(request):
    return render(request, "vendorlist.html")

def evaluationtypes(request):
    all_EvaluationType = EvaluationType.objects.all()
    return render(request, "evaluationtypes.html", {"EvaluationType":all_EvaluationType})

