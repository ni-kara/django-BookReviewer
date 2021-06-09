from django.shortcuts import render

# Create your views here.
def dashboard(request):
    content = { }
    return render(request, "dashboard/dashboard.html", content)
