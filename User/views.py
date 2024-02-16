from django.shortcuts import render,redirect
import firebase_admin 
from firebase_admin import firestore,credentials,storage,auth
import pyrebase


# Create your views here.
db=firestore.client()
config = {
  "apiKey": "AIzaSyDAqy5jDAFpKidRLW1ozDDT6bXZRICM718",
  "authDomain": "tenement-b24c0.firebaseapp.com",
  "projectId": "tenement-b24c0",
  "storageBucket": "tenement-b24c0.appspot.com",
  "messagingSenderId": "470025077637",
  "appId": "1:470025077637:web:c483afcaca8659e707faec",
  "measurementId": "G-QNX2BBF2QD",
  "databaseURL":""
}

firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
st = firebase.storage()


def user(request):
    return render(request,"User/User.html")
def request(request):
    return render(request,"User/Request.html")
def review(request):
    return render(request,"User/Review.html")
def Complains(request):
    com=db.collection("tbl_Complains").stream()
    com_data=[]
    for i in com:
        data=i.to_dict()
        com_data.append({"com":data,"id":i.id})
    if request.method=="POST":
        data={"Complains_name":request.POST.get("Title"),"Complains_Content":request.POST.get("Content")}
        db.collection("tbl_Complains").add(data)
        return redirect("webuser:Complains")
    else:
        return render(request,"User/Complains.html",{"Complains":com_data})
def Homepage(request):
    return render(request,"User/Homepage.html")

