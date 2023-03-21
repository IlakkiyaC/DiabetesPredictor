from django.shortcuts import render, redirect
from .models import USER
import hashlib

# Create your views here.
def register(request):
    print(request.method)
    print(request.user)
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        print(username,password)
        users = USER.objects.filter(username=username)
        if len(users) >0 :
            # messages.error(request, "User already exists")
            render(request=request, template_name="register.html")
        user = USER(username=username,password=hashlib.sha256(password.encode()).hexdigest())
        user.save()

        return redirect("/predict")
    else:
        return render(request, "register.html")

def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        users = USER.objects.filter(username=username)
        if ((len(users) <= 0) or users[0].password != hashlib.sha256(password.encode()).hexdigest()):
            # messages.error(request, "Wrong Credentials!")
            return render(request=request, template_name="login.html")
        return redirect("/predict")
    return render(request=request, template_name="login.html")