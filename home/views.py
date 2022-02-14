from django.shortcuts import render
from django.shortcuts import redirect
from home.models import Contact
from home.models import Content

from django.contrib import messages

# Create your views here.


def index(request):
    content=Content.objects.all()
    param={'content':content}
    return render(request,'home/index.html',param)



def about(request):
    return render(request,'home/about.html')


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
            
        # values={
        #     'name':name,'email':email,'number':number, 'message':message   
        # }
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
    
    
    