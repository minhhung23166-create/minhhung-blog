from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "blog/home.html", {"title": "this is the djangoblog home page"})

def about(request):
    return render(request, "blog/about.html", {"title": "this is the djangoblog about page"})

def contact(request):
    return render(request, "blog/contact.html", {"Minh Hung": "this is the djangoblog contact page"})