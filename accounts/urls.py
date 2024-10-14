from django.urls import path

from .views import register_view,dashboard_view,login_view,logout_view,edit_profile,edit,search

app_name = 'accounts'

urlpatterns = [

    path('register' , register_view , name = 'register_view'),

    path('login' , login_view , name = 'login_view'),

    path('dashboard',dashboard_view,name='dashboard_view'),

    path('logout', logout_view, name = 'logout_view'),

    path('edit_profile',edit_profile,name='edit_profile'),

    path('<id>/' , edit , name = 'edit'),

    path('search',search,name='search'),

    
]