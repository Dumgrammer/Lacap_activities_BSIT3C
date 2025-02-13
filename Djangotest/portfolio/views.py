from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "pages/portfolio.html")

def education(request):
    return render(request, 'pages/education.html')

def contact(request):
    return render(request, 'pages/contact.html')