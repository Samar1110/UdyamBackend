from django.shortcuts import render ,HttpResponse,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

def handleSignUp(request):
    if request.method=="POST":
        #Get the POST parameters
        username=request.POST['nameOfLoggedInUser']
        emailOfUser=request.POST['emailOfUser']
        firstName=request.POST['firstName']
        lastName=request.POST['lastName']
        pass1=request.POST['passwordOfLoggedInUser']
        pass2=request.POST['confirmpassword']

        # check for errorneous input
        if len(username)> 15 :
            messages.error(request, " Your User Name must not Exceed more than 15 characters")
            return redirect('register')
        if not username.isalnum():
            messages.error(request, " Only letters and digits should be used in user names.")
            return redirect('register')

        if (pass1!= pass2):
             messages.error(request, " Passwords do not match")
             return redirect('register')  

        # Create the user
        myuser = User.objects.create_user(username, emailOfUser, pass1)
        myuser.first_name= firstName
        myuser.last_name= lastName
        myuser.save()
        messages.success(request, " Your AUTH System ID has been successfully created")
        return redirect('login')

    else:
        return HttpResponse("404 - Not found")     

def handlelogin(request):
    if request.method=="POST":
        # Get the post parameters
        nameOfLoggedInUser=request.POST['nameOfLoggedInUser']
        passwordOfLoggedInUser=request.POST['passwordOfLoggedInUser']

        user=authenticate(username= nameOfLoggedInUser, password= passwordOfLoggedInUser)
        if user is not None:
            login(request, user)
            messages.success(request, "Logged In Successfully")
            return redirect("home")
        else:
            messages.error(request, "Please try again Credentials enterd by you is wrong")
            return redirect("login")

    return HttpResponse("404- Not found")


def handlelogout(request):
    logout(request)
    messages.success(request, "Logged out Successfully")
    return redirect('login')    