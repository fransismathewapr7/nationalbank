# views.py
from django.contrib import messages
from django.shortcuts import render


def student_form(request, ):
    return render(request, 'form1.html')


def odercom(request):

    if request.method == 'POST':
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        birthday = request.POST['birthday']
        age = request.POST['age']
        # gender = request.POST['gender']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']
        purpose = request.POST['purpose']

        if firstname == "" or lastname == "" or birthday == "" or age == "" \
                or email == "" or phone == "" or address == '' or purpose == "":
            print("Please fill the fields")
            messages.info(request, 'Please fill all the fields')
            return render(request,'form1.html')
        else:
            return render(request, 'odercom.html')

    return render(request, 'odercom.html')

