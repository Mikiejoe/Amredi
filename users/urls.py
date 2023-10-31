from django.urls import path
from . import views

urlpatterns = [
    path('create/',views.CreateUser.as_view(), name='create' ),
    path('createfxn/',views.createuser, name='createu' )
]
