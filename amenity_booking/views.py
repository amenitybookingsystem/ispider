from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate 
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.sites.shortcuts import get_current_site
from ispider import settings
from .models import *
from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from . tokens import *
import re
from django.views import View
from django.shortcuts import redirect
import uuid
from datetime import date as cdate
from datetime import timedelta
from datetime import datetime as cdatetime
import json
from django.http import JsonResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import AllowAny
import pytz
# Create your views here.

def home(request):
    user = request.user
    if user is not None:
        auth_logout(request)
    return render(request, 'amenity_booking/home.html')


def signup(request):
    user = request.user
    if user is not None:
        auth_logout(request)        
    return render(request, 'amenity_booking/signup.html')

def forgot_password(request):       
    return render(request, 'amenity_booking/forgot_password.html')

def login(request):
    user = request.user
    if user is not None:
        auth_logout(request)
    return render(request, 'amenity_booking/login.html')

def contact(request):
    return render(request, 'amenity_booking/contact.html')

def about(request):
    return render(request, 'amenity_booking/about.html')

def saveSign(request):
    n=''
    if request.method=="POST":
        fn = request.POST.get('first_name')
        ln = request.POST.get('last_name')
        username = request.POST.get('username')
        apt = request.POST.get('apt_no')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        mas = master.objects.all()
        sup = signup_table.objects.all()

        if apt and len(apt)!=3:
            n = "Given range for apartment no is only 101 - 200"
            return render(request, 'amenity_booking/signup.html',{'n':n,'form':request.POST})

        if(emailvalidate(email)==0):
            n = "Please give a valid email id !"
            return render(request, 'amenity_booking/signup.html',{'n':n,'form':request.POST})

        if(phone.isdigit()=="False")or(len(phone)!=10):
            n = "Please give a valid mobile number !"
            return render(request, 'amenity_booking/signup.html',{'n':n,'form':request.POST})

        errors = []
        se = ''
        if len(password) < 8:
            errors.append("Password must be at least 8 characters long.")
        if not any(char.islower() for char in password):
            errors.append("Password must contain at least 1 lowercase letter.")
        if not any(char.isupper() for char in password):
            errors.append("Password must contain at least 1 uppercase letter.")
        if not any(char.isdigit() for char in password):
            errors.append("Password must contain at least 1 numeric digit.")

        if errors:
            se = "Invalid password: " + " ".join(errors)
            return render(request, 'amenity_booking/signup.html', {'n': se, 'form': request.POST})


        if User.objects.filter(username=username,email=email).exists():
            n = "Account with same username and email already exists !"
            return render(request, 'amenity_booking/signup.html', {'n': n, 'form': request.POST})

        if(User.objects.filter(username=username.lower()).exists()):
            n = "Username already taken"
            return render(request, 'amenity_booking/signup.html',{'n':n,'form':request.POST})

        
        n="Sorry ! Your credentials are not registered with our apartment."

        for y in sup:
            if(y.phone==phone):
                n = "Phone number already registered"
                return render(request, 'amenity_booking/signup.html',{'n':n,'form':request.POST})
            elif(y.apt_no==apt):
                n = "Apartment no already registered"
                return render(request, 'amenity_booking/signup.html',{'n':n,'form':request.POST})
            elif(y.email==email):
                n = "Email id already registered"
                return render(request, 'amenity_booking/signup.html',{'n':n,'form':request.POST})


        if(n=="Sorry ! Your credentials are not registered with our apartment."):   
            for x in mas:

                if((x.first_name.lower()==fn.lower())and(x.phone==phone)and(x.apt_no==apt)and(x.email==email)):
                    en = signup_table(first_name=fn, last_name=ln, username=username.lower(), 
                        apt_no=apt, email=email, phone=phone)
                    newuser = User.objects.create_user(username, email, password)
                    en.save()
                    newuser.first_name = fn
                    newuser.last_name = ln
                    newuser.is_active = False
                    newuser.save()
                    n = "Successfully registered. Please verify email before login !"

                    current_site = get_current_site(request)
                    email_subject = "Email verification"
                    message = render_to_string('amenity_booking/email_verification.html',{
                        'name': newuser.first_name,
                        'domain': current_site.domain,
                        'uid': urlsafe_base64_encode(force_bytes(newuser.pk)),
                        'token': generate_token.make_token(newuser)
                    })
                    email = EmailMessage(
                        email_subject, message,
                        settings.EMAIL_HOST_USER, [newuser.email],
                    )
                    email.fail_silently = True
                    email.send()

                    return render(request, 'amenity_booking/login.html',{'n':n})

                elif((x.first_name.lower()!=fn.lower())and(x.phone==phone)and(x.apt_no==apt)and(x.email==email)):
                    n="Please enter only registered first name !"
                    return render(request, 'amenity_booking/signup.html',{'n':n,'form':request.POST})
                else:
                    n="Sorry your credentials are not registered with our apartment."

        tempp = 1
        for x in mas:
            if(x.apt_no==apt):
                tempp = 0
                break

        if(tempp==1):
            n = "Apartment no is not registered with database !"
            return render(request, 'amenity_booking/signup.html',{'n':n,'form':request.POST})


        tempp = 1
        for x in mas:
            if(x.phone==phone):
                tempp = 0
                break

        if(tempp==1):
            n = "Phone no is not registered with database !"
            return render(request, 'amenity_booking/signup.html',{'n':n,'form':request.POST})

   
        tempp = 1
        for x in mas:
            if(x.email==email):
                tempp = 0
                break

        if(tempp==1):
            n = "Email id is not registered with database !"
            return render(request, 'amenity_booking/signup.html',{'n':n,'form':request.POST})
                
        
    return render(request, 'amenity_booking/signup.html',{'n':n,'form':request.POST})

