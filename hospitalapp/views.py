from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login
from .models import *
from datetime import date
from django.contrib import messages
import random
from django.core.mail import send_mail
from django.conf import settings
import os
from django.contrib.auth import update_session_auth_hash
# Create your views here.
def pharsignup(request):
    if request.method=='POST':
        n = request.POST['name']

        p = request.POST['User']

        e = request.POST['pass']
        use = User.objects.create_user(username=p,password=e)
        use.save()
        usr=Pharmacy1(user=use,Name=n)
        usr.user= use
        usr.save()
    return render(request,'login.html')
def search_view2(request):
    # whatever user write in search box we get in query
    query = request.GET['query']
    products=Pharmacy.objects.all().filter(Patientno__icontains=query)
    if 'patient_id' in request.COOKIES:
        patient_id = request.COOKIES['patient_id']


    # word variable will be shown in html when user click on search button
    word="Searched Result :"

    if request.user.is_authenticated:
        return render(request,'docscearch.html',{'products':products,'word':word,})
    return render(request,'admin_home.html')
def search_view1(request):
    # whatever user write in search box we get in query
    query = request.GET['query']
    products=Pharmacy.objects.all().filter(Patientno__icontains=query)
    if 'patient_id' in request.COOKIES:
        patient_id = request.COOKIES['patient_id']


    # word variable will be shown in html when user click on search button
    word="Searched Result :"

    if request.user.is_authenticated:
        return render(request,'pharscearch.html',{'products':products,'word':word,})
    return render(request,'admin_home.html')
def docsearch(request):
        return render(request,'docscearch.html')
def pharmacysignup(request):
        return render(request,'phar.html')
def appoimentscearch(request):
        return render(request,'searchappointment.html')
def pharmcyscearch(request):
        return render(request,'pharscearch.html')
def phalogin(request):
        return render(request,'pharscearch.html')

def search_view(request):
    # whatever user write in search box we get in query
    query = request.GET['query']
    products=Appointment1.objects.all().filter(patientno__icontains=query)
    if 'patient_id' in request.COOKIES:
        patient_id = request.COOKIES['patient_id']


    # word variable will be shown in html when user click on search button
    word="Searched Result :"

    if request.user.is_authenticated:
        return render(request,'searchappoiment.html',{'products':products,'word':word,})
    return render(request,'admin_home.html')
def update_password1(request):
    if request.method == 'POST':
        current_password = request.POST.get('current_password')
        new_password = request.POST.get('new_password')
        confirm_new_password = request.POST.get('confirm_new_password')

        if request.user.check_password(current_password):
            
            if new_password == confirm_new_password:
                
                request.user.set_password(new_password)
                request.user.save()

                update_session_auth_hash(request, request.user)

                messages.success(request, 'Your password was successfully updated!')
                return render(request,'login.html')
        else:
            messages.error(request, 'Incorrect current password.')

    return render(request, 'pat_resetpassword.html')

def patientreset(request):
    user=request.user.id
    Doctor1 = Patient.objects.get(user_id=user)
    return render(request,'pat_resetpassword.html',{'patient':Doctor1})
def update_password(request):
    if request.method == 'POST':
        current_password = request.POST.get('current_password')
        new_password = request.POST.get('new_password')
        confirm_new_password = request.POST.get('confirm_new_password')

        if request.user.check_password(current_password):
            
            if new_password == confirm_new_password:
                
                request.user.set_password(new_password)
                request.user.save()

                update_session_auth_hash(request, request.user)

                messages.success(request, 'Your password was successfully updated!')
                return render(request,'login.html')
        else:
            messages.error(request, 'Incorrect current password.')

    return render(request, 'doctor_resetpassword.html')

def doctorreset(request):
    user=request.user.id
    Doctor1 = Doctor.objects.get(user_id=user)
    return render(request,'doctor_resetpassword.html',{'doctor':Doctor1})
def doctorlogin(request):
    user=request.user.id
    Doctor1 = Doctor.objects.get(user_id=user)
    return render(request,'doctorlogin.html',{'doctor':Doctor1})
