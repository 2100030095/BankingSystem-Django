from importlib.resources import _

from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.tokens import default_token_generator
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from django.template import loader
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import FormView

from .forms import StudentForm,MyForm
from .functions import handle_uploaded_file
from .models import *
from django.contrib.auth import login ,logout,authenticate


# Create your views here.
def test(request):
    form=MyForm()
    return render(request,'login.html',{'form':form})
def index(request):
    return render(request,'index.html')
def registration(request):
    error = ""
    if request.method == 'POST':
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        ec = request.POST['empcode']
        ac = request.POST['acctype']
        gender = request.POST['Gender']
        em = request.POST['email']
        pwd = request.POST['pwd']
        try:
            user = User.objects.create_user(first_name=fn,last_name=ln,username=em,password=pwd)
            employee=EmployeeDetails.objects.create(user=user,Mobile_Number=ec,Name=ln,Email=em,Account=ac,gender=gender)
            tr=Transactions.objects.create(user=user,balance=500)
            ac=Account.objects.create(user=user,Name=ln,Account_balance=500)
            l=Loans.objects.create(user=user)

            error = "no"

        except:
            error = "yes"
    return render(request,'registration.html',locals())

def login_user(request):
    error = ""
    if request.method == 'POST':
        form=MyForm(request.POST)
        if form.is_valid():
            u = request.POST['emailid']
            p = request.POST['password']
            user = authenticate(username=u, password=p)
            if user:
                login(request, user)
                error = "no"
            else:
                error = "yes"

    return render(request, 'login.html', locals())

def base(request):
    if not request.user.is_authenticated:
        return redirect('login_user')
    user=request.user
    ac = Account.objects.get(user=user)
    #id=Transactions.objects.get(user=user)
    employee=EmployeeDetails.objects.get(user=user)
    return render(request,'base.html')

def withdraw(request):
    if not request.user.is_authenticated:
        return redirect('login_user')

    error = ""

    user = request.user

    if request.method == "POST":
        amt = request.POST['with']
        id=Transactions.objects.create(user=user,balance=amt)
        ac=Account.objects.get(user=user)
        a=ac.Account_balance
        c=a-int(id.balance)
        ac.Account_balance=c
        ac.save()
        #transaction=Transactions.objects.get(id=id)




        try:
            transaction.save()
            error="no"

        except:
            error="yes"
    return render(request,'withdraw.html',locals())

def deposite(request):
    if not request.user.is_authenticated:
        return redirect('login_user')
    error=""
    user = request.user
    mydata = Transactions.objects.filter(user_id=request.user).values()


    #a=id.balance
    if request.method=="POST":
        amt = request.POST['dep']
        id = Transactions.objects.create(user=user, balance=amt)
        ac = Account.objects.get(user=user)
        a = ac.Account_balance
        c = a + int(id.balance)
        ac.Account_balance = c
        ac.save()
        acc=Account.objects.get(user=user)
        try:

            #Transactions.objects.create(user=user,balance=c)

            error = "no"

        except:
            error = "yes"

    return render(request,'deposite.html')

def transaction(request):

    if not request.user.is_authenticated:
        return redirect('login_user')

    #user = request.user
    user=request.user
    ac = Account.objects.filter(user_id=user).values()
    mydata = Transactions.objects.filter(user_id=user).values()
    template = loader.get_template('transaction.html')
    context = {
        'mydata': mydata,
        'ac':ac,
        }
    return HttpResponse(template.render(context, request))

def profile(request):
    if not request.user.is_authenticated:
        return redirect('login_user')

    error = ""
    user = request.user
    employee = EmployeeDetails.objects.get(user=user)
    ac = Account.objects.get(user=user)

    if request.method == "POST":
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        ec = request.POST['empcode']
        em = request.POST['email']
        Acc = request.POST['acctype']

        gender = request.POST['gender']

        employee.user.first_name = fn
        employee.user.last_name = ln
        employee.Name=ln
        employee.Mobile_Number = ec
        employee.Email = em
        employee.Account=Acc
        employee.gender = gender


        try:
            employee.save()
            employee.user.save()
            error="no"

        except:
            error="yes"
    return render(request,'profile.html',locals())

