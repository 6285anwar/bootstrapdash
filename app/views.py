from django.shortcuts import render

# Create your views here.
def corona(request):
    return render(request,'corona.html')