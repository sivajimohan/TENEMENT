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

def worker(request):
    return render(request,"Worker/Worker.html")
def work(request):
    if request.method=="POST":
        image=request.FILES.get("image")
        if image:
            path="WorkPhoto/"+image.name
            st.child(path).put(image)
            p_url=st.child(path).get_url(None)
        data={"title_name":request.POST.get("title"),"description_name":request.POST.get("description"),"work_photo":p_url,"amount":request.POST.get("amount")}
        db.collection("tbl_work").add(data)
        return redirect("webworker:work")
    else:
        return render(request,"Worker/Work.html")
    

def workpost(request):
    return render(request,"Worker/Workpost.html")
def Workgallery(request):
    return render(request,"Worker/Workgallery.html")

def Complains(request):
    com=db.collection("tbl_Complains").stream()
    com_data=[]
    for i in com:
        data=i.to_dict()
        com_data.append({"com":data,"id":i.id})
    if request.method=="POST":
        datedata=date.today()
        data={"Complains_name":request.POST.get("Title"),"Complains_Content":request.POST.get("Content"),"user_id":0,"worker_id":request.session["wid"],"complaint_status":0,"complains_date":str(datedata)}
        db.collection("tbl_Complains").add(data)
        return redirect("webworker:Complains")
    else:
        return render(request,"Worker/Complains.html",{"com":com_data})


def delComplains(request,id):
    com=db.collection("tbl_Complains").document(id).delete()
    return redirect("webworker:Complains")


def MyProfile(request):
    Worker=db.collection("tbl_Worker").document(request.session["wid"]).get().to_dict()
    return render(request,"Worker/MyProfile.html",{"Worker":Worker})

def EditProfile(request):
    Worker=db.collection("tbl_Worker").document(request.session["wid"]).get().to_dict()
    if request.method=="POST":
        data={"Worker_Name":request.POST.get("Name"),"Worker_Email":request.POST.get("Email"),"Worker_Contact":request.POST.get("Contact")}
        db.collection("tbl_Worker").document(request.session["wid"]).update(data)
        return redirect("webuser:MyProfile")
    else:
        return render(request,"Worker/EditProfile.html",{"Worker":Worker})


def ChangePassword(request):
    Worker = db.collection("tbl_Worker").document(request.session["wid"]).get().to_dict()
    email = Worker["Worker_Email"]
    password_link = firebase_admin.auth.generate_password_reset_link(email) 
    send_mail(
    'Reset your password ', 
    "\rHello \r\nFollow this link to reset your Project password for your " + email + "\n" + password_link +".\n If you didn't ask to reset your password, you can ignore this email. \r\n Thanks. \r\n Your D MARKET user.",#body
    settings.EMAIL_HOST_USER,
    [email],
    )
    return render(request,"Worker/Homepage.html",{"msg":email})


def Homepage(request):
    return render(request,"Worker/Homepage.html")

def viewreq(request):
    req=db.collection("tbl_request").where("request_status","==",0).stream()
    req_data=[]
    for i in req:
        data=i.to_dict()
        user=db.collection("tbl_User").document(data["user_id"]).get().to_dict()
        work = db.collection("tbl_work").document(data["work_id"]).get().to_dict()
        req_data.append({"view":data,"id":i.id,"user":user,"work":work})
    return render(request,"Worker/Viewrequest.html",{"view":req_data})



def accept(request,id):
    req=db.collection("tbl_request").document(id).update({"request_status":1})
    user = db.collection("tbl_User").document(request.session["uid"]).get().to_dict()
    email = user["User_Email"]
    send_mail(
    'Service Booking', 
    "\rHello \r\n Your service booking has accepted our technishian will  contact you",#body
    settings.EMAIL_HOST_USER,
    [email],
    )   
    return redirect("webworker:viewreq")
    

def reject(request,id):
    req=db.collection("tbl_request").document(id).update({"request_status":2})
    user = db.collection("tbl_User").document(request.session["uid"]).get().to_dict()
    email = user["User_Email"]
    send_mail(
    'Service Booking', 
    "\rHello \r\n Your service booking has rejected",#body
    settings.EMAIL_HOST_USER,
    [email],
    )   
    return redirect("webworker:viewreq")
    return redirect("webworker:viewreq")    