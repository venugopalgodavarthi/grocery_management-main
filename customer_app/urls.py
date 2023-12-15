from django.urls import path
from customer_app.views import *

app_name = 'customer_app'
urlpatterns = [
    path(route='customer_welcome/',
         view=customer_Welcome_view, name='customer_welcome'),
    path(route='customer_register/',
         view=customer_register_view, name='customer_register'),
    path(route='customer_update/',
         view=customer_update_view, name='customer_update'),
    path(route='customer_detail/',
         view=customer_detail_view, name='customer_detail'),
    path(route='customer_list/', view=customer_list_view, name='customer_list'),
    path(route='customer_login/', view=customer_login_view, name='customer_login'),
    path(route='customer_logout/',
         view=customer_logout_view, name='customer_logout'),
    path(route='customer_home/', view=customer_home_view, name='customer_home'),
    path(route='forgot_pwd/', view=forgot_pwd_view, name='forgot_pwd'),
    path(route='customer_otp/<int:pk>/',
         view=customer_otp_view, name='customer_otp'),
    path(route='change_pwd/', view=change_pwd_view, name='change_pwd'),


    path(route='admin_home/', view=admin_home_view, name='admin_home'),
]