def saveLogin(request):



    if request.method=='POST':
        n = ''
        form = request.POST
        username = request.POST['username']
        m = signup_table.objects.all()
        for x in m:
            if(username==x.phone):
                username = x.username
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:

            if user.username=='admin':
                auth_login(request, user)
                return redirect(adminbook)
            
            fname = user.first_name
            auth_login(request, user)
            request.session['n'] = n
            request.session['form'] = form
            return redirect(booking)
        else:
            n = 'Incorrect username or password'
            return render(request, 'amenity_booking/login.html', {'n':n})
        


def saveContact(request):
    if request.method =="POST":
        name= request.POST.get("name")
        email= request.POST.get("email")
        message= request.POST.get("message")
        variable = contact_table(name = name, email = email, message = message)
        variable.save()
        m = 'Message sent successfully'
        return render(request, 'amenity_booking/contact.html', {'m':m})



def activate(request, uidb64, token):
    n = ''
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        newuser = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        newuser = None

    if newuser is not None and generate_token.check_token(newuser, token):
        uidtab = uidtable.objects.values_list('unique',flat=True)

        for i in uidtab:
            if(str(token)==str(i)):
                n = "Account already activated !"
                return render(request, 'amenity_booking/login.html',{'n':n})

        newuser.is_active = True
        newuser.save()
        n = "Activation success !"
        variable = uidtable(unique=token)
        variable.save()
        return render(request, 'amenity_booking/login.html', {'n':n})
    else:
        n = "Activation failed !"
        return render(request, 'amenity_booking/login.html', {'n':n})

def email_password(request):

    try:
        current_site = get_current_site(request)
        email = request.POST.get('email')
        myuser = User.objects.get(email=email)

        email_subject = "Reset your password"
        message = render_to_string('amenity_booking/email_password.html',{
            'name': myuser.first_name,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(myuser.pk)),
            'token': generate_token.make_token(myuser)
            })
        email = EmailMessage(
            email_subject, message,
            settings.EMAIL_HOST_USER, [myuser.email],
            )
        email.fail_silently = True
        email.send()

        n = "Password reset link sent to your mail !"
        return render(request, 'amenity_booking/login.html',{'n':n})

    except:
        n = "Invalid / Unregistered email id"
        return render(request, 'amenity_booking/forgot_password.html',{'n':n})
    

