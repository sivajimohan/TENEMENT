from django.shortcuts import render

# Create your views here.
def user(request):
    return render(request,"User/User.html")
def request(request):
    return render(request,"User/Request.html")
def review(request):
    return render(request,"User/Review.html")
def complaint(request):
    return render(request,"User/Complaint.html")

