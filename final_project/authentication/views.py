from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            login(request,form.save())
            return redirect('home')
    else:
        form = UserCreationForm()
    form = UserCreationForm()
    return render(request,"register.html",{"form" : form} )

def login_user(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('home')
    else:
        form = AuthenticationForm()
    form = AuthenticationForm()
    return render(request,"login.html",{"form" : form} )


"""
username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username = username,password = password)
        if user is not none:
            login(request,user)
            return redirect('home')
        else:
            return redirect('login_user')"""