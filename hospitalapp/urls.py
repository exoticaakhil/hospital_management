from django.urls import path
from .views import *

urlpatterns = [
    path('about/', About, name="about"),
    path('',Index,name='index'),
    path('contact', contact, name='contact'),
    path('search_view', search_view, name='search_view'),
    path('search_view1', search_view1, name='search_view1'),
    path('search_view2', search_view2, name='search_view2'),
    path('pharmcyscearch', pharmcyscearch, name='pharmcyscearch'),
    path('appoimentscearch', appoimentscearch, name='appoimentscearch'),
    path('update_password', update_password, name='update_password'),
    path('update_password1', update_password1, name='update_password1'),
    path('doctorreset',doctorreset, name='doctorreset'),
    path('patientrest',patientreset, name='patientreset'),
    path('doctorlogin', doctorlogin, name='doctorlogin'),
    path('login', adminlogin, name='login'),
    path('admin_home', admin_home, name='admin_home'),
    path('logout', Logout, name='logout'),
    path('docsearch', docsearch, name='docsearch'),
    path('view_notification', view_notification, name='view_notification'),
    path('signupp', signupp, name='signupp'),
    path('approve/<int:pk>', approve, name='approve'),
    path('add_doctor', add_doctor, name='add_doctor'),
    path('add_doctor1', add_doctor1, name='add_doctor1'),
    path('add_pat1', add_pat1, name='add_pat1'),
    path('patient_signup', patient_signup, name='patient_signup'),
    path('view_doctor', view_doctor, name='view_doctor'),
    path('viewdoctor', viewdoctor, name='viewdoctor'),
    path('delete_doctor/<int:pid>', Delete_Doctor, name='delete_doctor'),
    path('add_patient', add_patient, name='add_patient'),
    path('view_patient', view_patient, name='view_patient'),
    path('editpatient/<int:pid>',editpatient,name='editpatient'),
    path('doctor_dashboard_view', doctor_dashboard_view, name='doctor_dashboard_view'),
    path('patient_dashboard_view', patient_dashboard_view, name='patient_dashboard_view'),
    path('delete_patient/<int:pid>', Delete_Patient, name='delete_patient'),
    path('delete_patient1/<int:pid>', Delete_Patient1, name='delete_patient1'),
    path('add_appointment', add_appointment, name='add_appointment'),
    path('view_appointment', view_appointment, name='view_appointment'),
    path('addappointment', addappointment, name='addappointment'),   
    path('delete_appointment/<int:pk>', Delete_Appointment, name='delete_appointment'),
    path('edit_doctor/<int:pid>',edit_doctor,name='edit_doctor'),
    path('edit_patient/<int:pid>',edit_patient,name='edit_patient'),
    path('unread_queries', unread_queries, name='unread_queries'),
    path('read_queries', read_queries, name='read_queries'),
    path('pharmacy', pharmacy, name='pharmacy'),
    path('pathome', pathome, name='pathome'),
    path('refer/<int:pk>',refer, name='refer'),
    path('delete2/<int:pk>',delete2, name='delete2'),
    path('view_queries/<int:pid>', view_queries, name='view_queries'),

]