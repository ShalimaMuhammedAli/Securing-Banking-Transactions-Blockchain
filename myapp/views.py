from django.shortcuts import render

# Create your views here.
from django.db.models import Max
from .models import user_login

def index(request):
    return render(request, './myapp/index.html')


def about(request):
    return render(request, './myapp/about.html')


def contact(request):
    return render(request, './myapp/contact.html')

#######################################################################
#################### ADMIN ###############################
def admin_login(request):
    if request.method == 'POST':
        un = request.POST.get('un')
        pwd = request.POST.get('pwd')
        #print(un,pwd)
        #query to select a record based on a condition
        ul = user_login.objects.filter(uname=un, passwd=pwd, u_type='admin')

        if len(ul) == 1:
            request.session['user_name'] = ul[0].uname
            request.session['user_id'] = ul[0].id
            return render(request,'./myapp/admin_home.html')
        else:
            msg = '<h1> Invalid Uname or Password !!!</h1>'
            context ={ 'msg1':msg }
            return render(request, './myapp/admin_login.html',context)
    else:
        msg = ''
        context ={ 'msg1':msg }
        return render(request, './myapp/admin_login.html',context)


def admin_home(request):
    try:
        uname = request.session['user_name']
        print(uname)
    except:
        return admin_login(request)
    else:
        return render(request,'./myapp/admin_home.html')


def admin_logout(request):
    try:
        del request.session['user_name']
        del request.session['user_id']
    except:
        return admin_login(request)
    else:
        return admin_login(request)

def admin_changepassword(request):
    if request.method == 'POST':
        opasswd = request.POST.get('opasswd')
        npasswd = request.POST.get('npasswd')
        cpasswd = request.POST.get('cpasswd')
        uname = request.session['user_name']
        try:
            ul = user_login.objects.get(uname=uname,passwd=opasswd,u_type='admin')
            if ul is not None:
                ul.passwd=npasswd
                ul.save()
                context = {'msg': 'Password Changed'}
                return render(request, './myapp/admin_changepassword.html', context)
            else:
                context = {'msg': 'Password Not Changed'}
                return render(request, './myapp/admin_changepassword.html', context)
        except user_login.DoesNotExist:
            context = {'msg': 'Password Err Not Changed'}
            return render(request, './myapp/admin_changepassword.html', context)
    else:
        context = {'msg': ''}
        return render(request, './myapp/admin_changepassword.html', context)


from .models import bank_master

def admin_bank_master_add(request):
    if request.method == 'POST':
        bankname = request.POST.get('bankname')
        bankifsc = request.POST.get('bankifsc')
        bankaddress = request.POST.get('bankaddress')
        bankcontact = request.POST.get('bankcontact')
        bankemail = request.POST.get('bankemail')
        bm = bank_master(bankname=bankname,bankifsc=bankifsc,
                         bankaddress=bankaddress, bankcontact=bankcontact,
                         bankemail=bankemail)
        bm.save()
        context = {'msg': 'Record Added'}
        return render(request, './myapp/admin_bank_master_add.html', context)
    else:
        return render(request, './myapp/admin_bank_master_add.html')


def admin_bank_master_edit(request):
    if request.method == 'POST':
        s_id = request.POST.get('s_id')
        bankname = request.POST.get('bankname')
        bankifsc = request.POST.get('bankifsc')
        bankaddress = request.POST.get('bankaddress')
        bankcontact = request.POST.get('bankcontact')
        bankemail = request.POST.get('bankemail')
        bm = bank_master.objects.get(id=int(s_id))
        bm.bankname = bankname
        bm.bankaddress = bankaddress
        bm.bankifsc = bankifsc
        bm.bankcontact = bankcontact
        bm.bankemail = bankemail
        bm.save()
        msg = 'Record Updated'
        bm_l = bank_master.objects.all()
        context = {'bank_list': bm_l, 'msg': msg}
        return render(request, './myapp/admin_bank_master_view.html', context)
    else:
        id = request.GET.get('id')
        bm = bank_master.objects.get(id=int(id))
        context = {'bm': bm, 's_id': bm.id}
        return render(request, './myapp/admin_bank_master_edit.html',context)


