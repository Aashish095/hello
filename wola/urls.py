from django.urls import path
from wola import views

urlpatterns=[
    path('',views.index,name='index'),

]
