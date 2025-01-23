from django.urls import path
from posts import views
urlpatterns = [
    # path('<int:id>/',views.showPage),
    # path('home/', views.home),
    path('',views.homePage),
    path('allPosts/',views.getAllPosts),
    path('allPosts/<int:id>/',views.individualPost,name='individual_post')
]