def admin_bank_master_delete(request):
    id = request.GET.get('id')
    print('id = '+id)
    bm = bank_master.objects.get(id=int(id))
    bm.delete()
    msg = 'Record Deleted'
    bm_l = bank_master.objects.all()
    context = {'bank_list': bm_l, 'msg':msg}
    return render(request, './myapp/admin_bank_master_view.html',context)


def admin_bank_master_view(request):
    bm_l = bank_master.objects.all()
    context = {'bank_list':bm_l}
    return render(request, './myapp/admin_bank_master_view.html',context)

def admin_user_view(request):
    ul_l = user_login.objects.filter(u_type='user')

    tm_l = []
    for u in ul_l:
        ud = user_details.objects.get(user_id=u.id)
        tm_l.append(ud)

    context = {'user_list':tm_l,'type':'User Details'}
    return render(request, './myapp/admin_user_view.html',context)

def admin_user_delete(request):
    id = request.GET.get('id')
    print("id="+id)

    nm = user_details.objects.get(id=int(id))
    u_l = user_login.objects.get(id= nm.user_id)
    u_l.delete()

    nm.delete()

    ul_l = user_login.objects.filter(u_type='user')

    tm_l = []
    for u in ul_l:
        ud = user_details.objects.get(user_id=u.id)
        tm_l.append(ud)

    context = {'user_list': tm_l, 'type': 'User Details','msg':'User Removed'}
    return render(request, './myapp/admin_user_view.html', context)


def admin_staff_details_add(request):
    if request.method == 'POST':

        uname = request.POST.get('email')
        password = request.POST.get('pwd')
        #status = "new"

        ul = user_login(uname=uname, passwd=password, u_type='staff')
        ul.save()
        
        
        context = {'msg': 'Staff Registered'}
        return render(request, 'myapp/admin_staff_details_add.html',context)

    else:
        return render(request, 'myapp/admin_staff_details_add.html')

def admin_staff_view(request):
    ul_l = user_login.objects.filter(u_type='staff')

    
    context = {'staff_list':ul_l,'type':'Staff Details'}
    return render(request, './myapp/admin_staff_view.html',context)

def admin_staff_delete(request):
    id = request.GET.get('id')
    print("id="+id)

    u_l = user_login.objects.get(id= nm.user_id)
    u_l.delete()
    
    ul_l = user_login.objects.filter(u_type='staff')

    context = {'staff_list': ul_l, 'type': 'Staff Details','msg':'Staff Removed'}
    return render(request, './myapp/admin_staff_view.html', context)