def pharmacy(request):
    if not request.user.is_authenticated:
        return redirect('login')
    contact = Pharmacy.objects.all()
    return render(request,'pharmacy.html', {'contact':contact})
def delete2(request,pk):

    pro = Appointment.objects.get(id=pk)
    usr=Appointment1.objects.create(doctor=pro.doctor, patient=pro.patient, date1=pro.date1, time1=pro.time1,token=pro.token)
    usr.save()
    pro.delete()
    return render(request,'patlogin.html')
def patient_dashboard_view(request):

    user=request.user.id
    patient1 = Patient.objects.get(user_id=user)
    d=Patient.objects.get(user_id=user)
    appointment = Appointment.objects.filter(patient_id=d.id)
    d = {'appointment':appointment,'patient':patient1}
    return render(request,'patient_dashboard_view.html',d)
def doctor_dashboard_view(request):
    user=request.user.id
    Doctor1=Doctor.objects.get(user_id=user)
    appointment = Appointment.objects.filter(doctor_id=Doctor1.id)
    d = {'appointment':appointment,'doctor':Doctor1}
    return render(request,'doctor_dashboard_view.html', d)

def viewdoctor(request):
    user=request.user.id
    patient1 = Patient.objects.get(user_id=user)
    use=User.objects.all()
    doc = Doctor.objects.all()
    d = {'doc':doc,'use':use,'patient':patient1}
    return render(request,'doctorview.html', d)
def About(request):
    return render(request,'about.html')
# def pathome(request):
#     return render(request,'patentpage.html')
def add_doctor1(request):
    return render(request,'add_doctor.html')
def add_pat1(request):
    return render(request,'add_patient.html')
def refer(request,pk):
    user=request.user.id
    Doctor1 = Doctor.objects.get(user_id=user)
    v=Appointment.objects.get(id=pk)
    c=Doctor.objects.all()
    return render(request,'Refer.html',{'v':v,'c':c,'doctor':Doctor1})
def Index(request):
    return render(request,'index.html')
def signupp(request):
    return render(request,'patient_signup.html')
def approve(request,pk):
    pro = Patient1.objects.get(id=pk)
    pa = str(random.randint(100000,999999))
    use = User.objects.create_user(email=pro.email,username=pro.username,password=pa)
    use.save()
    usr=Patient(name=pro.name,gender=pro.gender,mobile=pro.mobile,address=pro.address,image=pro.image)
    usr.user= use
    usr.save()
    pro.delete()
    subject='Your Approval has been successful'
    message=f' sir, ur patient username={usr.user.username} \n user_id={usr.id}'' password={} '.format(pa)
    recipient=use.email
    send_mail(subject,message,settings.EMAIL_HOST_USER,[recipient])
    return render(request, 'admin_home.html', locals())

def patient_signup(request):
    error = ""
    if request.method == 'POST':
        n = request.POST['name']
        g = request.POST['gender']
        m = request.POST['mobile']
        a = request.POST['address']
        p = request.POST['User']
        i = request.FILES['image']
        e = request.POST['mail']

        try:
            usr=Patient1.objects.create(name=n, gender=g, mobile=m,username=p,address=a,image=i,email=e)
            usr.save()

            error = "no"
        except:
            error = "yes"
    return render(request,'patient_signup.html', locals())

def contact(request):
    error = ""
    if request.method == 'POST':
        n = request.POST['name']
        c = request.POST['contact']
        e = request.POST['email']
        s = request.POST['subject']
        m = request.POST['message']
        try:
            Contact.objects.create(name=n, contact=c, email=e, subject=s, message=m, msgdate=date.today(), isread="no")
            error = "no"
        except:
            error = "yes"
    return render(request, 'contact.html', locals())

def adminlogin(request):

    if request.method == 'POST':
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        don1=Doctor.objects.filter(user=user)
        pat1=Patient.objects.filter(user=user)
        pha1=Pharmacy1.objects.filter(user=user)
        if user is not None:
            if don1:
                login(request,user)
                Doctor1 = Doctor.objects.get(user_id=user)
                return render(request,'doctorlogin.html',{'doctor':Doctor1})
            elif pat1:
                login(request,user)
                patient1 = Patient.objects.get(user_id=user)
                return render(request,'patlogin.html',{'patient':patient1})
            elif pha1:
                login(request,user)
                return render(request,'phrlogin.html')
            else :
                login(request,user)
                return redirect('admin_home')
        else:
            return render(request,'login.html', locals())
    else:

       return render(request,'login.html', locals())