def reset(request, uidb64, token):

    current_site = get_current_site(request)
    uid = force_str(urlsafe_base64_decode(uidb64))
    myuser = User.objects.get(pk=uid)
    uidtab = uidtable.objects.values_list('unique',flat=True)

    for i in uidtab:
        if(str(token)==str(i)):
            n = "Link expired, create a new one !"
            return render(request, 'amenity_booking/login.html',{'n':n})

    return render(request, 'amenity_booking/password_reset.html',{
        'name': myuser.first_name,
        'domain': current_site.domain,
        'uid': urlsafe_base64_encode(force_bytes(myuser.pk)),
        'token': token
    })
    
def reset_pass(request, uidb64, token):
    n = ''
    if request.method=="POST":
        password = request.POST['new_pass1']
        pass2 = request.POST['new_pass2']

        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            myuser = User.objects.get(pk=uid)

            errors = []
            se = ''
            if len(password) < 8:
                errors.append("Password must be at least 8 characters long.")
            if not any(char.islower() for char in password):
                errors.append("Password must contain at least 1 lowercase letter.")
            if not any(char.isupper() for char in password):
                errors.append("Password must contain at least 1 uppercase letter.")
            if not any(char.isdigit() for char in password):
                errors.append("Password must contain at least 1 numeric digit.")

            
            if errors:
                se = "Invalid password: " + " ".join(errors)
                current_site = get_current_site(request)
                uid = force_str(urlsafe_base64_decode(uidb64))
                myuser = User.objects.get(pk=uid)
                return render(request, 'amenity_booking/password_reset.html',{
                    'name': myuser.first_name,
                    'n':se,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(myuser.pk)),
                    'token': token
                    })
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None


        pass1 = password

        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            myuser = User.objects.get(pk=uid)
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if myuser is not None and generate_token.check_token(myuser, token):
            if(pass1==pass2):
                myuser.set_password(pass1)
                myuser.save()
                variable = uidtable(unique=token)
                variable.save()
                n = "Password reset successfully !"
                return render(request, 'amenity_booking/login.html', {'n':n})
            else:
                n = "Password doesn't match !"
                current_site = get_current_site(request)
                uid = force_str(urlsafe_base64_decode(uidb64))
                myuser = User.objects.get(pk=uid)
                return render(request, 'amenity_booking/password_reset.html',{
                    'name': myuser.first_name,
                    'n':n,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(myuser.pk)),
                    'token': generate_token.make_token(myuser)
                    })

        n = "Password reset successfully !"
        return render(request, 'amenity_booking/login.html', {'n':n})


def user_profile(request):
    details = signup_table.objects.get(username=request.user.username)
    return render(request, 'amenity_booking/userprofile.html', locals())


def currentbooking(request):
    n = ''
    try:
        n = request.session['n']
    except:
        n = ''

    if(n!="Here is your booking ! Email Sent"):
        n = "Here is your booking !"

    book = booking_table.objects.filter(username=request.user.username)

    current_date = cdatetime.now().strftime('%m/%y/%d')
    current_date = current_date.replace('/', '')
    current_date = int(current_date)

    all_list = []
    active_list = []
    completed_list = []
    
    for i in book:
        book_date = i.date
        book_date = book_date.replace('/', '')
        book_date = book_date[0:6]
        book_date = book_date[2] + book_date[3] + book_date[4] + book_date[5] + book_date[0] + book_date[1]
        book_date = int(book_date)
        if(current_date>=book_date):
            completed_list.append(book_date)
        else:
            active_list.append(book_date)
        all_list.append(book_date)

    mylist = zip(book, all_list)


    return render(request, 'amenity_booking/currentbooking.html', locals())


def previousbooking(request):
    return render(request, 'amenity_booking/previousbooking.html')

def logout(request):
    auth_logout(request)
    n = "Logged out successfully !"
    return render(request, 'amenity_booking/login.html', {'n':n})

