from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import authenticate
from decimal import Decimal
from django.http import HttpResponse
from sklearn.preprocessing import LabelEncoder
import pickle
import pandas as pd
import numpy as np
from django.http import JsonResponse

# Create your views here.



def index(request): 
    obj=Vehicles.objects.all()
    context={'result':obj} 
    return render(request,'index.html',context)

def about(request):
    return render(request,'about.html')

def service(request):
    return render(request,'services.html')

def packages(request):
    return render(request,'packages.html')

def contact(request):
    return render(request,'contact.html')

def register(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email'] 
        phone=request.POST['phone']     
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        if password==cpassword:   
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username Already Exists")
                return redirect('login') 
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email Already Exists")
                return redirect('login') 
            else:
                user=User.objects.create_user(username=username,email=email,password=password)
                user.save();
                u=customer(username=username,email=email,phone=phone,password=password)
                u.save();
            print("User Created");
            messages.success(request,"successfully registered")
            return redirect('login')
        else:
            messages.info(request,"password not match")
            return redirect('login')
    return render(request, 'login.html')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
    

        if user:
            print(2)
            auth.login(request,user)
            #save email in session
            request.session['username'] = username
            

            return redirect('index')
        else:
            # print(3)
            messages.info(request,"invalid values")
            return redirect('login')
    return render(request,'login.html')

def logout(request):
    if 'username' in request.session:
        request.session.flush()
    return redirect('index')

def change_password(request):
    if request.method == 'POST':
        current_password = request.POST['current_password']
        new_password = request.POST['new_password']
        confirm_password = request.POST['confirm_password']

        user = User.objects.get(email__exact=request.user.email)
        success = user.check_password(current_password)
        if success:
            user.set_password(new_password)
            user.save()
            messages.success(request, 'Password updated successfully.')
            return redirect('login')
        else:
            messages.error(request, 'Password does not match!')
            return redirect('change_password')
    return render(request, 'change/change_password.html')


def testdrive(request):  
    obj={}
    obj=Vehicles.objects.all()
    context={'result':obj}

    # objtime={}
    # objtime=time.objects.all()
    # cont={'res':objtime}

    if request.method=='POST':
        
        username=request.session['username']
        user=customer.objects.filter(username=username)
        
        for i in user:
            id=i.id
            print(id)
        
        venue=request.POST['venue']
        carmodel=request.POST['carmodel']  
        Contact=request.POST['Contact']  
        Email=request.POST['Email']  
        testdate=request.POST['testdate']
        testtime=request.POST['testtime']
        # print(username,user,venue,carmodel,Contact,Email,testdate,testtime)
        # print('userid',id)
        # print(Contact)
        
        test=test_drive(username_id=id,venue=venue,carmodel=carmodel,testdate=testdate,testtime=testtime,Contact=Contact,Email=Email)
        # num=customer(Contact=Contact)
        # num.save()
        test.save()
        messages.success(request, "book appoinment successfully.")
    return render(request,'testdrive.html',context)

def testview(request):
    obj=test_drive.objects.all()
    obje=showroom_visit.objects.all()
    # context={'info':obj}
    return render(request,'testview.html',{'obj':obj,'obje':obje})

def delete(request,id):
    appoimnt_info=test_drive.objects.get(id=id)
    appoimnt_info.delete() 
    return redirect('testview')

def cars(request,id):
    print(id)
    lst=Vehicles.objects.filter(id=id)
    sp=Productgallery.objects.filter(product__id=id)
    context={
        'lst':lst,
        'sp':sp
    }
    return render(request,'cars.html',context)

def book(request,id):
    lst=Vehicles.objects.filter(id=id)
    context={
        'lst':lst,
        
    }
    return render(request,'book.html',context)

def stafflogin(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
    

        if user:
            print(2)
            auth.login(request,user)
            #save email in session
            request.session['username'] = username
            

            return redirect('staffhome')
        else:
            # print(3)
            messages.info(request,"invalid values")
            return redirect('stafflogin')
    return render(request,'stafflogin.html')



def staffregister(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email'] 
        phone=request.POST['phone']     
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        if password==cpassword:   
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username Already Exists")
                return redirect('stafflogin') 
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email Already Exists")
                return redirect('stafflogin') 
            else:
                user=User.objects.create_user(username=username,email=email,password=password)
                user.save();
                u=staff(username=username,email=email,phone=phone,password=password)
                u.save();
            print("User Created");
            messages.success(request,"successfully registered")
            return redirect('stafflogin')
        else:
            messages.info(request,"password not match")
            return redirect('stafflogin')
    return render(request, 'stafflogin.html')

def staffhome(request):
    return render(request,'staffhome.html')

def showroomvisit(request):
    obj={}
    obj=Vehicles.objects.all()
    context={'result':obj}
    if request.method=='POST':
        
        username=request.session['username']
        user=customer.objects.filter(username=username)
        
        for i in user:
            id=i.id
            print(id)
        
        
        carmodel=request.POST['carmodel']  
        Contact=request.POST['Contact']  
        Email=request.POST['Email']  
        visitdate=request.POST['visitdate']
        visittime=request.POST['visittime']
        # print(username,user,venue,carmodel,Contact,Email,testdate,testtime)
        # print('userid',id)
        # print(Contact)
        
        visit=showroom_visit(username_id=id,carmodel=carmodel,visitdate=visitdate,visittime=visittime,Contact=Contact,Email=Email)
        # num=customer(Contact=Contact)
        # num.save()
        visit.save()
        messages.success(request, "book appoinment successfully.")
    return render(request,'visit.html',context)

def visit_delete(request,id):
    visit_info=showroom_visit.objects.get(id=id)
    visit_info.delete() 
    return redirect('testview')

def job(request):
    return render(request,'job.html')

def appoinmentview(request):
    return render(request,'appoinmentview.html')



def car_loan_emi(request):
    banks = Bank.objects.all()
    if request.method == 'POST':
        bank_id = request.POST.get('bank')
        loan_amount = float(request.POST.get('loan_amount'))
        loan_tenure = int(request.POST.get('loan_tenure'))
        bank = Bank.objects.get(id=bank_id)
        interest_rate = bank.interest_rate
        emi_amount = calculate_emi(loan_amount, loan_tenure, interest_rate)
        car_loan = CarLoan.objects.create(bank=bank, loan_amount=loan_amount, loan_tenure=loan_tenure, interest_rate=interest_rate, emi_amount=emi_amount)
<<<<<<< HEAD
        return render(request, 'emi.html', {'banks': banks, 'emi_amount': emi_amount})
=======
        return render(request, 'car_loan_emi.html', {'banks': banks, 'emi_amount': emi_amount})
>>>>>>> dbe8adc81f270ff8faf1403c5d073de8decd1232
    else:
        return render(request, 'car_loan_emi.html', {'banks': banks})

def calculate_emi(loan_amount, loan_tenure, interest_rate):
    r = interest_rate / (12 * 100)
    n = loan_tenure * 12
    emi = loan_amount * r * ((1 + r) ** n) / (((1 + r) ** n) - 1)
    return round(emi, 2)

<<<<<<< HEAD
# USED CAR PRICE PREDICTION
=======














>>>>>>> dbe8adc81f270ff8faf1403c5d073de8decd1232

def predict(request):
    return render(request, 'predict.html')

def predict_price(request):
    # Load the saved linear regression model
    model = pickle.load(open('LinearRegressionModel.pkl', 'rb'))

    # Load the cleaned car data
    car = pd.read_csv('Cleaned_Car_data.csv')

<<<<<<< HEAD
    # Get unique values of company and name columns
    companies = car['company'].unique()
    names = car['name'].unique()

=======
>>>>>>> dbe8adc81f270ff8faf1403c5d073de8decd1232
    # Get the form data
    if request.method=='POST':
        company = request.POST['company']
        car_model = request.POST['name']
        year = int(request.POST['year'])
        fuel_type = request.POST['fuel_type']
        kms_driven = int(request.POST['kms_driven'])
        

    # Make a prediction using the model
<<<<<<< HEAD
        prediction = model.predict(pd.DataFrame(columns=['name', 'company', 'year', 'kms_driven', 'fuel_type'],
                              data=[[car_model, company, year, kms_driven, fuel_type]]))
    
     # Pass the context variables to the HTML template
        context = {
        'companies': companies,
        'names': names,
        'prediction': round(prediction[0], 2)
    }

    # Return the prediction as a JSON response
        return render(request, 'result.html', context)

    
=======
    prediction = model.predict(pd.DataFrame(columns=['name', 'company', 'year', 'kms_driven', 'fuel_type'],
                              data=[[car_model, company, year, kms_driven, fuel_type]]))
    
    # Return the prediction as a JSON response
    return JsonResponse({'predicted_price': round(prediction[0], 2)})
>>>>>>> dbe8adc81f270ff8faf1403c5d073de8decd1232





# def signup(request):
#     if request.method == 'POST':
#         role=request.POST['role']
#         email=request.POST['email']
#         username = email.split('@')[0]
#         phonenumber=request.POST['phonenumber']
#         address=request.POST['address']
#         city=request.POST['city']
#         pincode=request.POST['pincode']
        
#         password = request.POST['password']
#         cpassword = request.POST['cpassword']
#         print('one')
#         is_customer= is_staff = False
#         if role=='is_customer':
#             is_customer=True
        
#         else:
#             is_staff=True
         
#         if password==cpassword:
        
#             if Account.objects.filter(email=email).exists():

#                 messages.info(request,'email already taken')
#                 return redirect('login')
#             else:
#                 user=Account.objects.create_user(username=username,phonenumber=phonenumber,email=email,address=address,city=city,pincode=pincode,district=district,password=password,is_child=is_child,is_ashaworker=is_ashaworker,is_hospital=is_hospital,is_PHC=is_PHC)
#                 user.save()
#                 messages.success(request, 'Thank you for registering with us. Please Login')
#                 return redirect('login')
#         else:
#               print("password is not matching")
#     else:   
#               # return redirect('index.html')
#      return render(request,'register.html')
