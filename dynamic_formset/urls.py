from django.urls import path

from dynamic_formset.views import index,create_contact

app_name = "dynamic_formset"

urlpatterns = [
    path('',index,name='index'),
    path('create-contact',create_contact,name='create-contact'),
]