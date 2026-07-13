from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate

# models

# forms
from .forms import RegisterForm, LoginForm




# Create your views here.

def registerpage(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        # print(request.POST.get('username')) debugging

        if form.is_valid():

            user = form.save() # returns model instance (in this case model is user)

            # print(user.username, user.email) debugging
            login(request, user)

            return redirect('books')
        
    context = {'form': form}
    
    return render(request, 'ManageUsers/register.html', context)
        
def loginpage(request):
    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(request, username= username, password= password)
            if user:
                login(request, user)
                return redirect('books')
            else:
                form.add_error(None, 'Invalid Username or Password')
            

    context = {'form': form}
    return render(request, 'ManageUsers/login.html', context)

def logoutpage(request):
    logout(request)
    return redirect('login')
