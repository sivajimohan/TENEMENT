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
    path('ViewComplaint/',views.viewcomplaint,name="viewcomplaint"),
    path ('homepage/',views.Homepage,name="homepage"),
    path('Reply/<str:id>',views.reply,name="reply"),
    path('viewworker/',views.viewworker,name="viewworker"),
    path('accept/<str:id>',views.accept,name="accept"),
    path('reject/<str:id>',views.reject,name="reject"),
    path('accepted/',views.accepted,name="accepted"),
    path('rejected/',views.rejected,name="rejected"),
]
