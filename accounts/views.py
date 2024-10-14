from tkinter import NO, YES
from django.shortcuts import render,redirect
from django.contrib import messages
from .models import MyUser
from django.contrib.auth import login,logout
from django.contrib.auth.hashers import check_password
from django.shortcuts import get_object_or_404


def register_view(request):
    if not request.user.is_authenticated:

        if request.method == 'POST':

            email= request.POST['email' ]
            global password 
            password= request.POST['psw' ]
            global password2 
            password2= request.POST['psw-repeat']
            global passwordtxt
            passwordtxt = request.POST['psw' ]
            
            pp = request.POST.get('pp')
                
            sp = request.POST.get('sp')          
            if password == password2:
                if MyUser.objects.filter(username=email).exists():
                    messages.info(request,'ایمیل قبلا استفاده شده')
                    return redirect('home:home_view') 
                    
                elif pp == None and sp == None :
                    messages.info(request,'لطفا یکی از گزینه ها را انتخاب کنید')
                elif password == None or password2 == None :
                    messages.info(request,'پسورد ها خالی هستند')
                else:
                    User = MyUser.objects.create_user(username=email,email=email,password=password,personal_P=pp,startup_P=sp,passwordtxt=passwordtxt)
                    return redirect('home:home_view') 

                
            else:
                messages.info(request,'پسورد ها یکی نیستند')
                return redirect('home:home_view') 
            
            
        return redirect('home:home_view')
    
def login_view(request):
    if not request.user.is_authenticated:


        if request.method == 'POST':

            username = request.POST.get('username' , None)

            password = request.POST.get('password' , None)

            if username == '' or username == None :

                messages.error(request , 'نام کاربری خالی است')

                return redirect('home:home_view')

            if password == '' or password == None :

                messages.error(request , 'رمز خود را وارد کنید')

                return redirect('home:home_view')

            try:

                user = MyUser.objects.get(username = username)

                matchcheck = check_password(password , user.password)

                if matchcheck:

                    login(request , user)

                    return redirect('accounts:dashboard_view')
                else:
                    messages.error('نام کاربری یا پسورد اشتباه است')
                    return redirect('home:home_view')
            except:

                messages.error(request , 'کاربری یافت نشد')

                return redirect('home:home_view')


def dashboard_view(request):
    user = request.user  
    all_users = MyUser.objects.exclude(id=user.id)  # Exclude the logged-in user from the list important ******
    context = {'logged_in_user': user, 'all_users': all_users}
    if request.user.personal_P==True:
        
        return render(request,'home/index-after.html',context)
    
    elif request.user.startup_P==True:
        return render(request,'home/index-after-startap.html',context)

def logout_view(request):

    logout(request)
    return redirect('home:home_view')

def edit_profile(request):
    current_user = request.user


    
    if request.user.personal_P==True:


        if request.method == 'POST':
            phone_number= request.POST['phone_number']
            username= request.POST['username' ] 
            age= request.POST['age' ]
            skill= request.POST['skill' ]
            money= request.POST['money' ]
            address= request.POST['address' ]
            password= request.POST['password']
            code_meli= request.POST['code_meli' ]
            description= request.POST['description' ]
            
            #if MyUser.objects.filter(username=username).exists():

                        #messages.info(request,'نام کاربری قبلا استفاده شده') 
                        #return redirect('accounts:edit_profile')
            #else:
            User = MyUser.objects.get(id=request.user.id)
            current_user = request.user

            User.username = username
            User.phone_number = phone_number
            User.age = age
            User.skill = skill
            User.money = money
            User.address = address
            User.code_meli = code_meli
            User.description = description
            if password !=None and password !='':
                User.set_password(password) 
                User.save(update_fields=['username', 'password'])
            User.save()


            User.save(update_fields=['username'])
            return redirect('home:home_view')


        return render(request,'home/پروفایل شخصی.html')

    elif request.user.startup_P==True:
        
        if request.method == 'POST':
            phone_number= request.POST['phone_number']
            username= request.POST['username'] 
            company_history= request.POST['company_history' ]
            skill= request.POST['skill' ]
            money= request.POST['money' ]
            address= request.POST['address' ]
            password= request.POST['password']
            password2= request.POST['password2']

            #if MyUser.objects.filter(username=username).exists():

                        #messages.info(request,'نام کاربری قبلا استفاده شده') 
                        #return redirect('accounts:edit_profile')
            #else:
            User = MyUser.objects.get(id=request.user.id)
            current_user = request.user

            User.username = username
            User.phone_number = phone_number
            User.company_history = company_history
            User.skill = skill
            User.money = money
            User.address = address

            if password !=None and password !='':
                if password == password2:
                    User.set_password(password) 
                    User.save(update_fields=['username', 'password'])
                else:
                    messages.info(request,'پسورد ها یکی نیستند')
                    return redirect(request,'accounts:edit_profile')
            User.save()


            User.save(update_fields=['username'])
            return redirect('home:home_view')
        user = MyUser.objects.all()

        if request.user.is_superuser:
            return render(request,'home/پروفایل استارتاپی-مدیریت.html',{'user': user})
        else:
            return render(request,'home/پروفایل استارتاپی.html')
def search(request):
     user=MyUser.objects.all()
     if request.method == 'POST':
        
        usearch = request.POST.get('usearch')
        if usearch:
            user = MyUser.objects.filter(username__contains=usearch)
            return render(request,'home/پروفایل استارتاپی-مدیریت.html',{'user': user})
        else:
            user=MyUser.objects.all()
            return render(request,'home/پروفایل استارتاپی-مدیریت.html',{'user': user})


     return render(request,'home/پروفایل استارتاپی-مدیریت.html',{'user': user})


def edit(request,id):
    current_user = request.user
    user = MyUser.objects.all()
    userid = get_object_or_404(MyUser, pk=id)
    if request.method == 'POST':
            print(request.POST)
            phone_number= request.POST['phone_number']
            username= request.POST['username']
            skill= request.POST['skill' ]
            password= request.POST['password']
            passwordtxt= request.POST['password']
            code_meli= request.POST['code_meli']
            description=request.POST['description']
            can_edit = request.POST.get('can_edit')
            p_access = request.POST.get('p_access')
            #1 HA CHECK BOX haye paini ast
            see_users = request.POST.get('see_users')
            can_edit = request.POST.get('can_edit1')
            see_users = request.POST.get('see_users1')
            p_access = request.POST.get('p_access1')
            userid = MyUser.objects.get(pk=id)
            userid.username = username
            userid.phone_number = phone_number
            userid.code_meli = code_meli
            userid.skill = skill
            userid.description = description
          
            

            
    # DONT TOUCH THIS PART! STUDY BUT DONT TOUCH IT (i mean it!)
            if can_edit:
    # If it's present, set it to True
                userid.can_edit = True
            else:
    # If it's not present, or it's None, set it to False
                userid.can_edit = False
            if p_access:
                userid.p_access = True
            else:
                userid.p_access = False
            if see_users:
                userid.p_access = True
                userid.is_superuser = True
                
            else:
                userid.p_access = False
                userid.is_superuser = False
                
                

            

            if password !=None and password !='':
                    userid.set_password(password) 
                    userid.passwordtxt = passwordtxt
                    userid.save(update_fields=['username', 'password',])

            userid.save()
            userid.save(update_fields=['username'])

            
            
    return render(request,'home/پروفایل استارتاپی-مدیریت.html',{'user': user, 'userid':userid,'current_user':current_user})

        


                


            

        