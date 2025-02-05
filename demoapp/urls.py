from django.urls import path
from . import views

urlpatterns = [
    path('getclient/<name>/<id>', views.pathview, name='pathview'),
    path('getuser/', views.qryview, name="qryview"),
    path("showform/", views.showform, name="showform"), 
    path("getform/", views.getform, name="getform"),
    path('menu/<str:dish>/', views.dishesitem, name='menu'),
]