########################################################################
############################ STAFF ###################################
def staff_login_check(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        passwd = request.POST.get('passwd')

        ul = user_login.objects.filter(uname=uname, passwd=passwd, u_type='staff')
        print(len(ul))
        if len(ul) == 1:
            request.session['user_id'] = ul[0].id
            request.session['user_name'] = ul[0].uname
            context = {'uname': request.session['user_name']}
            #send_mail('Login','welcome'+uname,uname)
            return render(request, 'myapp/staff_home.html',context)
        else:
            context = {'msg': 'Invalid Credentials'}
            return render(request, 'myapp/staff_login.html',context)
    else:
        return render(request, 'myapp/staff_login.html')

def staff_home(request):

    context = {'uname':request.session['user_name']}
    return render(request,'./myapp/staff_home.html',context)
    #send_mail("heoo", "hai", 'snehadavisk@gmail.com')

def staff_changepassword(request):
    if request.method == 'POST':
        uname = request.session['user_name']
        new_password = request.POST.get('new_password')
        current_password = request.POST.get('current_password')
        print("username:::" + uname)
        print("current_password" + str(current_password))

        try:

            ul = user_login.objects.get(uname=uname, passwd=current_password)

            if ul is not None:
                ul.passwd = new_password  # change field
                ul.save()
                context = {'msg':'Password Changed Successfully'}
                return render(request, './myapp/staff_changepassword.html',context)
            else:
                context = {'msg': 'Password Not Changed'}
                return render(request, './myapp/staff_changepassword.html', context)
        except user_login.DoesNotExist:
            context = {'msg': 'Password Not Changed'}
            return render(request, './myapp/staff_changepassword.html', context)
    else:
        return render(request, './myapp/staff_changepassword.html')

def staff_logout(request):
    try:
        del request.session['user_name']
        del request.session['user_id']
    except:
        return staff_login_check(request)
    else:
        return staff_login_check(request)

from .models import user_bank
from datetime import datetime

def staff_user_bank_add(request):
    if request.method == 'POST':

        bankid = int(request.POST.get('bankid'))
        #userid=int(request.session['user_id'])
        #ud = user_details.objects.get(user_id=userid)
        accno = request.POST.get('accno')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        type_of_acc = 'SB'
        dt = datetime.today().strftime('%Y-%m-%d')
        tm = datetime.today().strftime('%H:%M:%S')
        status = 'safe'
        balance = request.POST.get('balance')
        addr1 = request.POST.get('addr1')
        addr2 = request.POST.get('addr2')
        addr3 = request.POST.get('addr3')
        pin = request.POST.get('pin')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        gender = request.POST.get('gender')
        dob = request.POST.get('dob')
        ul = user_login(uname=email, passwd='1234', u_type='user')
        ul.save()
        userid = user_login.objects.all().aggregate(Max('id'))['id__max']
        try:
            ub = user_bank.objects.get(userid=userid)
            if ub is not None:
                ub.bankid = bankid
                ub.userid = userid
                ub.accno= accno
                ub.fname= fname
                ub.lname = lname
                ub.type_of_acc = type_of_acc
                ub.dt = dt
                ub.tm = tm
                ub.balance = balance
                ub.addr1 = addr1
                ub.addr2 = addr2
                ub.addr3 = addr3
                ub.pin = pin
                ub.email = email
                ub.contact = contact
                ub.save()
                b_l = bank_master.objects.all()
                context = {'msg': 'Bank Record Updated', 'bank_list': b_l}
                return render(request, 'myapp/user_bank_add.html', context)
            else:
                ub = user_bank(bankid=bankid, userid=userid, accno=accno,
                               fname=fname,lname=lname,type_of_acc='SB',
                               dt=dt, tm=tm, balance=balance, addr1=addr1,
                               addr2=addr2, addr3=addr3, pin=pin, email=email, 
                               contact=contact, dob=dob, gender=gender)
                ub.save()
                b_l = bank_master.objects.all()
                context = {'msg': 'Bank Record Added', 'bank_list': b_l}
                return render(request, 'myapp/staff_user_bank_add.html', context)
        except user_bank.DoesNotExist:
            ub = user_bank(bankid=bankid, userid=userid, accno=accno,
                           fname=fname, lname=lname, type_of_acc='SB',
                           dt=dt, tm=tm, balance=balance, addr1=addr1,
                           addr2=addr2, addr3=addr3, pin=pin, email=email, 
                           contact=contact, dob=dob, gender=gender)
            ub.save()
            b_l = bank_master.objects.all()
            context = {'msg': 'User Account Added', 'bank_list': b_l}
            return render(request, 'myapp/staff_user_bank_add.html', context)
    else:
        b_l = bank_master.objects.all()
        context = {'bank_list': b_l}
        return render(request, 'myapp/staff_user_bank_add.html', context)

def staff_user_bank_delete(request):
    id = request.GET.get('id')
    print("id="+id)
    ub = user_bank.objects.get(id=int(id))
    ub.delete()
    b_l = bank_master.objects.all()
    bl = {}
    for b in b_l:
        bl[b.id] = b.bankname
    user_id = int(request.session['user_id'])
    ub_l = user_bank.objects.filter(userid=user_id)
    context ={'userbank_list':ub_l,'bank_list':bl,'msg':'Deleted'}
    return render(request,'myapp/staff_user_bank_view.html',context)

def staff_user_bank_view(request):
    user_id = int(request.session['user_id'])
    b_l = bank_master.objects.all()
    user_id = int(request.session['user_id'])
    ub_l = user_bank.objects.all()
    context = {'userbank_list': ub_l, 'bank_list': b_l, 'msg': ''}
    return render(request, 'myapp/staff_user_bank_view.html', context)

def staff_staff_view(request):
    ul_l = user_login.objects.filter(u_type='staff')

    
    context = {'staff_list':ul_l,'type':'Staff Details'}
    return render(request, './myapp/staff_staff_view.html',context)

def staff_bank_master_view(request):
    bm_l = bank_master.objects.all()
    context = {'bank_list':bm_l}
    return render(request, './myapp/staff_bank_master_view.html',context)

#######################################################################
######################### USER###############################
from .models import user_details

def user_login_check(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        passwd = request.POST.get('passwd')

        ul = user_login.objects.filter(uname=uname, passwd=passwd, u_type='user')
        print(len(ul))
        if len(ul) == 1:
            request.session['user_id'] = ul[0].id
            request.session['user_name'] = ul[0].uname
            context = {'uname': request.session['user_name']}
            #send_mail('Login','welcome'+uname,uname)
            return render(request, 'myapp/user_home.html',context)
        else:
            context = {'msg': 'Invalid Credentials'}
            return render(request, 'myapp/user_login.html',context)
    else:
        return render(request, 'myapp/user_login.html')

def user_home(request):

    context = {'uname':request.session['user_name']}
    return render(request,'./myapp/user_home.html',context)
    #send_mail("heoo", "hai", 'snehadavisk@gmail.com')

def user_details_add(request):
    if request.method == 'POST':

        fname = request.POST.get('fname')
        lname = request.POST.get('lname')

        gender = request.POST.get('gender')
        age = request.POST.get('age')
        addr = request.POST.get('addr')
        pin = request.POST.get('pin')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        password = request.POST.get('pwd')
        uname=email
        #status = "new"

        ul = user_login(uname=uname, passwd=password, u_type='user')
        ul.save()
        user_id = user_login.objects.all().aggregate(Max('id'))['id__max']

        ud = user_details(user_id=user_id,fname=fname, lname=lname, gender=gender, age=age,addr=addr, pin=pin, contact=contact, email=email )
        ud.save()

        print(user_id)
        context = {'msg': 'User Registered'}
        return render(request, 'myapp/user_login.html',context)

    else:
        return render(request, 'myapp/user_details_add.html')

def user_changepassword(request):
    if request.method == 'POST':
        uname = request.session['user_name']
        new_password = request.POST.get('new_password')
        current_password = request.POST.get('current_password')
        print("username:::" + uname)
        print("current_password" + str(current_password))

        try:

            ul = user_login.objects.get(uname=uname, passwd=current_password)

            if ul is not None:
                ul.passwd = new_password  # change field
                ul.save()
                context = {'msg':'Password Changed Successfully'}
                return render(request, './myapp/user_changepassword.html',context)
            else:
                context = {'msg': 'Password Not Changed'}
                return render(request, './myapp/user_changepassword.html', context)
        except user_login.DoesNotExist:
            context = {'msg': 'Password Not Changed'}
            return render(request, './myapp/user_changepassword.html', context)
    else:
        return render(request, './myapp/user_changepassword.html')



def user_logout(request):
    try:
        del request.session['user_name']
        del request.session['user_id']
    except:
        return user_login_check(request)
    else:
        return user_login_check(request)

#############################################################

