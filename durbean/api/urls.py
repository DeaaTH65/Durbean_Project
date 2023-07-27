from django.urls import path
from .views import CustomUserViewSet, getRoutes

user_list = CustomUserViewSet.as_view({'get': 'list'})
user_register = CustomUserViewSet.as_view({'post': 'register'})
user_login = CustomUserViewSet.as_view({'post': 'login'})
user_logout = CustomUserViewSet.as_view({'post': 'logout'})



urlpatterns = [
    path('', getRoutes, name='Routes'),
    path('users/', user_list, name='user-list'),
    path('register/', user_register, name='user-register'),
    path('login/', user_login, name='user-login'),
    path('api/logout/', user_logout, name='user-logout'),
]
