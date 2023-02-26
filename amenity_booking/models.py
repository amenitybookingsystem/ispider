from django.db import models
from django import forms
from django.core.exceptions import ValidationError
import re
from django.contrib import admin
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save # Produce a signal if there is any database action.
from django.core.validators import MinValueValidator
from django.utils import timezone
from datetime import datetime, date



def validate_date(value):
    today = timezone.now().date()
    if value <= today:
        raise ValidationError("Date should be tomorrow or later.")

    booked_dates=[]

    x = booking_table.objects.all()
    temp = ''

    for i in x:
        temp = temp + str(i.date)
        temp = temp[0:8]
        temp = temp.replace('/','')
        booked_dates.append(str(temp))
        temp = ''

    y = str(value)
    y = y[-2] + y[-1] + y[-5] + y[-4] + y[2:4]
    y = str(y)


    if(y in booked_dates):
        raise ValidationError("Date already booked by someone !")

    return value

def validate_apt_no(data):
    try:
        data = int(data)
    except ValueError:
        raise forms.ValidationError('Input must be an integer')
    if((data <= 100) or (data > 200)):
        raise forms.ValidationError('Given range for apartment no is only 101 - 200')
    return data

def validate_phone(data):

    if(data.isdigit() and len(data)==10):
        if master.objects.filter(phone=data).exists():
            raise forms.ValidationError('Phone number already exists in master')
    else:
        raise forms.ValidationError('Please give a valid mobile number')
    return data

def validate_email(data):

    if master.objects.filter(email=data).exists():
            raise forms.ValidationError('Email id already exists in master')

    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if(re.fullmatch(regex, data)):
        return data
 
    else:
        raise forms.ValidationError('Please give a valid email id')

def validate_slots(data):
    try:
        am = amenity_slots.objects.all()
        for x in am:
            if( str(x.slot).lower()==str(data).lower()):
                raise forms.ValidationError('Slot already exists !')
    except:
            raise forms.ValidationError("Please enter valid slot, check if it already exists")
    return data

def validate_amenity(data):
    name = amenity_type.objects.all()
    for x in name:
        if(x.name.lower()==data.lower()):
            raise forms.ValidationError('Amenity already exists !')

def validate_hours(data):
    if(data>12):
       raise forms.ValidationError('Active hours is limited to 12 !')
    return data 

def validate_space(data):

    if(data<0):
            raise forms.ValidationError("Please enter proper integer value !")

    return data

class master(models.Model):
    apt_no = models.CharField(max_length=3, primary_key=True, validators=[validate_apt_no])
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30,blank=True)
    phone = models.CharField(max_length=10)
    email = models.CharField(max_length=50)


    def __str__ (self):
        return self.first_name

    class Meta:
        verbose_name_plural = "1) Master Table"

    def clean(self):
        data = self.phone
        data2 = self.email
        if(data.isdigit() and len(data)==10):
            if (master.objects.filter(phone=data).exclude(pk=self.pk)).exists():
                raise forms.ValidationError('Phone number already exists in master')
        else:
            raise forms.ValidationError('Please give a valid mobile number')

        if (master.objects.filter(email=data2).exclude(pk=self.pk)).exists():
            raise forms.ValidationError('Email id already exists in master')

        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if(re.fullmatch(regex, data2)):
            return data2
        else:
            raise forms.ValidationError('Please give a valid email id')

    

class signup_table(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30,blank=True)
    username = models.CharField(max_length=16)
    apt_no = models.CharField(max_length=3, validators=[validate_apt_no])
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=10,blank=True)

    def __str__ (self):
        return self.first_name

    class Meta:
        verbose_name_plural = "2) Signup Table"

    def clean(self):
        data = self.phone
        data2 = self.email
        if(data.isdigit() and len(data)==10):
            if (signup_table.objects.filter(phone=data).exclude(pk=self.pk)).exists():
                raise forms.ValidationError('Phone number already exists in signup table')
        else:
            raise forms.ValidationError('Please give a valid mobile number')

        if (signup_table.objects.filter(email=data2).exclude(pk=self.pk)).exists():
            raise forms.ValidationError('Email id already exists in Signup table')

        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if(re.fullmatch(regex, data2)):
            return data2
        else:
            raise forms.ValidationError('Please give a valid email id')

