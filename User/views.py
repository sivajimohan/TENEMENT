from django.shortcuts import render,redirect
import firebase_admin 
from firebase_admin import firestore,credentials,storage,auth
import pyrebase
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from datetime import date,datetime
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

def MyProfile(request):
    User=db.collection("tbl_User").document(request.session["uid"]).get().to_dict()
    return render(request,"User/MyProfile.html",{"User":User})

def EditProfile(request):
    User=db.collection("tbl_User").document(request.session["uid"]).get().to_dict()
    if request.method=="POST":
        data={"User_Name":request.POST.get("Name"),"User_Email":request.POST.get("Email"),"User_Contact":request.POST.get("Contact")}
        db.collection("tbl_User").document(request.session["uid"]).update(data)
        return redirect("webuser:MyProfile")
    else:
        return render(request,"User/EditProfile.html",{"User":User})


def ChangePassword(request):
    User = db.collection("tbl_User").document(request.session["uid"]).get().to_dict()
    email = User["User_Email"]
    password_link = firebase_admin.auth.generate_password_reset_link(email) 
    send_mail(
    'Reset your password ', 
    "\rHello \r\nFollow this link to reset your Project password for your " + email + "\n" + password_link +".\n If you didn't ask to reset your password, you can ignore this email. \r\n Thanks. \r\n Your D MARKET user.",#body
    settings.EMAIL_HOST_USER,
    [email],
    )
    return render(request,"User/Homepage.html",{"msg":email})


def Homepage(request):
    return render(request,"User/Homepage.html")

def ViewWork(request):
    w=db.collection("tbl_work").stream()
    w_data=[]
    for i in w:
        data=i.to_dict()
        w_data.append({"w":data,"id":i.id})
    return render(request,"User/ViewWork.html",{"work":w_data})


def Worker(request,id):
    data={"worker_id":id,"user_id":request.session["uid"],"request_status":0} 
    db.collection("tbl_request").add(data)
    return render(request,"Worker/Worker.html")

def workreq(request,id):
    if request.method=="POST":
        datedata=date.today()
        data={"work_id":id,"user_id":request.session["uid"],"Details":request.POST.get("details"),"for_date":request.POST.get("fordate"),"request_date":str(datedata),"request_status":0}
        db.collection("tbl_request").add(data)
        return redirect("webuser:ViewWork")  
    else:
        return render(request,"User/request.html")


def myreq(request):
    return render(request,"User/MyRequest.html")