def change_pass(request):
    if not request.user.is_authenticated:
        return redirect('login_user')

    error = ""
    user = request.user
    if request.method == "POST":
        c = request.POST['currentpassword']
        n = request.POST['newpassword']
        try:
            if user.check_password(c):
                user.set_password(n)
                user.save()
                error="no"
            else :
                error="not"

        except:
            error="yes"
    return render(request,'change_pass.html',locals())

def logout(request):


    return HttpResponseRedirect('test')

def admin_login(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['username']
        p = request.POST['pwd']
        user = authenticate(username=u,password=p)
        try:
            if user.is_staff:
               login(request,user)
               error="no"
            else:
               error="yes"

        except :
            error="yes"
    return render(request,'admin_login.html',locals())
def admin_home(request):
    return render(request,'admin_home.html')


def change_passwordadmin(request):

    error = ""

    user = request.user
    if request.method == "POST":
        c = request.POST['currentpassword']
        n = request.POST['newpassword']
        try:
            if user.check_password(c):

                user.save()
                error = "no"
            else:
                error = "not"

        except:
            error = "yes"
    return render(request, 'change_passwordadmin.html', locals())

def loans(request):
    if not request.user.is_authenticated:
        return redirect('login_user')
    return render(request,'loans.html')

def cards(request):
    if not request.user.is_authenticated:
        return redirect('login_user')
    return render(request,'cards.html')

def apply_loan(request):
    if not request.user.is_authenticated:
        return redirect('login_user')
    user= request.user
    if request.method == 'POST':
        student = StudentForm(request.POST, request.FILES)
        if student.is_valid():
            file=request.FILES['file']
            handle_uploaded_file(request.FILES['file'])
            Docc.objects.create(user=user,File=file)
            return HttpResponse("File uploaded successfuly","base") and redirect('base')
    else:
        student = StudentForm()
        return render(request,"apply_loan.html",{'form':student})

def apply(request):

    error = ""
    if request.method == 'POST':
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        ec = request.POST['empcode']
        em = request.POST['email']
        prf = request.POST['proof']
        ltype = request.POST['ltype']
        user = request.user
        if Loans.objects.get(user=user):
            l=Loans.objects.get(user=user)
            l.Name=ln
            l.Mobile=ec
            l.Email=em
            l.Proof=prf
            error="no"
            l.save()
        else:

            try:

                loan=Loans.objects.create(user=user,Name=ln,Mobile=ec,Email=em,Proof=prf)

                error = "no"

            except:
                error = "yes"
    return render(request,'apply.html',locals())

def transfer(request):
    if not request.user.is_authenticated:
        return redirect('login_user')
    error=""
    user = request.user
    mydata = Transactions.objects.filter(user_id=request.user).values()


    #a=id.balance
    if request.method=="POST":
        tr=request.POST['em']
        amt = request.POST['transfer']
        id = Transactions.objects.create(user=user, balance=amt)
        u=EmployeeDetails.objects.get(Email=tr)
        u_id=u.user_id
        ac = Account.objects.get(user=user)
        trto=Account.objects.get(user=u_id)
        ta=trto.Account_balance
        a = ac.Account_balance
        c = a - int(id.balance)
        d=ta+ int(id.balance)
        ac.Account_balance = c
        trto.Account_balance=d
        trto.save()
        ac.save()
        acc=Account.objects.get(user=user)
        try:

            #Transactions.objects.create(user=user,balance=c)

            error = "no"

        except:
            error = "yes"

    return render(request,'transfer.html')

class PasswordContextMixin:
    extra_context = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'title':self.title,
            **(self.extra_context or {})
        })
        return context

class PasswordResetView(PasswordContextMixin, FormView):
    email_template_name = 'registration/password_reset_email.html'
    extra_email_context = None
    form_class = PasswordResetForm
    form_email = 'chsatish7095@gmail.com'
    html_email_template_name = None
    subject_template_name = 'registration/password_reset_subject.html'
    success_url = reverse_lazy('password_reset_done')
    template_name = 'registration/password_reset_form.html'
    title = _('Password reset')
    token_generator = default_token_generator

    @method_decorator(csrf_protect)
    def dispatch(self,*args, **kwargs):
        return super().dispatch(*args, **kwargs)




