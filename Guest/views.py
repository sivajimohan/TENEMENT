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
    return render(request,"Guest/Login.html")


def CustomerRegistration(request):
    dis=db.collection("tbl_district").stream()
    dis_data=[]
    for i in dis:
        data=i.to_dict()
        dis_data.append({"dis":data,"id":i.id})
    if request.method=="POST":
        email = request.POST.get("Email")
        password = request.POST.get("Password")
        try:
            Customer = firebase_admin.auth.create_user(email=email,password=password)
        except (firebase_admin._auth_utils.EmailAlreadyExistsError,ValueError) as error:
            return render(request,"Guest/CustomerRegistration.html",{"msg":error})
      
        image=request.FILES.get("Photo")
        if image:
            path="CustomerPhoto/"+image.name
            st.child(path).put(image)
            cp_url=st.child(path).get_url(None)
        db.collection("tbl_Customer").add({"Customer_Name":request.POST.get("Name"),"Customer_Email":request.POST.get("Email"),"Customer_Contact":request.POST.get("Contact"),"Customer_Address":request.POST.get("Address"),"place_id":request.POST.get("place"),"Customer_Photo":cp_url})
        return render(request,"Guest/CustomerRegistration.html")
    else:    
        return render(request,"Guest/CustomerRegistration.html",{"district":dis_data})    