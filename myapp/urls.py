from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('contact/',views.contact,name='contact'),
    path('about/',views.about,name='about'),
    path('doctors/',views.doctors,name='doctors'),
    path('sign_up/',views.sign_up,name='sign_up'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('change_password/',views.change_password,name='change_password'),
    path('doctor_profile/',views.doctor_profile,name='doctor_profile'),
    path('doctor_details/<int:pk>/',views.doctor_details,name='doctor_details'),
    path('book_appointment/<int:pk>',views.book_appointment,name='book_appointment'),
    path('myappointment/',views.myappointment,name="myappointment"),
    path('patient_cencel_appoinment/<int:pk>/',views.patient_cencel_appoinment,name="patient_cencel_appoinment"),
    path('doctor_index/',views.doctor_index,name="doctor_index"),
    path('health_profile/',views.health_profile,name="health_profile"),
    path('doctor_appointment/',views.doctor_appointment,name='doctor_appointment'),
    path('doctor_approve_appointment/<int:pk>',views.doctor_approve_appointment,name='doctor_approve_appointment'),
    path('doctor_complete_appointment/<int:pk>',views.doctor_complete_appointment,name='doctor_complete_appointment'),
    path('doctor_cencel_appoinment/<int:pk>',views.doctor_cencel_appoinment,name='doctor_cencel_appoinment'),

]
