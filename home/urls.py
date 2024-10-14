from django.urls import path

from .views import home_view,why_this_site,my_saves,chat,tutorial,my_funds,my_investments,comment

app_name = 'home'

urlpatterns = [

    path('' , home_view , name = 'home_view'),
    
    path('why_this_site',why_this_site , name= 'why_this_site'),

    path('my_saves',my_saves,name='my_saves'),

    path('chat',chat,name='chat'),

    path('tutorial',tutorial,name='tutorial'),

    path('my_funds',my_funds,name='my_funds'),

    path('my_investments',my_investments,name='my_investments'),

    path('comment',comment,name='comment'),





]