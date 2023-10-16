from django.urls import path
from userview.views import *

urlpatterns =[
    path('',loginform, name='loginform'),
    # path('logout',views.logout, name='logout')
]