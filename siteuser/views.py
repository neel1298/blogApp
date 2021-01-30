from django.shortcuts import render,redirect,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages,auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import UserProfile
# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        user = User.objects.create_user(username=username,password=password,email=email)
        user.save()
        return redirect('blog-home')
    else:    
        "form = UserCreationForm()"
        return render(request,'siteuser/register.html')    
"""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Account created for {username}')
"""   


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        auth.login(request,user)
        if user is not None:
            return redirect('blog-home')

        else:
            return render(request,'siteuser/login.html')    
    else:

        return render(request,'siteuser/login.html')   
        

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('blog-home')


@login_required
def profile(request):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        new_username = request.POST['username']
        new_email = request.POST['email']
        imageurl = request.FILES.get('profile_pic')
        new_User= User.objects.get(pk= user_id)
        new_User.username = new_username
        new_User.email = new_email

        new_User.save()
        if imageurl is not None:
            new_image=UserProfile.objects.get(user_id=user_id)
            new_image.delete()
            new_image.user_id = user_id
            new_image.image = 'user_profile_pics/%s/%s'%(user_id,imageurl)
            new_image.save()
        return HttpResponseRedirect(request.path_info)

    return render(request,'siteuser/profile.html')