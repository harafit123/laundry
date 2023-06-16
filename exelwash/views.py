from django.shortcuts import render, redirect
from .models import Enquiry,Profile
from django.contrib.auth.models import User
from django.contrib import messages
import uuid
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    if request.method=="POST":
        if 'enquiry_form' in request.POST:
            name =request.POST.get('name')
            email=request.POST.get('email')
            message=request.POST.get('message')
                
            e = Enquiry.objects.create(name=name, email=email, message=message )
            e.save()
            return redirect('index')
        
        if 'login_form' in request.POST:
            username = request.POST.get('username')
            password = request.POST.get('password')

            user_obj = User.objects.filter(username = username).first()
            if user_obj is None:
                messages.success(request, 'User not found.')
                return redirect('/log_in')
            
            
            profile_obj = Profile.objects.filter(user = user_obj ).first()

            if not profile_obj.is_verified:
                messages.success(request, 'Profile is not verified check your mail.')
                return redirect('/log_in')

            user = authenticate(username = username , password = password)
            if user is None:
                messages.success(request, 'Wrong password.')
                return redirect('/log_in')
            
            login(request,user)
            return redirect('/user')
    return render(request, 'exelwash/index.html', {'title':'Login|Exel wash'})


def washing(request):
    if request.method=="POST":
        name =request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
            
        e = Enquiry.objects.create(name=name, email=email, message=message )
        e.save()
        return redirect('washing')
    
    return render(request, 'exelwash/washing.html', {'title':'Washing |services||exel wash'})

def wash_fold(request):
    if request.method=="POST":
        name =request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
            
        e = Enquiry.objects.create(name=name, email=email, message=message )
        e.save()
        return redirect('wash_fold')
    return render(request, 'exelwash/wash&fold.html', {'title':'Wash & Fold |services||exel wash'})

def dry_cleaning(request):
    if request.method=="POST":
        name =request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
            
        e = Enquiry.objects.create(name=name, email=email, message=message )
        e.save()
        return redirect('dry_cleaning')
    return render(request, 'exelwash/drycleaning.html', {'title':'Dry Cleaning|services||exel wash'})

def shoe_laundry(request):
    if request.method=="POST":
        name =request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
            
        e = Enquiry.objects.create(name=name, email=email, message=message )
        e.save()
        return redirect('shoe_laundry')
    return render(request, 'exelwash/shoelaundry.html', {'title':'Shoe Laundry|services||exel wash'})

def saree_rooling(request):
    if request.method=="POST":
        name =request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
            
        e = Enquiry.objects.create(name=name, email=email, message=message )
        e.save()
        return redirect('saree_rooling')
    return render(request, 'exelwash/sareerolling.html', {'title':'Saree Rolling|services||exel wash'})

def strain_removal(request):
    if request.method=="POST":
        name =request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
            
        e = Enquiry.objects.create(name=name, email=email, message=message )
        e.save()
        return redirect('strain_removal')
    return render(request, 'exelwash/stainremoval.html', {'title':'Stain Removal|services||exel wash'})

def steam_ironing(request):
    if request.method=="POST":
        name =request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
            
        e = Enquiry.objects.create(name=name, email=email, message=message )
        e.save()
        return redirect('steam_ironing')
    return render(request, 'exelwash/steamironing.html', {'title':'Steam Ironing|services||exel wash'})

def carpet(request):
    if request.method=="POST":
        name =request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
            
        e = Enquiry.objects.create(name=name, email=email, message=message )
        e.save()
        return redirect('carpet')
    return render(request, 'exelwash/carpet.html', {'title':'Carpet & Curtains Cleaning |services||exel wash'})

def toys_cleaning(request):
    if request.method=="POST":
        name =request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
            
        e = Enquiry.objects.create(name=name, email=email, message=message )
        e.save()
        return redirect('toys_cleaning')
    return render(request, 'exelwash/softtoyscleaning.html', {'title':'Soft Toys Cleaning |services||exel wash'})


def services(request):
    if request.method=="POST":
        name =request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
            
        e = Enquiry.objects.create(name=name, email=email, message=message )
        e.save()
        return redirect('services')
    return render(request, 'exelwash/services.html', {'title':'Service Page|Exel wash'})





def log_in(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('psw')

        user_obj = User.objects.filter(username = username).first()
        if user_obj is None:
            messages.success(request, 'User not found.')
            return redirect('/log_in')
        
        
        profile_obj = Profile.objects.filter(user = user_obj ).first()

        if not profile_obj.is_verified:
            messages.success(request, 'Profile is not verified check your mail.')
            return redirect('/log_in')

        user = authenticate(username = username , password = password)
        if user is None:
            messages.success(request, 'Wrong password.')
            return redirect('/log_in')
        
        login(request,user)
        return redirect('/user')
    return render(request, 'exelwash/login.html', {'title':'Login|Exel wash'})

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('psw')
        password1 = request.POST.get('psw-repeat')
        print(password)

        try:
            if password and password1 and password != password1:
                messages.success(request, "Passwords do not match.")
                return redirect('/signup')
            
            if User.objects.filter(username = username).first():
                messages.success(request, 'Username is taken.')
                return redirect('/signup')

            if User.objects.filter(email = email).first():
                messages.success(request, 'Email is taken.')
                return redirect('/signup')
            
            
            user_obj = User(username = username,email = email)
            user_obj.set_password(password)
            user_obj.save()
            auth_token = str(uuid.uuid4())
            profile_obj = Profile.objects.create(user = user_obj , auth_token = auth_token)
            profile_obj.save()
            send_mail_after_registration(email , auth_token)
            return redirect('/token')

        except Exception as e:
            print(e)

    return render(request, 'exelwash/signup.html', {'title':'Register|Exel wash'})

def log_out(request):
    logout(request)
    messages.success(request,"Logged Out Successfully")
    return redirect("index")






def success(request):
    return render(request , 'exelwash/allerts/success.html')


def token_send(request):
    return render(request ,'exelwash/allerts/token_send.html')



def verify(request , auth_token):
    try:
        profile_obj = Profile.objects.filter(auth_token = auth_token).first()
    

        if profile_obj:
            if profile_obj.is_verified:
                messages.success(request, 'Your account is already verified.')
                return redirect('/log_in')
            profile_obj.is_verified = True
            profile_obj.save()
            messages.success(request, 'Your account has been verified.')
            return redirect('/log_in')
        else:
            return redirect('/error')
    except Exception as e:
        print(e)
        return redirect('/')

def error_page(request):
    return  render(request , 'exelwash/allerts/error.html')

def send_mail_after_registration(email , token):
    subject = 'Your accounts need to be verified'
    message = f'Hi paste the link to verify your account http://127.0.0.1:8000/verify/{token}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message , email_from ,recipient_list )


@login_required(login_url='/log_in')
def user_int(request):
        return render(request, 'user_interface/ui.html', {'title':'Laundry Shop/Vendor Selection'})

@login_required(login_url='/log_in')
def user_cart(request):      
        return render(request, 'user_interface/addtocart.html')