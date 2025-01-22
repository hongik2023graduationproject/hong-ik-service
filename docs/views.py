from django.shortcuts import render

# Create your views here.

def docs_home(request):
    return render(request, 'docs/home.html')