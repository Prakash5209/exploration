from django.urls import path

from demo import views

app_name = "demo"
urlpatterns = [
    path('',views.demohome,name="demohome"),
    path('update/<int:id>/',views.updatedemo,name="updatedemo"),
]