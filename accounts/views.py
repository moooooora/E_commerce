from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .forms import SignupForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        
        if form.is_valid():
            
            form.save()
            
            return redirect('home')
    else:    
        form = SignupForm()
    
    return render(request,'accounts/register.html',{'form':form})

def login(request):
    return render(request,'accounts/login.html')

def logout(request):

    pass



