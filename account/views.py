from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.contrib.auth.models import User

def login_view(request):
    if request.user.is_authenticated:
        return redirect("home")
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            return render(request, "account/login.html", {
                "error": "username ya da parola yanlış"
            })
        
    return render(request, "account/login.html")

def register_request(request):
    if request.user.is_authenticated:
        return redirect("home")
    
    if request.method == "POST":
        username = request.POST.get("username")
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        email = request.POST.get("email")
        password = request.POST.get("password")
        repassword = request.POST.get("repassword")
        
        if password == repassword:
            if User.objects.filter(username=username).exists():
                return JsonResponse({
                    "error": "Bu kullanıcı adı zaten alınmış.",
                    "username": username,
                    "firstname": firstname,
                    "lastname": lastname,
                    "email": email,
                }, status=400)
            elif User.objects.filter(email=email).exists():
                return JsonResponse({
                    "error": "Bu e-posta adresi zaten kullanılıyor.",
                    "username": username,
                    "firstname": firstname,
                    "lastname": lastname,
                    "email": email,
                }, status=400)
            else:
                user = User.objects.create_user(username=username, first_name=firstname, last_name=lastname, email=email, password=password)
                user.save()
                return JsonResponse({"success": True}, status=201)
        else:
            return JsonResponse({
                "error": "Parolalar eşleşmiyor.",
                "username": username,
                "firstname": firstname,
                "lastname": lastname,
                "email": email,
            }, status=400)
        
    return render(request, "account/register.html")

def logout_request(request):
    logout(request)
    return redirect("home")
