from django.urls import path
from .import views
urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerUser, name='register'),
    path('profile/<str:pk>', views.profile, name='profile'),
    path('crud/<str:pk>', views.crud, name='crud'),
    path('Delete/<str:pk>', views.Delete, name='Delete'),
    
    path('submit/', views.submit_leave_request, name='submit_leave_request'),
    path('requests/', views.leave_requests, name='requests'),
    path('accept/<str:pk>/', views.accept_leave_request, name='accept_leave_request'),
]
