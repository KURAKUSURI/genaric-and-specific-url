from django.shortcuts import render

# Create your views here.

def mi(request):
    return render(request,'mi.html')

def dc(request):
    return render(request,'dc.html')

def kkr(request):
    return render(request,'kkr.html')
