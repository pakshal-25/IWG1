from django.shortcuts import render,HttpResponseRedirect,redirect
from .form import SignUpForm,ImageForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import Post,Image,Contact
from django.contrib.auth.models import Group
    


# Create your views here.
def home(request):
    return render(request,'blog/home.html')
def about(request):
    return render(request,'blog/about.html')



def contact(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        content =request.POST['content']
        if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<4:
            messages.error(request, "Please fill the form correctly")
        else:
            contact=Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request, "Your message has been successfully sent")
    return render(request,'blog/contact.html',{})

    

def user_signup(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        form=SignUpForm(request.POST)
    if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid(): 
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request,'Account was created for' +user)
            return redirect('login')
            #group=Group.objects.get(name='Author')
            #user.groups.add(group)
    else:

        form=SignUpForm()
    return render(request,'blog/signup.html',{'form':form})

def user_login(request):
	if request.user.is_authenticated:
		return redirect('dashboard')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('dashboard')
			else:
				messages.info(request, 'Username OR Password is Incorrect')

		context = {}
		return render(request, 'blog/login.html', context)



def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')
    
def dashboard (request):
    if request.method=='POST':
        form=ImageForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    form=ImageForm
    img=Image.objects.all()
    return render(request,'blog/Dashboard.html',{'img':img,'form':form})

def upload(request):  
    if request.method=='POST':
        return render(request,'blog/upload.html')
