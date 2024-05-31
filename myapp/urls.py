
from django.urls import path
from . import views

urlpatterns = [
    path('send-email/', views.send_email_function, name='send_email_function'),
    #path('', views.login_view, name='login_view')
]
