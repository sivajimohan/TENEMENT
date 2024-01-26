from django.shortcuts import render

# Create your views here.
def worker(request):
    return render(request,"Worker/Worker.html")
def work(request):
    return render(request,"Worker/Work.html")
def workpost(request):
    return render(request,"Worker/Workpost.html")
def Workgallery(request):
    return render(request,"Worker/Workgallery.html")

