from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .forms import SignupForm,UserForm,ProfileForm
from .models import Profile

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        
        if form.is_valid():
            
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request,user)
            return redirect('accounts:profile')
    else:    
        form = SignupForm()
    
    return render(request,'accounts/register.html',{'form':form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        if username and password:
            user = authenticate(username=username,password=password)
            login(request,user)
            return redirect('home')
        else:
            pass
    return render(request,'accounts/login.html')

def logout_view(request):

    logout(request)
    return redirect('accounts:login')


def profile(request):
    profile = Profile.objects.get(user = request.user)
    if request.method =='POST':
        userform = UserForm(request.POST,request.FILES,instance=request.user)
        profileform = ProfileForm(request.POST,request.FILES,instance=profile) 
        if userform.is_valid() and profileform.is_valid():
            userform.save()
            profileform.user=request.user
            profileform.save()
            return redirect('accounts:profile')
    else:    
        userform = UserForm(instance=request.user)
        profileform = ProfileForm(instance=profile)

    context = {
        'userform':userform,
        'profileform':profileform,
        'profile':profile,
    }
    return render(request,'accounts/profile.html',context)

def forgetpassword(request):
    if request.method == 'POST':
        email = request.POST['email']
        user = User.objects.filter(email=email).exists()
        if user:
            return redirect('accounts:reset_password')

    return render(request,'accounts/check_email.html')
def reset_password(request):
    if request.method=='POST':
        password = request.POST['password1']
        confirmpassword = request.POST['password2']
        if password == confirmpassword:
            email = request.POST['email']
            user = User.objects.get(email=email)
            user.set_password(password)
            user.save()
            return redirect('accounts:login')

    return render(request,'accounts/reset_password.html')