def pathome(request):
    user=request.user.id
    patient1 = Patient.objects.get(user_id=user)
    return render(request,'patlogin.html',{'patient':patient1})

def admin_home(request):
    if not request.user.is_staff:
        return redirect('login_admin')
    dc = Doctor.objects.all().count()
    pc = Patient.objects.all().count()
    ac = Appointment.objects.all().count()

    d = {'dc': dc, 'pc': pc, 'ac': ac}
    return render(request,'admin_home.html', d)

def Logout(request):
    logout(request)
    return redirect('index')

def add_doctor(request):
    error=""
    if request.method=='POST':
        n = request.POST['name']
        m = request.POST['mobile']
        sp = request.POST['special']
        p = request.POST['User']
        img = request.FILES['image']
        e = request.POST['mail']
        pa = str(random.randint(100000,999999))
        use = User.objects.create_user(email=e,username=p,password=pa)
        use.save()
        usr=Doctor(user=use,name=n,mobile=m,special=sp,image=img)
        usr.user= use
        usr.save()
        subject='Your Approval has been successful'
        message=f' sir, ur username ={usr.user.username}'' password={} '.format(pa)
        recipient=use.email
        send_mail(subject,message,settings.EMAIL_HOST_USER,[recipient])
        try:
    
            error = "no"
        except:
            error = "yes"
    return render(request,'view_doctor.html')

def view_doctor(request):
    use=User.objects.all()
    doc = Doctor.objects.all()
    d = {'doc':doc,'use':use}
    return render(request,'view_doctor.html', d)

