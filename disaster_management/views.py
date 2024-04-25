from django.shortcuts import render

# A home view to render our home page
def home(request):
    return render(request, 'home.html')
