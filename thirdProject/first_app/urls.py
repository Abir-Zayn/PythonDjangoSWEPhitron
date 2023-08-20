from django.urls import path
from . import views

urlpatterns = [
    # path('',views.newcontact, name='newcontact'),
    path('contact/',views.contact),
]

    #path('', views.contact),