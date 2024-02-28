from django.urls import path,include
from User import views
app_name="webuser"
urlpatterns = [
    path ('user/',views.user,name="user"),
    path ('workreq/<str:id>',views.workreq,name="workreq"),
    path ('review/',views.review,name="review"),
    path ('Complains/',views.Complains,name="Complains"),
    path ('Homepage/',views.Homepage,name="Homepage"),
    path ('MyProfile/',views.MyProfile,name="MyProfile"),
    path ('ChangePassword/',views.ChangePassword,name="ChangePassword"),
    path ('EditProfile/',views.EditProfile,name="EditProfile"),
    path ('ViewWork/',views.ViewWork,name="ViewWork"),
    path ('Worker/<str:id>',views.Worker,name="Worker"),
    path ('myreq/',views.myreq,name="myreq"),

]