def emailvalidate(data):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if(re.fullmatch(regex, data)):
        return 1
 
    else:
        return 0


def booknow(request):
    return redirect(booking)


def booking(request):

    try:
        form = request.session['form']
    except:
        user = request.user
        if user is not None:
            auth_logout(request)
        return render(request, 'amenity_booking/home.html')

    form = request.session['form']
    user = request.user
    username = user.username
    current = booking_table.objects.filter(username=username)
    d = []
    no = []
    for i in current:

        x = i.date
        x = x[0:2] + x[3:5] + x[6:8]
        x = int(x)
        today = cdate.today()
        d3 = today.strftime("%d%m%y")
        d3 = int(d3)

        if(x>d3):
            no.append(i.amenity_name)



    amenityid = request.GET.get('amenity', None)
    dateid = request.GET.get('date', None)
    slotid = request.GET.get('slot', None)
    spaceid = request.GET.get('space', None)
    slot = None
    timeid = request.GET.get('timing', None)
    timing = None
    space = 0
    temm = 0
    newfill = None
    available = 0
    newfill2 = None
    fill = None
    available = 0

    if amenityid:
        getamenity = amenity_type.objects.get(name=amenityid)
        slot = amenity_slots.objects.filter(amenity_name=getamenity)
    if slotid:
        timing = amenity_timings.objects.filter(amenity_name=getamenity)

    if timeid:

        newfill2 = amenity_type.objects.get(name=amenityid)
        newfill2 = newfill2.housing_space
        total = int(newfill2)

        fill = filled.objects.filter(amenity_name=amenityid, amenity_slot=slotid,
                                     amenity_date=dateid, amenity_timing=timeid)

        newfill = fill.values_list('available_space', flat=True)
        if(newfill.exists()):
            newfill = list(newfill)
            newfill.sort()
            available = int(newfill[0])
        else:
            available = total

        try:
            amenity_space = amenity_type.objects.get(name=getamenity)
            if amenity_space.allow_multiple_bookings:
                temm = 1
            else:
                temm = 0  
        except:
            space = 1
            temm = 0
        
        
    amenity = amenity_type.objects.all()
    n = request.session['n']
    a = amenity_type.objects.all()

    return render(request, 'amenity_booking/booking.html', locals())

    


