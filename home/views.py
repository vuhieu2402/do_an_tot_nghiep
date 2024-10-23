from django.shortcuts import render


def home_view(request):
    return render(request, 'home/index.html')

# Create your views here.
