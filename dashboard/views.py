from lib2to3.fixes.fix_input import context

from django.shortcuts import render

# Create your views here.
def dashboard(request):
    data = [
        {"title": "Users", "count": 150},
        {"title": "Orders", "count": 320},
        {"title": "Revenue", "count": "12450"},
    ]
    return render(request, 'pages/dashboard.html', context={"data": data})