def saveBook(request):
    form = request.POST
    request.session['form'] = form
    user = request.user
    name = request.POST.get('name')
    apt_no = request.POST.get('apt_no')
    partner_name = request.POST.get('partner_name')
    partner_apt_no = request.POST.get('partner_apt_no')
    amenity_name = request.POST.get('amenity')
    date = request.POST.get('date')
    slot = request.POST.get('slot')
    timing = request.POST.get('timing')
    payment = request.POST.get('payment')
    space = request.POST.get('space')
    amount = 0
    payment_status=''

    maintenance_dates=[]
    w = amenity_type.objects.get(name=amenity_name)
    v = amenity_slots.objects.get(slot=slot)
    c = amenity_timings.objects.get(amenity_name=w, timing=timing)
    x = amenity_maintenance.objects.filter(slot=v, time=c)
    y = ''

    for i in x:
        y = str(i.date)
        y = y[-2] + y[-1] + y[-5] + y[-4] + y[2:4]
        maintenance_dates.append(y)
        y = ''

    z = str(date)
    z = z.replace('/','')
    z = z[0:6]


    if(z in maintenance_dates):
        n = "This slot is under maintenance"
        request.session['n'] = n
        return redirect(booking)


    if(int(space)==0):
        n = "You cannot book 0 seats."
        request.session['n'] = n
        return redirect(booking)
    

    if payment=="online":
        n = "Online payment is under construction please select other payment methods."
        request.session['n'] = n
        return redirect(booking)


    sign = signup_table.objects.get(username=user.username)

    if(name.lower()!=sign.first_name.lower()):
        n = "Please enter your first name only"
        request.session['n'] = n
        return redirect(booking)
    if(apt_no!=sign.apt_no):
        n = "Please enter only your registered apartment no"
        request.session['n'] = n
        return redirect(booking)

    if(partner_name!='')and(partner_apt_no!=''):
        try:
            lx = signup_table.objects.get(apt_no=partner_apt_no)
            if(partner_name.lower()!=lx.first_name.lower()):
                n = "Please enter partner's first name only"
                request.session['n'] = n
                return redirect(booking)
        except:
            n = "Partner's apartment no is not registered with our website !"
            request.session['n'] = n
            return redirect(booking)
    elif(partner_name!='')or(partner_apt_no!=''):
        n = "Please fill both partner fields or leave empty !"
        request.session['n'] = n
        return redirect(booking)


    base = amenity_type.objects.get(name=amenity_name)
    amount = 0

    amount = int(amount)
    amount = amount + int(base.base_rate) + int(base.extra_rate_per_person)*int(space)

    if(partner_name=='')or(partner_apt_no==''):
        amount = amount + 100 
    

    if(payment=='cash'):
        payment_status = 'Pending'

    now = booking_table.objects.all()

    lig = filled.objects.filter(amenity_name=amenity_name, amenity_slot=slot,
                                amenity_date=date, amenity_timing=timing)
    lig = lig.values_list('available_space', flat=True)
    newfill2 = amenity_type.objects.get(name=amenity_name)
    newfill2 = newfill2.housing_space
    total = int(newfill2)
    ava = 0
    if (lig is not None):
        ava = total
    else:
        lig = list(lig)
        lig.sort()
        ava = lig[0]

    if(int(space)>ava):
        for z in now:
            if(z.amenity_name==amenity_name)and(z.date==date)and(z.slot==slot)and(z.time==timing):
                n = "This slot is already booked, Check available slots !"
                request.session['n'] = n
                return redirect(booking)

    ist = pytz.timezone('Asia/Kolkata')
    noww = cdatetime.now(ist)
    book_time = noww.strftime('%d/%m/%y, %H:%M:%S')


    booking_id = "J1000"
    t1 = "J1000"
    t2 = []
    if now.exists():
        for j in now:
            t2.append(j.booking_id)
        t1 = t2[-1]
        t1 = t1[1:]
        t1 = int(t1)
        t1 = amenity_name[0:1] + str(t1 + 1)
        booking_id = t1
    else:
        booking_id = "J1000"

    en = booking_table(name=name, apt_no=apt_no, username=user.username, 
                       partner_name=partner_name, partner_apt_no=partner_apt_no,
                       amenity_name=amenity_name, date=date, slot=slot,
                       time=timing, payment_method=payment, booking_id=booking_id,
                       amount=amount, payment_status=payment_status, book_time=book_time, space=int(space))

    
    en.save()

    available = 0
    newfill2 = amenity_type.objects.get(name=amenity_name)
    newfill2 = newfill2.housing_space
    total = int(newfill2)

    fill = filled.objects.filter(amenity_name=amenity_name, amenity_slot=slot,
                                 amenity_date=date, amenity_timing=timing)

    newfill = fill.values_list('available_space', flat=True)
    if(newfill.exists()):
        newfill = list(newfill)
        newfill.sort()
        available = int(newfill[0])
    else:
        available = total


    available = int(available)
    available = int(available) - int(space)

    fn = filled(amenity_name=amenity_name, amenity_slot=slot, booking_id=booking_id,
                amenity_date=date, amenity_timing=timing, available_space=available, total_space=total)

    fn.save()


    current_site = get_current_site(request)
    user = request.user
    email_subject = "New Booking"
    message = render_to_string('amenity_booking/email_booking.html',{
        'name': name,
        'domain': current_site.domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': generate_token.make_token(user),
        'booking_id' : booking_id,
        'amenity_name' : amenity_name,
        'slot' : slot,
        'date' : date,
        'time' : timing

    })
    email = EmailMessage(
        email_subject, message,
        settings.EMAIL_HOST_USER, [user.email],
    )
    email.fail_silently = True
    email.send()


    n = "Here is your booking ! Email Sent"
    request.session['n'] = n
    return redirect(currentbooking)

