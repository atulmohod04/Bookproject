from django.contrib import messages
from django.contrib.auth import authenticate, login  # add this
from django.contrib.auth.forms import AuthenticationForm  # add this
from django.http import HttpResponse
from django.shortcuts import redirect, render

from .models import Book

# Create your views here.
# def homepage(request):
#     return HttpResponse("hello django")

def homepage(request):
    bookinformation = Book.active_objects.all()  
    return render(request,template_name="index.html" ,context={'msg':'test django',"books":bookinformation})


def save_book_info(request):
    if request.method == 'POST':
        print(request.POST)
        if request.POST.get('bid'):
            book_edit = Book.active_objects.get(id=request.POST.get('bid'))
            book_edit.name = request.POST['name']
            book_edit.author = request.POST['author']
            book_edit.prize = request.POST['prize']
            book_edit.publication = request.POST['publication']
            book_edit.save()
            messages.success(request, f'Book "{book_edit.name}" updated successfully..!')
        else:
            nam=request.POST["name"]
            auth=request.POST["author"]
            priz=request.POST["prize"]
            pub=request.POST["publication"]
            bookinfosave=Book(name=nam,author=auth,prize=priz,publication=pub)
            bookinfosave.save()

            messages.success(request, 'Data ADD successful')
    
        return redirect("/homepage/")
    else:
        return HttpResponse("Wrong method invoked..!")


def delete_data(request,id):
    # return render(request, 'index.html')
    delete_book = Book.active_objects.get(id=id) 
    delete_book.is_delete = 1
    delete_book.save()
    messages.success(request, 'Data Delete successful')
    return redirect("/homepage/")

def edit_book(request,id):
    edit_book = Book.active_objects.get(pk=id)
    bookinformation = Book.active_objects.all() 
    return render(request,template_name="index.html" ,context={"book":edit_book,"books":bookinformation})


def show_deleted_book(request):
    bookinformation = Book.Inactive_objects.all()  
    return render(request,template_name="index.html" ,context={"deleted":"yes","books":bookinformation})


def restore_book(request,id):
    bookinformation = Book.book_objects.get(pk=id) 
    bookinformation.is_delete = 0
    bookinformation.save()
    return redirect("/homepage/")

from django.contrib import messages
from django.contrib.auth import login , logout
from django.shortcuts import redirect, render

from .forms import NewUserForm


def landing_page(request):
    return render(request,template_name="landing_page.html" ,context={})


def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			return redirect("/login/")

		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm
	return render (request=request, template_name="register.html", context={"register_form":form})


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)   
        # print(form) 
        if form.is_valid():
            usrnm = form.cleaned_data.get('username')
            pswd = form.cleaned_data.get('password')
            user_obj = authenticate(request, username=usrnm, password=pswd)
            # print(user_obj)
            if user_obj:
                login(request, user_obj)
                messages.info(request, f"User logged in successfully..{usrnm}")
                return redirect("user_info")

    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form":form})



def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return render(request,template_name="logout.html" ,context={})

def user_info(request):
    return render(request, template_name="user_info.html")

# git op
def book():
    print("helloatul")