from django.shortcuts import render, HttpResponse

recipes = [
    {
        'author': 'Dom',
        'title': 'meatball sub',
        'directions': 'combine all ingredients',
        'date_posted': 'January 1st 2025'
    },
    {
        'author': 'Dom',
        'title': 'turkey sub',
        'directions': 'combine all ingredients',
        'date_posted': 'January 5th 2025'
    },
    {
        'author': 'Dom',
        'title': 'harm & cheese sub',
        'directions': 'combine all ingredients',
        'date_posted': 'January 10th 2025'
    }
]

# Create your views here.
def home(request):
    context = {
        'recipes': recipes
    }
    return render(request, "recipes/home.html", context)

def about(request):
    return render(request, "recipes/about.html", {'title':'About Us'})