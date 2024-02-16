from django.urls import path,include
from Worker import views
app_name="webworker"
urlpatterns = [
    path ('worker/',views.worker,name="worker"),
    path ('work/',views.work,name="work"),
    path ('workpost/',views.workpost,name="workpost"),
    path ('workgallery/',views.Workgallery,name="Workgallery"),
    path ('Homepage/',views.Homepage,name="Homepage"),
]
