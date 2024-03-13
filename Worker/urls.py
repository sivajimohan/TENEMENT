from django.urls import path,include
from Worker import views
app_name="webworker"
urlpatterns = [
    path ('worker/',views.worker,name="worker"),
    path ('work/',views.work,name="work"),
    path ('workpost/',views.workpost,name="workpost"),
    path ('workgallery/',views.Workgallery,name="Workgallery"),
    path ('Complains/',views.Complains,name="Complains"),
    path ('delComplains/<str:id>',views.delComplains,name="delComplains"),
    path ('Homepage/',views.Homepage,name="Homepage"),
    path ('MyProfile/',views.MyProfile,name="MyProfile"),
    path ('ChangePassword/',views.ChangePassword,name="ChangePassword"), 
    path ('EditProfile/',views.EditProfile,name="EditProfile"),
    path ('Homepage/',views.Homepage,name="Homepage"),
    path('viewreq/',views.viewreq,name="viewreq"),
    path('accept/<str:id>',views.accept,name="accept"),
    path('reject/<str:id>',views.reject,name="reject"),
    
    
    


]
