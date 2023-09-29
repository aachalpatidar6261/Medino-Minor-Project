from django.urls import path
from . import views

urlpatterns = [    
    path('',views.index,name='index'),
    path('doctor/',views.doctor_index,name='doctor'),
    path('signup/',views.signup,name='signup'),
    path('login',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('department/',views.department,name='department'),
    path('doctors/',views.doctors,name='doctors'),
    path('contact/',views.contact,name='contact'),
    path('change-password/',views.change_password,name='change-password'),
    path('profile/',views.profile,name='profile'),
    path('forgot-password/',views.forgot_password,name='forgot-password'),
    path('verify-otp/',views.verify_otp,name='verify-otp'),
    path('new-password/',views.new_password,name='new-password'),
    path('take-appointment/',views.take_appointment,name='take-appointment'),
    path('dr-view-appointment/',views.dr_view_appointment,name='dr-view-appointment'),

    path('ajax/validate-email/',views.validate_signup,name='ajax/validate-email'),


]
