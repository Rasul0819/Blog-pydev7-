from django.urls import path
from . import views

urlpatterns =[
    path('',views.homepage,name='homepage'),
    path('registration/',views.registration, name='registration'),
    path('login/',views.log_in,name='login'),
    path('logout/',views.log_out,name='logout'),
    path('blogs/<int:id>/',views.post_detail,name='post_detail'),
    path('blogs/create/',views.create_post,name='create_post'),
    path('blogs/<int:id>/update',views.update_post,name='update'),
    path('blogs/<int:id>/delete',views.delete_post,name='delete')
]