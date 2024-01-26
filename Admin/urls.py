from django.urls import path,include
from Admin import views
app_name="webadmin"
urlpatterns = [
    path ('District/',views.District,name="District"),
    path ('type/',views.type,name="type"),
    path ('Place/',views.Place,name="Place"),
    path ('admin/',views.type,name="admin"),
]
