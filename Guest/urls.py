from django.urls import path
from Guest import views
app_name = "webguest"

urlpatterns=[
    path('Login/',views.Login,name="Login"),
    path('CustomerRegistration/',views.CustomerRegistration,name="CustomerRegistration"),
]