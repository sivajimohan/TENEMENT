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

def Login(request):
    Workerid =""
    userid=""
    adminid=""
    if request.method == "POST":
        email = request.POST.get("Email")
        password = request.POST.get("Password")
        try:
            data = authe.sign_in_with_email_and_password(email,password)
        except:
            return render(request,"Guest/Login.html",{"msg":"Error in Email Or Password"})
        admin=db.collection("tbl_admin").where("admin_id","==",data["localId"]).stream() 
        for a in admin:
            adminid=a.id   
        worker=db.collection("tbl_Worker").where("Worker_id","==",data["localId"]).stream()    
        for w in worker:
            Workerid=w.id  
            worker=w.to_dict()
            worker_status = worker["worker_status"] 
        user=db.collection("tbl_User").where("User_id","==",data["localId"]).stream()    
        for u in user:
            userid=u.id
        if Workerid:
            if worker_status ==  2:
                return render(request,"Guest/Login.html",{"msg":"Your Request is Rejected"})
            elif worker_status == 0:
                return render(request,"Guest/Login.html",{"msg":"Your Request is Pending...."})
            else:
                request.session["wid"]=Workerid 
                return redirect("webworker:Homepage")   
        elif userid:
            request.session["uid"]=userid
            return redirect("webuser:Homepage")   
        elif adminid:
            request.session["aid"]=adminid 
            return redirect("webadmin:Homepage")  
        else:
            return render(request,"Guest/Login.html",{"msg":"error"})    
    else:
       return render(request,"Guest/Login.html")


def UserRegistration(request):
    dis=db.collection("tbl_district").stream()
    dis_data=[]
    for i in dis:
        data=i.to_dict()
        dis_data.append({"dis":data,"id":i.id})
    if request.method=="POST":
        email = request.POST.get("Email")
        password = request.POST.get("Password")
        try:
            User = firebase_admin.auth.create_user(email=email,password=password)
        except (firebase_admin._auth_utils.EmailAlreadyExistsError,ValueError) as error:
            return render(request,"Guest/UserRegistration.html",{"msg":error})
      
        image=request.FILES.get("Photo")
        if image:
            path="UserPhoto/"+image.name
            st.child(path).put(image)
            cp_url=st.child(path).get_url(None)
        db.collection("tbl_User").add({"User_id":User.uid,"User_Name":request.POST.get("Name"),"User_Email":request.POST.get("Email"),"User_Contact":request.POST.get("Contact"),"User_Address":request.POST.get("Address"),"place_id":request.POST.get("place"),"User_Photo":cp_url})
        return render(request,"Guest/index.html")
    else:    
        return render(request,"Guest/UserRegistration.html",{"district":dis_data})    

def AjaxPlace(request):
    place=db.collection("tbl_place").where("district_id","==",request.GET.get("did")).stream()
    place_data=[]
    for p in place:
        place_data.append({"place":p.to_dict(),"id":p.id})
    return render(request,"Guest/AjaxPlace.html",{"place":place_data})


def WorkerRegistration(request):
    dis=db.collection("tbl_district").stream()
    dis_data=[]
    for i in dis:
        data=i.to_dict()
        dis_data.append({"dis":data,"id":i.id})
    if request.method=="POST":
        email = request.POST.get("Email")
        password = request.POST.get("Password")
        try:
            Worker = firebase_admin.auth.create_user(email=email,password=password)
        except (firebase_admin._auth_utils.EmailAlreadyExistsError,ValueError) as error:
            return render(request,"Guest/WorkerRegistration.html",{"msg":error})
      
        image=request.FILES.get("Photo")
        if image:
            path="WorkerPhoto/"+image.name
            st.child(path).put(image)
            wp_url=st.child(path).get_url(None)
        Proof=request.FILES.get("Proof")
        if Proof:
            path="WorkerProof/"+Proof.name
            st.child(path).put(image)
            wpr_url=st.child(path).get_url(None)    
        db.collection("tbl_Worker").add({"Worker_id":Worker.uid,"Worker_Name":request.POST.get("Name"),"Worker_Email":request.POST.get("Email"),"Worker_Contact":request.POST.get("Contact"),"Worker_Address":request.POST.get("Address"),"place_id":request.POST.get("place"),"Worker_Photo":wp_url,"Worker_Proof":wpr_url,"worker_status":0})
        return render(request,"Guest/WorkerRegistration.html")
    else:    
        return render(request,"Guest/WorkerRegistration.html",{"district":dis_data})    

def index(request):
    return render(request,"Guest/index.html")
