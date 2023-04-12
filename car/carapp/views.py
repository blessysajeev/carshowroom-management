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
import razorpay
from django.conf import settings

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

def book(request,id=None):
    lst=Vehicles.objects.get(id=id)
    print(lst)
    # context={
    #     'lst':lst,     
    # }
    
        # Get the down payment amount entered by the user
    down_payment = int(lst.exshowroomprice)*(10/100)*100
    print(lst.exshowroomprice)

        #  create a Razorpay client and generate a payment order
    client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
    order = client.order.create({
            'amount': down_payment,
            'currency': 'INR',
            # 'payment_capture': '1'
    })
        # print(order)
    order_id = order['id']

    order_status = order['status']
    if order_status == 'created':
        payment = Payments(
            # user = customer.objects.get(id=request.user.id),
            amount = down_payment,
            razorpay_order_id=order_id,
            razorpay_payment_status=order_status,
        )
        payment.save()

        context = {
                'order_id': order_id,
                'amount': down_payment,
                'currency': 'INR',
                'lst':lst
            }
        print(context)


    return render(request, 'book.html', context)
    
def paydone(request):
    return render(request,'pymentdone.html')


# # Check if the down payment amount is valid (i.e., greater than or equal to 20000)
        # if down_payment < 20000:
        #     context['error'] = "Minimum down payment amount is 20000"
        # else:
        #     # TODO: Process payment using a payment gateway, such as Razorpay
        #     context['success'] = True


# def booking(request):
#     if request.method == 'POST':
#         # get the amount from the form
#         down_payment = request.POST.get('down_payment')
#         print(down_payment)
#         amount_in_paise = max(int(down_payment) * 100, 100) # convert down payment to paise and ensure minimum value of 100 paise

#         # create a Razorpay client and generate a payment order
#         client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
#         order = client.order.create({
#             'amount': amount_in_paise,
#             'currency': 'INR',
#             'payment_capture': '1'
#         })

#         # render the payment form with the order details
#         return render(request, 'book.html', {'order_id': order['id'], 'amount': amount_in_paise})

#     else:
#         # render the initial form with the list of products
#         lst = [{'name': 'Product1', 'exshowroomprice': '100000'}, {'name': 'Product2', 'exshowroomprice': '200000'}, {'name': 'Product3', 'exshowroomprice': '300000'}]
#         return render(request, 'book.html', {'lst': lst})


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
        return render(request, 'emi.html', {'banks': banks, 'emi_amount': emi_amount})
    else:
        return render(request, 'car_loan_emi.html', {'banks': banks})

def calculate_emi(loan_amount, loan_tenure, interest_rate):
    r = interest_rate / (12 * 100)
    n = loan_tenure * 12
    emi = loan_amount * r * ((1 + r) ** n) / (((1 + r)  ** n) - 1)
    return round(emi, 2)

# USED CAR PRICE PREDICTION

def predict(request):
    return render(request, 'predict.html')

def predict_price(request):
    # Load the saved linear regression model
    model = pickle.load(open('LinearRegressionModel.pkl', 'rb'))

    # Load the cleaned car data
    car = pd.read_csv('Cleaned_Car_data.csv')

    # Get unique values of company and name columns
    companies = car['company'].unique()
    names = car['name'].unique()
    fuel_type = car['fuel_type'].unique()

    
    # Get the form data
    if request.method=='POST':
        company = request.POST['company']
        car_model = request.POST['name']
        year = int(request.POST['year'])
        fuel_type = request.POST['fuel_type']
        kms_driven = int(request.POST['kms_driven'])
        

    # Make a prediction using the model
        prediction = model.predict(pd.DataFrame(columns=['name', 'company', 'year', 'kms_driven', 'fuel_type'],
                              data=[[car_model, company, year, kms_driven, fuel_type]]))
    
     # Pass the context variables to the HTML template
        context = {
        'companies': companies,
        'names': names,
        'fuel_type' : fuel_type,
        'prediction': round(prediction[0], 2)
    }

    # Return the prediction as a JSON response
        return render(request, 'result.html', context)

    





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
