from django.shortcuts import render,HttpResponse,redirect
from home.models import Contact
from Blog.models import Post
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

# Create your views here.

# html pages
def home(request):
    allposts=Post.objects.all()
    context={'allposts':allposts}
    return render(request,'home/home.html',context)


def contact(request):
    if request.method=='POST':
        name=request.POST['name']       
        email=request.POST['email']       
        phone=request.POST['phone']       
        desc=request.POST['desc']  
        if len(name)<2 or len(email)<3 or len(phone)<10 or len(desc)<4:
            messages.error(request,"Please Fill the Form Correctly")   
        else:
            contact=Contact(name=name,email=email,phone=phone,content=desc)
            contact.save()
            messages.success(request,"Your Message has been sent")

    return render(request,'home/contact.html')


def about(request):
    return render(request,'home/about.html')


def search(request):
    query=request.GET['query']
    if len(query) > 78:
        allposts=Post.objects.none()

    else:
        allpoststitle=Post.objects.filter(title__icontains=query)
        allpostscontent=Post.objects.filter(content__icontains=query)
        allposts=allpoststitle.union(allpostscontent)
    if allposts.count()==0:
        messages.warning(request,"Please Search Correctly")     
    params={'allposts':allposts,'query':query}
    return render(request,"home/search.html",params)   

# Authentication APIs    

def handleSignup(request):
    if request.method == 'POST':
        username=request.POST['username']
        email=request.POST['email']
        fname=request.POST['fname']
        lname=request.POST['lname']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        # check for errorneous inputs
        if len(username)>10:
            messages.error(request,"Username must be under 10 characters ")
            return redirect('home')
        elif not  username.isalnum():
            messages.error(request,"Username must be alphanumeric  ")
            return redirect('home')
        elif pass1!=pass2 :
            messages.error(request,"Password does not match ")
            return redirect('home')

        else:
        # create the user 
           
            myuser=User.objects.create_user(username=username,email=email,password=pass1)
            myuser.first_name=fname
            myuser.last_name=lname
            myuser.save()
            messages.success(request,"Your Account has been Succesfully Created")
            return redirect('home')
       
    else:
        return HttpResponse('404- Not Found')   


def handleLogin(request):
    if request.method == 'POST':
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpass']

        user=authenticate(username=loginusername,password=loginpassword)
        if user is not None :
            login(request,user)
            messages.success(request,f"Successfully Logged In , Welcome {user.first_name}")
            return redirect('home')
        else:
            messages.error(request,"Invalid Credentials , Please try again")
            return redirect('home')    

    return HttpResponse("404 Not Found")


def handleLogout(request):
    
    logout(request)
    messages.success(request,"Successfully Logged Out ")
    return redirect('home')

    
    