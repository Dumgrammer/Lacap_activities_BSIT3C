from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        "title": "Portfolio",
        "user": {
            "birthday": "03-11-2003"
        }
    }
    return render(request, "pages/portfolio.html", context=context)

def education(request):
    return render(request, 'pages/education.html')

def contact(request):
    return render(request, 'pages/contact.html')