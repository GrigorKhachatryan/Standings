from django.shortcuts import render, redirect

def main(request):
    return render(request, 'main.html')

def signup(request):
    return redirect('/')

def signin(request):
    return redirect('/')


# Create your views here.
