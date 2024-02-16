from django.urls import path
from Guest import views
app_name = "webguest"

urlpatterns=[
    path('Login/',views.Login,name="Login"),
    path('UserRegistration/',views.UserRegistration,name="UserRegistration"),
    path('AjaxPlace/',views.AjaxPlace,name="AjaxPlace"),
    path('WorkerRegistration/',views.WorkerRegistration,name="WorkerRegistration"),
]