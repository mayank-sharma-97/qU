from django.urls import path

from . import views

urlpatterns = [
    path('sign_up', views.sign_up, name='sign_up'),
    path('sign_in', views.sign_in, name='sign_in'),
    path('ticket_gen', views.create_ticket, name='ticket'),
    path('check_queue', views.check_queue, name='check_queue'),
    path('Processed', views.clear_ticket, name='check_queue'),
    path('', views.index, name='signin'),
    path('signup', views.signup, name='signup')

]