class contact_table(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    message = models.CharField(max_length=500)

    def __str__ (self):
        return self.name

    class Meta:
        verbose_name_plural = "4) Contact Table"

TIMING_CHOICE = [('12AM-1AM', '12AM-1AM'),                 
                ('1AM-2AM', '1AM-2AM'),                 
                ('2AM-3AM', '2AM-3AM'),                 
                ('3AM-4AM', '3AM-4AM'),                 
                ('4AM-5AM', '4AM-5AM'),                 
                ('5AM-6AM', '5AM-6AM'),                 
                ('6AM-7AM', '6AM-7AM'),                 
                ('7AM-8AM', '7AM-8AM'),                 
                ('8AM-9AM', '8AM-9AM'),                 
                ('9AM-10AM', '9AM-10AM'),                 
                ('10AM-11AM', '10AM-11AM'),                 
                ('11AM-12PM', '11AM-12PM'),                 
                ('12PM-1PM', '12PM-1PM'),                 
                ('1PM-2PM', '1PM-2PM'),                 
                ('2PM-3PM', '2PM-3PM'),                 
                ('3PM-4PM', '3PM-4PM'),                 
                ('4PM-5PM', '4PM-5PM'),                 
                ('5PM-6PM', '5PM-6PM'),                 
                ('6PM-7PM', '6PM-7PM'),                 
                ('7PM-8PM', '7PM-8PM'),                 
                ('8PM-9PM', '8PM-9PM'),                 
                ('9PM-10PM', '9PM-10PM'),                 
                ('10PM-11PM', '10PM-11PM'),                 
                ('11PM-12AM', '11PM-12AM')]


PAYMENT_CHOICE = [('Pending', 'Pending'),
                 ('Paid', 'Paid'),]


AMOUNT_CHOICE = [('100', '100'),
                 ('250', '250')]


class booking_table(models.Model):
    username = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    apt_no = models.CharField(max_length=3)
    partner_name = models.CharField(max_length=30, null=True, blank=True)
    partner_apt_no = models.CharField(max_length=3, null=True, blank=True)
    amenity_name = models.CharField(max_length=30)
    date = models.CharField(max_length=30)
    slot = models.CharField(max_length=30, verbose_name='Slot Name')
    time = models.CharField(max_length=30)
    payment_method = models.CharField(max_length=30)
    booking_id = models.CharField(max_length=50, null=True)
    amount = models.IntegerField(default=0, validators=[validate_space])
    payment_status = models.CharField(max_length=30, choices=PAYMENT_CHOICE, blank=True, null=True)
    book_time = models.CharField(max_length=30, blank=True)
    space = models.IntegerField(default=0, validators=[validate_space])

    def __str__(self):
        return self.name + " - " + self.amenity_name + " - " + self.date + " - " + self.slot

    class Meta:
        verbose_name_plural = "3) Bookings Table"


class amenity_type(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    housing_space = models.IntegerField(default=0, validators=[validate_space])
    allow_multiple_bookings = models.BooleanField(default=False)
    base_rate = models.IntegerField(default=0, validators=[validate_space])
    extra_rate_per_person = models.IntegerField(default=0, validators=[validate_space])
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "5) Amenity Name Table"

    def clean(self):
        n = self.name
        other = amenity_type.objects.all().exclude(pk=self.pk)
        for x in other:
            if((x.name.lower()).replace(' ','')==(n.lower()).replace(' ','')):
                raise forms.ValidationError('Amenity already exists !')

class amenity_slots(models.Model):
    amenity_name = models.ForeignKey(amenity_type, on_delete=models.CASCADE, null=True)
    slot = models.CharField(max_length=100, blank=True, null=True)


    class Meta:
        verbose_name_plural = "6) Amenity Slots Table"
        unique_together = (("amenity_name", "slot"),)

    def __str__(self):
        return self.amenity_name.name + " - " + self.slot

    def clean(self):
        n = self.slot
        other = amenity_slots.objects.all().exclude(pk=self.pk)
        for x in other:
            if((x.slot.lower()).replace(' ','')==(n.lower()).replace(' ','')):
                raise forms.ValidationError('Slot already exists !')


class amenity_timings(models.Model):
    amenity_name = models.ForeignKey(amenity_type, on_delete=models.CASCADE, null=True)
    timing = models.CharField(max_length=100, choices=TIMING_CHOICE, blank=True, null=True)

    class Meta:
        verbose_name_plural = "7) Amenity Timing Table"
        unique_together = (("amenity_name", "timing"),)

    def __str__(self):
        return self.amenity_name.name + " - " + self.timing

class uidtable(models.Model):
    unique = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        verbose_name_plural = "System Info 1"

class filled(models.Model):
    amenity_name = models.CharField(max_length=100, blank=True, null=True)
    amenity_slot = models.CharField(max_length=100, blank=True, null=True)
    amenity_date = models.CharField(max_length=100, blank=True, null=True)
    amenity_timing = models.CharField(max_length=100, blank=True, null=True)
    total_space = models.IntegerField(blank=True, null=True)
    available_space = models.IntegerField(blank=True, null=True)
    booking_id = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name_plural = "System Info 2"

class amenity_maintenance(models.Model):
    slot= models.ForeignKey(amenity_slots, on_delete=models.CASCADE, null=True)
    time = models.ForeignKey(amenity_timings, on_delete=models.CASCADE, null=True)
    date = models.DateField()

    class Meta:
        verbose_name_plural = "8) Amenity Maintenance"
        unique_together = (("slot", "time","date"),)

    def __str__(self):
        return self.slot.__str__() + " - " + self.time.__str__()

    def clean(self):
        super().clean()
        if self.slot.amenity_name != self.time.amenity_name:
            raise ValidationError("Slot and time must be associated with the same amenity")

        today = timezone.now().date()

        value = self.date

        value2 = (self.slot).amenity_name

        if value <= today:
            raise ValidationError("Date should be tomorrow or later.")

        booked_dates=[]

        x = booking_table.objects.filter(amenity_name=value2)
        temp = ''

        for i in x:
            temp = temp + str(i.date)
            temp = temp[0:8]
            temp = temp.replace('/','')
            booked_dates.append(str(temp))
            temp = ''

        y = str(value)
        y = y[-2] + y[-1] + y[-5] + y[-4] + y[2:4]
        y = str(y)


        if(y in booked_dates):
            raise ValidationError("Date already booked by someone !")