def Delete_Doctor(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    doctor = Doctor.objects.get(id=pid)
    doctor.delete()
    return render(request,'view_doctor.html')

def edit_doctor(request,pid):
    error = ""
    if not request.user.is_authenticated:
        return redirect('login')
    user = request.user
    doctor = Doctor.objects.get(id=pid)
    if request.method == "POST":
        n1 = request.POST['name']
        m1 = request.POST['mobile']
        s1 = request.POST['special']
        if len(request.FILES)!=0:
            if len(doctor.image)>0:
                os.remove(doctor.image.path)
                doctor.image=request.FILES['image']
            else :
                doctor.image=request.FILES['image']

        doctor.name = n1
        doctor.mobile = m1
        doctor.special = s1

        try:
            doctor.save()
            error = "no"
        except:
            error = "yes"
    return render(request, 'edit_doctor.html', locals())

def add_patient(request):
    error=""
    if request.method == 'POST':
        n = request.POST['name']
        g = request.POST['gender']
        m = request.POST['mobile']
        a = request.POST['address']
        p = request.POST['User']
        i = request.FILES['image']
        e = request.POST['mail']
        pa = str(random.randint(100000,999999))
        use = User.objects.create_user(email=e,username=p,password=pa)
        use.save()
        usr=Patient(user=use,name=n,gender=g,mobile=m,address=a,image=i)
        usr.user= use
        usr.save()
        subject='Your Approval has been successful'
        message=" sir, ur patient id={} password={} ".format(p,pa)
        recipient=use.email
        send_mail(subject,message,settings.EMAIL_HOST_USER,[recipient])
        try:
    
            error = "no"
        except:
            error = "yes"
    return redirect('/')

def view_patient(request):
    if not request.user.is_staff:
        return redirect('login')
    pat = Patient.objects.all()
    d = {'pat':pat}
    return render(request,'view_patient.html', d)
def view_notification(request):
    if not request.user.is_staff:
        return redirect('login')
    pat = Patient1.objects.all()
    d = {'pat':pat}
    return render(request,'admin_notification.html', d)

def Delete_Patient(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    patient = Patient.objects.get(id=pid)
    patient.delete()
    return render(request,'view_doctor.html')
def Delete_Patient1(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    patient = Patient1.objects.get(id=pid)
    patient.delete()
    return render(request,'view_patient.html')

def edit_patient(request,pid):
    error = ""
    if not request.user.is_authenticated:
        return redirect('login')
    patient = Patient.objects.get(id=pid)
    if request.method == "POST":
        n1 = request.POST['name']
        m1 = request.POST['mobile']
        g1 = request.POST['gender']
        a1 = request.POST['address']
        if len(request.FILES)!=0:
            if len(patient.image)>0:
                os.remove(patient.image.path)
                patient.image=request.FILES['image']
            else :
                patient.image=request.FILES['image']

        patient.name = n1
        patient.mobile = m1
        patient.gender = g1
        patient.address = a1


        try:
            patient.save()
            error = "no"
        except:
            error = "yes"
    return render(request, 'edit_patient.html', locals())


def add_appointment(request):
    error=""
    if not request.user.is_staff:
        return redirect('login')
    doctor1 = Doctor.objects.all()
    patient1 = Patient.objects.all()
    if request.method=='POST':
        d = request.POST['doctor']
        p = request.POST['patient']
        pid=request.POST['patientid']
        d1 = request.POST['date']
        t = request.POST['time']
        s = request.POST['Sym']
        doctor = Doctor.objects.filter(name=d).first()
        patient = Patient.objects.filter(name=p).first()
        tk = str(random.randint(1,100))
        try:
            Appointment.objects.create(doctor=doctor, patient=patient, date1=d1, time1=t,token=tk,Symptoms=s,patientno=pid)
            error="no"
        except:
            error="yes"
    d = {'doctor':doctor1,'patient':patient1,'error':error}
    return render(request,'add_appointment.html', d)
def addappointment(request):
    doctor1 = Doctor.objects.all()
    user=request.user.id
    patient1 = Patient.objects.get(user_id=user)
    if request.method=='POST':
        d = request.POST['doctor']
        p = request.POST['patient']
        d1 = request.POST['date']
        t = request.POST['time']
        s = request.POST['Sym']
        doctor = Doctor.objects.filter(name=d).first()
        patient = Patient.objects.filter(name=p).first()
        tk = str(random.randint(1,100))

        Appointment.objects.create(doctor=doctor, patient=patient, date1=d1, time1=t,token=tk,Symptoms=s)

    d = {'doctor':doctor1,'patient':patient1}
    return render(request,'patbook.html', d)

def editpatient(request,pid):
   
   user=request.user.id
   Doctor1 = Doctor.objects.get(user_id=user)
   patient= Appointment.objects.get(id=pid)
   if request.method == "POST":
        n1 = request.POST['pname']
        m1 = request.POST['dname']
        g1 = request.POST['symptoms']
        p1 = request.POST['patno']
        a1 = request.POST['medicine']

   
        phr=Pharmacy(Doctor1=n1,Patient1=m1,Symptoms=g1,medicine=a1,Patientno=p1)



        try:
            phr.save()
            error = "no"
        except:
            error = "yes"


   return render(request,'Digonosis.html' ,{'patient':patient,'doctor':Doctor1})

def view_appointment(request):
    if not request.user.is_staff:
        return redirect('login')
    appointment = Appointment.objects.all()
    d = {'appointment':appointment}
    return render(request,'view_appointment.html', d)

def Delete_Appointment(request,pk):
    pro = Appointment.objects.get(id=pk)
    usr=Appointment1.objects.create(doctor=pro.doctor, patient=pro.patient,patientno=pro.patientno,date1=pro.date1, time1=pro.time1,token=pro.token)
    usr.save()
    pro.delete()
    return render(request, 'admin_home.html', locals())

def unread_queries(request):
    if not request.user.is_authenticated:
        return redirect('login')
    contact = Contact.objects.filter(isread="no")
    return render(request,'unread_queries.html', locals())

def read_queries(request):
    if not request.user.is_authenticated:
        return redirect('login')
    contact = Contact.objects.filter(isread="yes")
    return render(request,'read_queries.html', locals())

def view_queries(request,pid):
    if not request.user.is_authenticated:
        return redirect('login')
    contact = Contact.objects.get(id=pid)
    contact.isread = "yes"
    contact.save()
    return render(request,'view_queries.html', locals())