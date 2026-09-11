from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def products(request):
    return render(request , 'products.html')


def wipes(request):
    return render(request , 'wipes.html')


def pampers(request):
    return render(request , 'pampers.html')


def mothers(request):
    return render(request , 'mothers.html')


def about(request):
    return render(request , 'about.html')

def connect_us(request):
    return render(request, 'connect.html')

def our_story(request):
    return render(request, 'our_story.html')

def quality(request):
    return render(request, 'quality.html')

def why_us(request):
    return render(request, 'why_us.html')  