from django.urls import path
from . import views
urlpatterns =[
    path('',views.index,name='index'),
    path('signup/',views.sign_up,name='signup'),
    path('login/',views.signup,name='login'),
    path('post/',views.login,name='post'),
    path('post1/',views.post_get,name='post1'),
    path('update_post/',views.update_post,name='update_post'),
    path('update/',views.update,name='update'),
    path('update1/<int:id>',views.update1,name='update1'),
    path('back_post/',views.back_post,name='back_post'),
]
