from django.urls import path
from . import views

urlpatterns =[
    path('',views.homepage,name='homepage'),
    path('registration/',views.registration, name='registration'),
    path('login/',views.log_in,name='login'),
    path('logout/',views.log_out,name='logout'),
    path('blogs/<int:id>/',views.post_detail,name='post_detail'),
    path('blogs/create/',views.create_post,name='create_post')
]