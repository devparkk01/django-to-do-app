from app.models import Item
from django.contrib.auth import login , authenticate, logout
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import ItemForm
from django.contrib.auth.decorators import login_required
from .models import Item
from django.contrib.auth.models import User
from django.core.paginator import Paginator 


@login_required(login_url= "login")
def home_view(request) :
    form = ItemForm() 
    user = request.user 
    all_items = Item.objects.filter(user = user ).order_by('priority')
    p =  Paginator(all_items , 5 ) 
    page_number = request.GET.get('page' ) 

    page = p.get_page(page_number  ) 
    context = { 'form' : form , 'all_items' : page }
    return render(request , 'app/home.html' , context = context ) 


def add_item(request ) :
    form = ItemForm(request.POST) 
    if (form.is_valid()) :
        form_saved = form.save(commit = False )
        form_saved.user = request.user 
        form_saved.save() 
        return redirect('home')
    else :
        return render(request , 'app/home.html' , {'form' : form })



@login_required(login_url= 'login')
def delete_item(request , id ) :
    item = Item.objects.get(pk = id)
    item.delete()
    return redirect('home')

@login_required(login_url= 'login')
def change_status(request , id , status ) :
    item = Item.objects.get(pk = id )
    item.status = status 
    item.save()
    return redirect('home')

@login_required(login_url= 'login')
def delete_completed(request , username) :
    query_user = User.objects.filter(username = username )[0]
    all_item = Item.objects.filter(user = query_user , status = 'C')  
    all_item.delete()
    return redirect('home') 


@login_required(login_url= 'login')
def delete_all( request ,username  ) :
    query_user = User.objects.filter(username = username)[0]
    all_item = Item.objects.filter(user = query_user )  
    all_item.delete()
    return redirect('home')


def login_view (request ) :
    if ( request.method == "POST") :
        form = AuthenticationForm(data = request.POST) 
        if ( form.is_valid())  : 
            username = request.POST['username'] 
            password = request.POST['password']
            user = authenticate(request ,username = username ,password = password)

            if ( user ) : 
                login(request ,user =  user ) 
                return redirect('home') 
            else : print("user not found ") 
        # else :
        print("Form invalid ")
        return render(request , 'app/login.html' , {'form' : form } )

    else : 
        form = AuthenticationForm() 
        return render(request , 'app/login.html' , {'form' : form } ) 



def register_view (request ) :
    if request.method == "POST" :
        form = UserCreationForm( request.POST)
        if ( form.is_valid()) :
            form.save() 
            username = form.cleaned_data.get("username") 
            password = form.cleaned_data.get("password1") 
            user = authenticate(request , username = username , password = password )
            print(user)
            print(user.get_username())
            print(type(user))
            return redirect('home' )
        else :
            return render(request , 'app/register.html' , {'form' : form }) 

    else :
        form = UserCreationForm() 
        return render(request , 'app/register.html' , {'form' : form } ) 


def logout_view (request ) :
    logout(request ) 
    return redirect("home")

