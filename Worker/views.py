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

def worker(request):
    return render(request,"Worker/Worker.html")
def work(request):
    if request.method=="POST":
        image=request.FILES.get("image")
        if image:
            path="WorkPhoto/"+image.name
            st.child(path).put(image)
            p_url=st.child(path).get_url(None)
        data={"title_name":request.POST.get("title"),"description_name":request.POST.get("description"),"work_photo":p_url}
        db.collection("tbl_work").add(data)
        return redirect("webworker:work")
    else:
        return render(request,"Worker/Work.html")
    

def workpost(request):
    return render(request,"Worker/Workpost.html")
def Workgallery(request):
    return render(request,"Worker/Workgallery.html")
def Homepage(request):
    return render(request,"Worker/Homepage.html")



