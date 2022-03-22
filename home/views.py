from asyncio import constants
from asyncio.windows_events import NULL
from email import message
from django.forms import PasswordInput
from django.shortcuts import render
from django.shortcuts import redirect
from home.models import Contact
from home.models import Content
from blog.models import Blog
from home. models import Signup


from django.contrib import messages
from django.contrib.auth.models import User



# Create your views here.

# home_section

def index(request):
    content=Content.objects.all()
    param={'content':content}
    return render(request,'home/index.html',param)


# about_section
def about(request):
    return render(request,'home/about.html')


# contact_section
def contact(request):
    if request.method=='POST':
        details=Contact.objects.all()
        name=request.POST['name']
        email=request.POST['email']
        number=request.POST['number']
        message=request.POST['message']
        check_error=""
        if name :
            if(len(name))<3 :
                messages.add_message(request,messages.ERROR,'name numst be 3 digit long or more !!')
                check_error=True
        if not name:
            messages.add_message(request,messages.ERROR,'Name required !!')
            check_error=True
        if number:
            if (len(number))<10:
                messages.add_message(request,messages.ERROR,'Number must be 10 digit long')
                check_error=True
        if not number:   
            messages.add_message(request,messages.ERROR,'Number reqiured !!')
            check_error=True
        if not email:
            messages.add_message(request,messages.ERROR,'Email is required !!')
            check_error=True
        if message:
            if (len(message))<6:
                messages.add_message(request,messages.ERROR,'Please describe properly !!!')
                check_error=True
            
        if check_error!=True:
            contact=Contact(
            name=name,
            email=email,
            phone_number=number,
            message=message,
            )
            contact.save()
            if contact.save:
                messages.add_message(request,messages.SUCCESS,'Thanks for contacting us.')
            return redirect('contactpage')
    else:
        return render(request,'home/contact.html')

    return render(request,'home/contact.html')

#search_section
def search(request):
    if request.method=='GET':
        query=request.GET['query']
        if(len(query))>100:
            messages.add_message(request,messages.INFO,f'your search {query} did not match any document, its too long ....')
        if query:
            blogTitle=Blog.objects.filter(title__icontains=query)
            blogContent=Blog.objects.filter(text__icontains=query)
            result=blogTitle.union(blogContent)
        if not query:
            messages.add_message(request,messages.INFO,'Opps!! result  not found please type something else for better response .....')  
        if query=="":
            return redirect('homePage')
        param={'query':result}
    return render(request,'home/search.html',param)  

# signup_section  
def sign_up(request):
    if request.method=='POST':
        print(request.POST['username'])
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST["password"]
        repassword=request.POST['re_password']

        register_cutomer=Signup(username=username,
                                email=email,
                                password=password,
                                re_password=repassword)
        register_cutomer.save()      
    return redirect('homePage')
   
#sign_up_section
def sigin_in(request):
    if request.method=='POST':
        user=request.POST['checkuser']
        password=request.POST['checkpass']
        flag=0

        # username
        try:
            checkuser=Signup.getuser_by_email(user)
            flag=1
        except Exception as a:
            flag=0
        # password
        try:
            checkpassword=Signup.getuser_by_password(password)
            flag=1
        except Exception as a:
            flag=0
        
        # controller
        if flag==1:
            messages.add_message(request,messages.SUCCESS,f'Hellow  {user} welcome to blogger')
            return redirect('homePage')
        elif flag==0:
            messages.add_message(request,messages.ERROR,'username or password does not matched..')

    return render(request,'home/index.html')