def cancel(request, variable):

    i = booking_table.objects.filter(booking_id=variable)
    d = booking_table.objects.get(booking_id=variable)
    i.delete()
    g = filled.objects.filter(booking_id=variable)
    g.delete()



    current_site = get_current_site(request)
    user = request.user
    email_subject = "Cancelled Booking"
    message = render_to_string('amenity_booking/email_cancel.html',{
        'name': user.username,
        'domain': current_site.domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': generate_token.make_token(user),
        'booking_id' : variable,
        'amenity_name' : d.amenity_name,
        'slot' : d.slot,
        'date' : d.date,
        'time' : d.time

    })
    email = EmailMessage(
        email_subject, message,
        settings.EMAIL_HOST_USER, [user.email],
    )
    email.fail_silently = True
    email.send()

    return redirect(currentbooking)



def getdata(request):
    user = request.user
    a = amenity_type.objects.values_list('name', flat=True)
    temp = []
    final = []
    temp_str = ''


    for i in a:
        getamenity = amenity_type.objects.get(name=i)
        slot = amenity_slots.objects.filter(amenity_name=getamenity)
        for j in slot:
            temp.append(i)
            temp.append(j.slot)
            temp_str = ', '.join(temp)
            final.append(temp_str)
            temp = []


    val = request.POST.get('amenity')
    if (val is not None):
        val_list = val.split(', ')
        val1 = val_list[0]
        val2 = val_list[1]

        booked = []
        skr = []
        fill = None 
        sog = None 
        tem = ''
        newfill2 = amenity_type.objects.get(name=val1)
        newfill2 = newfill2.housing_space
        total = int(newfill2)

        book = booking_table.objects.filter(amenity_name=val1, slot=val2)

        for i in book:
            booked.append(str(i.date) + str(i.time))
            fill = filled.objects.filter(amenity_name=val1, amenity_slot=val2,
                                        amenity_date=str(i.date), amenity_timing=str(i.time))

            if(fill.exists()):

                sog = fill.values_list('available_space', flat=True)
                sog = list(sog)
                sog.sort()
                tem = str(total-int(sog[0])) + '/' + str(total)
                skr.append(tem)
                tem = ''

        maintenance = []
        te = amenity_slots.objects.get(slot=val2)
        main = amenity_maintenance.objects.filter(slot=te)
        y= ''

        for i in main:
            y = str(i.date)
            y = y[-2] + y[-1] + '/' + y[-5] + y[-4] + '/' + y[2:4]
            date_obj = cdatetime.strptime(y, "%d/%m/%y")
            day_of_date = date_obj.strftime("%A")
            y = y + ', ' + day_of_date
            maintenance.append(str(y) + str(i.time.timing))
            y = ''

        today = cdate.today()
        dates = []
        for i in range(14):

            date = today + timedelta(days=i)
            date_str = date.strftime('%d/%m/%y, %A')
            dates.append(date_str)

        getamenity = amenity_type.objects.get(name=val1)
        timings = amenity_timings.objects.filter(amenity_name=getamenity)
        time = []

        for i in timings:
            time.append(i.timing)


    return render(request, 'amenity_booking/data.html', locals())



def adminbook(request):
    user = request.user
    but = request.POST.get('but')

    if(but=='2'):
        book = booking_table.objects.filter(payment_status="Pending")
    elif(but=='1'):
        book = booking_table.objects.filter(payment_status="Paid")
    else:
        return redirect(getdata)


    return render(request, 'amenity_booking/adminanalytics.html', locals())

def adminbook2(request):
    user = request.user
    dates = booking_table.objects.values_list('date', flat=True).distinct()
    print(dates)
    return render(request, 'amenity_booking/bookingsbydate.html', {'dates': dates})

def bookbydate(request):
    user = request.user
    date = request.POST.get('date')
    book = booking_table.objects.filter(date=date)
    return render(request, 'amenity_booking/adminanalytics.html', locals())








