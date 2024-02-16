from django.urls import path,include
from User import views
app_name="webuser"
urlpatterns = [
    path ('user/',views.user,name="user"),
    path ('request/',views.request,name="request"),
    path ('review/',views.review,name="review"),
    path ('Complains/',views.Complains,name="Complains"),
    path ('Homepage/',views.Homepage,name="Homepage"),
]
