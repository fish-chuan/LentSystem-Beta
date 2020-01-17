from django.shortcuts import render, redirect
from django.contrib import messages
from main.models import Item
from django.contrib.auth.models import User, auth
# Create your views here.

def register(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, '帳號已存在')
            elif User.objects.filter(email=email).exists():
                messages.info(request, '電子郵件已存在')
            else:
                user = User.objects.create_user(username=username, first_name=first_name, email=email, password=password1)
                user.save()
                print('User created')
                return redirect('login')
        else:
            print('密碼不符！')
        return redirect('/')

    else:
        return render(request, 'register.html')

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            data = Item.objects.all()
            return render(request, 'index.html', {'Item':data})
        else:
            messages.info(request, 'invalid')
            return redirect('login')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect("/")