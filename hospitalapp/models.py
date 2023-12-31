from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Doctor(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=50)
    mobile = models.IntegerField()
    special = models.CharField(max_length=50)
    image = models.ImageField(upload_to='image/', blank=True)


    def __str__(self):
       return self.name;

class Patient(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    mobile = models.IntegerField(null=True)
    address = models.CharField(max_length=50)
    image = models.ImageField(upload_to='image/', blank=True)


    def __str__(self):
       return self.name;

class Patient1(models.Model):
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    mobile = models.IntegerField(null=True)
    address = models.CharField(max_length=50)
    username = models.CharField(max_length=50,null=True)
    image = models.ImageField(upload_to='image/', blank=True)
    email=models.EmailField(null=True)

    def __str__(self):
       return self.name;

class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    patientno=models.CharField(max_length=255,null=True)
    date1 = models.DateField()
    time1 = models.TimeField()
    token = models.CharField(max_length=255,null=True)
    Symptoms = models.CharField(max_length=255,null=True)

    def __str__(self):
       return self.doctorname+"--"+self.patient.name;


class Appointment1(models.Model):
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    patientno=models.CharField(max_length=255,null=True)
    date1 = models.DateField()
    time1 = models.TimeField()
    token = models.CharField(max_length=255,null=True)
    Symptoms = models.CharField(max_length=255,null=True)

    def __str__(self):
       return self.doctorname+"--"+self.patient.name;

class Contact(models.Model):
    name = models.CharField(max_length=100, null=True)
    contact = models.CharField(max_length=15, null=True)
    email = models.CharField(max_length=50, null=True)
    subject = models.CharField(max_length=100, null=True)
    message = models.CharField(max_length=300, null=True)
    msgdate = models.DateField(null=True)
    isread = models.CharField(max_length=10,null=True)

    def __str__(self):
        return self.id
class Pharmacy(models.Model):
    Doctor1=models.CharField(max_length=255,null=True)
    Patient1=models.CharField(max_length=255,null=True)
    Symptoms=models.CharField(max_length=255,null=True)
    medicine=models.CharField(max_length=255,null=True)
    Patientno=models.CharField(max_length=255,null=True)
class Pharmacy1(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    Name = models.CharField(max_length=255,null=True)
class Pharmacy2(models.Model):
    Doctor1=models.CharField(max_length=255,null=True)
    Patient1=models.CharField(max_length=255,null=True)
    Symptoms=models.CharField(max_length=255,null=True)
    medicine=models.CharField(max_length=255,null=True)
    Patientno=models.CharField(max_length=255,null=True)
    