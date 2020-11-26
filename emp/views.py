from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse,HttpResponseRedirect
import os
from django.contrib import messages
from emp.models import *
from django.core.files.storage import FileSystemStorage
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# # Create your views here.
# def fn_index(request):
    
#     try:
#         return render(request,'index.html')
#     except Exception as e:
#         print(e)
#         return HttpResponse(e)

def fn_login(request):
    try:
        if request.method =="POST":
        
            email=request.POST['username']
            password=request.POST['password']
            check_exist=Login.objects.filter(email=email).exists()
            if check_exist == False:
                messages.success(request, 'User not Exist')
                return HttpResponseRedirect('/login')
            login_obj = Login.objects.filter(email=email).values('pk','email','password','role')
            request.session['user_id'] = login_obj[0]['pk']
           
            if login_obj[0]['password'] == password:
                # return render(request,'dashboard.html',{'users':login_obj,})
                return HttpResponseRedirect('/load_dashboard')
            messages.success(request, 'Wrong password')
        
        return render(request,'login.html')
    except Exception as e:
        print(e)
        return HttpResponse(e)

# LOAD EMPLOYEES IN VIEW PAGE
def load_addemployee(request):
    
    try:
        users=Login.objects.get(id=request.session['user_id'])
        if request.method =="POST":
            
            name=request.POST['name']
            print(name)
            email=request.POST['email']
            # birth_date=request.POST['birth_date']
            phone=request.POST['phone']
            profile=request.POST['profile']
            address=request.POST['address']
            state=request.POST['state']
            city=request.POST['city']
            pincode=request.POST['pincode']
            password=request.POST['password']
            c_password=request.POST['c_password']
            gender=request.POST.get('gender')
            print(gender)
            image = request.FILES['propic']
         
            print(image)
            if Login.objects.filter(email=email).values('email').count()== 0:
                Login.objects.create(email=email,password=password,role='employee')
                user_pk=Login.objects.get(email=email)
                
            else:
                user_pk=Login.objects.get(email=email)

            Employee.objects.create(name=name,email=email,phone=phone,Address=address,state=state,
            city=city,pincode=pincode,password=password,gender=gender,emp_image=image,profile=profile,log_fk=user_pk)
            

        return render(request,'add_emp.html',{'users':users})
    except Exception as e:
        print(e)
        return HttpResponse(e)

#VIEW EMPLOYEE  FUNCTION
def view_employee(request):
    
    try:
        user = Login.objects.get(id=request.session['user_id'])
        login_user=Login.objects.filter(pk=request.session['user_id']).values('role')
        if login_user[0]['role'] =='admin':
            emp=Employee.objects.all()
        else:
            emp=Employee.objects.filter(log_fk=request.session['user_id'])
        return render(request,'view_emp.html',{'emp':emp,'users':user})
    except Exception as e:
        print(e)
        return HttpResponse(e)

# TO LOAD DASHBOARD
def load_dashboard(request):
    
    try:
        users=Login.objects.get(id=request.session['user_id'])
        print(users.role)
        emp=Employee.objects.all()
        return render(request,'dashboard.html',{'emp':emp,'users':users})
    except Exception as e:
        print(e)
        return HttpResponse(e)

# lOGOUT FUNCTION
def Logout(request):
    try:
        if request.session.has_key('user_id'):
            request.session.flush()
            return HttpResponseRedirect('/login')
        else:
            return HttpResponseRedirect('/login')
    except Exception as e:
        return HttpResponse(e)

# cHART DATA FETCH
def Chartdata_fetch(request):
    
    try:
        if request.method == "POST":
            men_rate=Employee.objects.filter(gender='male').count()
            print(men_rate)
            women_rate=Employee.objects.filter(gender='female').count()
            return JsonResponse({'men_rate':men_rate,'women_rate':women_rate})
    except Exception as e:
        print(e)
        return HttpResponse(e)

# UPDATE EMPLOYEE
def update_employee(request):
    
    try:
        if request.method == "POST":
            user_id=request.POST['user_id']
            name=request.POST['name']
            email=request.POST['email']
            phone=request.POST['phone']
            profile=request.POST['profile']
            address=request.POST['address']
            state=request.POST['state']
            city=request.POST['city']
            pincode=request.POST['pincode']
            print(name)
            print(pincode)
            Employee.objects.filter(pk=user_id).update(name=name,email=email,phone=phone,profile=profile,
            Address=address,state=state,city=city,pincode=pincode)
            return JsonResponse({'data':'updated'})
    except Exception as e:
        print(e)
        return HttpResponse(e)
# TO UPDATE PROFILEPIC
def data_image_upload(request):
    
    try:
        if request.method == "POST":
            
            user_id=request.POST['user_id']
            uploaded_file = request.FILES['propic']
            fs = FileSystemStorage()
            pic = fs.save(uploaded_file.name, uploaded_file)
            # pic_name = 'media/' + pic
            pic_name = pic
            Employee.objects.filter(pk=user_id).update(emp_image=pic_name)
            return JsonResponse({'data':'success'})
    except Exception as e:
        print(e)
        return HttpResponse(e)

# DELETE EMPLOYEE
def Delete_data(request):
    try:
        if request.method == "POST":
            row_id= request.POST['div_id']
            Employee.objects.filter(pk=row_id).delete() 
        return JsonResponse({'data':'deleted'})
    
    except Exception as e:
        print(e)