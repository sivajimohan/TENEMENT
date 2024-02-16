from django.urls import path,include
from Admin import views
app_name="webadmin"
urlpatterns = [
    path ('District/',views.District,name="District"),
    path('editdistrict/<str:id>',views.editdistrict,name="editdistrict"),
    path ('type/',views.type,name="type"),
    path('edittype/<str:id>',views.edittype,name="edittype"),
    path('deltype/<str:id>',views.deltype,name="deltype"),
    path ('Place/',views.Place,name="Place"),
    path('delPlace/<str:id>',views.delPlace,name="delPlace"),
    path ('admin/',views.admin,name="admin"),
    path ('homepage/',views.Homepage,name="homepage"),
]
