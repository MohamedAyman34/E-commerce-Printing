from django.shortcuts import render , redirect
from .models import Profile , UserAddress , UserPhoneNumbers
from .forms import SignupForm , UserActiveForm
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required

# Create your views here.

def signup(request):

    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            myform = form.save(commit=False)
            myform.active = False
            myform.save()
            profile = Profile.objects.get(user__username=username)
            print(profile)
            print(profile.code)
            send_mail(
                        subject= 'Active your Account',
                        message= f'This code {profile.code} for activate your account',
                        from_email = 'aymanabdelfattahm@gmail.com',
                        recipient_list = [email],
                        fail_silently=False,)
            return redirect(f'/accounts/{username}/activate')

       
    else :
        form = SignupForm()
    return render(request,'registration/signup.html',{'form':form})

def user_activate(request,username):
    profile = Profile.objects.get(user__username = username)
    if request.method == 'POST':
        form = UserActiveForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data['code']
            if profile.code == code :
                profile.code_used = True
                profile.save()
                return redirect('/accounts/login')
    
    else:
        form = UserActiveForm()
    return render(request,"registration/activate.html",{'form':form})
    
    



@login_required
def profile(request):
    profile = Profile.objects.get(user=request.user)
    user_phone = UserPhoneNumbers.objects.filter(user = request.user)
    user_address = UserAddress.objects.filter(user = request.user)

    return render(request,'registration/profile.html',{'profile':profile,'phones':user_phone,'address':user_address})

def edit_profile(request):
    pass
