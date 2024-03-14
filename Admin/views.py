from django.shortcuts import render,redirect
import firebase_admin 
from firebase_admin import firestore,credentials,storage,auth
import pyrebase



db=firestore.client()


# Create your views here.
def District(request):
    dis=db.collection("tbl_district").stream()
    dis_data=[]
    for i in dis:
        data=i.to_dict()
        dis_data.append({"dis":data,"id":i.id})
    if request.method=="POST":
        data={"district_name":request.POST.get("District")}
        db.collection("tbl_district").add(data)
        return redirect("webadmin:District")
    else:
        return render(request,"Admin/District.html",{"district":dis_data})

        
def editdistrict(request,id):
    dis=db.collection("tbl_district").document(id).get().to_dict()
    if request.method=="POST":
        data={"district_name":request.POST.get("District")}
        db.collection("tbl_district").document(id).update(data)
        return redirect("webadmin:district")
    else:
        return render(request,"Admin/District.html",{"dis_data":dis})
   
def Place(request):
    dis=db.collection("tbl_district").stream()
    dis_data=[]
    for i in dis:
        data=i.to_dict()
        dis_data.append({"dis":data,"id":i.id})
    result=[]
    place_data=db.collection("tbl_place").stream()
    for place in place_data:
        place_dict=place.to_dict()
        district=db.collection("tbl_district").document(place_dict["district_id"]).get()
        district_dict=district.to_dict()
        result.append({'district_data':district_dict,'place_data':place_dict,'placeid':place.id})
    if request.method=="POST":
        data={"place_name":request.POST.get("Place"),"district_id":request.POST.get("district")}
        db.collection("tbl_place").add(data)
        return redirect("webadmin:Place")
    else:
        return render(request,"Admin/Place.html",{"district":dis_data,"place":result})

def delPlace(request,id):
    db.collection("tbl_place").document(id).delete()
    return redirect("webadmin:Place")



def type(request):
    t=db.collection("tbl_type").stream()
    t_data=[]
    for i in t:
        data=i.to_dict()
        t_data.append({"t":data,"id":i.id})
    if request.method=="POST":
        data={"type_name":request.POST.get("type")}
        db.collection("tbl_type").add(data)
        return redirect("webadmin:type")
    else:
        return render(request,"Admin/Type.html",{"type":t_data})


def edittype(request,id):
    t=db.collection("tbl_type").document(id).get().to_dict()
    if request.method=="POST":
        data={"type_name":request.POST.get("type")}
        db.collection("tbl_type").document(id).update(data)
        return redirect("webadmin:type")
    else:
        return render(request,"Admin/Type.html",{"t_data":t})        
   

def deltype(request,id):
    db.collection("tbl_type").document(id).delete()
    return redirect("webadmin:type")



def Homepage(request):
    return render(request,"Admin/Homepage.html")


def admin(request):
    if request.method =="POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        try:
            admin = firebase_admin.auth.create_user(email=email,password=password)
        except (firebase_admin._auth_utils.EmailAlreadyExistsError,ValueError) as error:
            return render(request,"Admin/Admin.html",{"msg":error})
        db.collection("tbl_admin").add({"admin_id":admin.uid,"admin_name":request.POST.get("name"),"admin_email":request.POST.get("email")})    
        return render(request,"Admin/Admin.html")
    else:
        return render(request,"Admin/Admin.html")
    


def viewcomplaint(request):
   
        
        user_data=[]
        worker_data=[]
        wcom = db.collection("tbl_Complains").where("Worker_id", "!=","").where("complaint_status", "==", 0).stream()
        for i in wcom:
            wdata = i.to_dict()
            worker = db.collection("tbl_Worker").document(wdata["Worker_id"]).get().to_dict()
            worker_data.append({"complaint":i.to_dict(),"id":i.id,"worker":worker})

        ucom=db.collection("tbl_Complains").where("User_id","!=","").where("complaint_status","==",0).stream()
        for i in ucom:
            udata = i.to_dict()
            user = db.collection("tbl_User").document(udata["User_id"]).get().to_dict()
            user_data.append({"complaint":i.to_dict(),"id":i.id,"user":user})  
        return render(request,"Admin/ViewComplaints.html",{"worker":worker_data,"user":user_data})    
    

def reply(request,id):
    
    if request.method == "POST":
            db.collection("tbl_Complains").document(id).update({"complaint_reply":request.POST.get("reply"),"complaint_status":"1"})
            return render(request,"Admin/Reply.html",{"msg":"Reply Sended..."})
    return render(request,"Admin/Reply.html")    
    
def viewworker(request):
    worker=db.collection("tbl_Worker").where("worker_status","==",0).stream()
    worker_data=[]
    for i in worker:
        data=i.to_dict()
        worker_data.append({"worker":data,"id":i.id})
    return render(request,"Admin/ViewWorker.html",{"worker":worker_data})

def accept(request,id):
    db.collection("tbl_Worker").document(id).update({"worker_status":1})
    return redirect("webadmin:accepted")   

def reject(request,id):
    db.collection("tbl_Worker").document(id).update({"worker_status":2})
    return redirect("webadmin:rejected")   


def accepted(request):
    worker=db.collection("tbl_Worker").where("worker_status","==",1).stream()
    worker_data=[]
    for i in worker:
        data=i.to_dict()
        worker_data.append({"worker":data,"id":i.id})
    return render(request,"Admin/AcceptedWorker.html",{"worker":worker_data})

def rejected(request):
    worker=db.collection("tbl_Worker").where("worker_status","==",2).stream()
    worker_data=[]
    for i in worker:
        data=i.to_dict()
        worker_data.append({"worker":data,"id":i.id})
    return render(request,"Admin/RejectedWorker.html",{"worker":worker_data})

      