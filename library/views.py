from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
from .models import *
from .forms import *
from .filters import * 
from .emailbackend import EmailBackEnd

# Create your views here.

def dashboard(request):
    book = Book.objects.all()
    category = Category.objects.all()
    author = Author.objects.all()
    publisher = Publication.objects.all()
    total_book = book.count()
    total_category = category.count()
    total_author = author.count()
    total_publication = publisher.count()
    context = {'total_book':total_book,
               'total_category':total_category,
               'total_author':total_author,
               'total_publication':total_publication}
    return render(request,'library/status.html',context)


def base(request):
    return render(request,'view/base.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/base')
    else:
        form=RegisterForm()
    return render(request,'view/register.html',{'form':form})

def loginpage(request):
    if request.method == 'POST':
         username = request.POST.get("email")
         password = request.POST.get("password")
         user =EmailBackEnd.authenticate(request,username=username,password=password)
         if user is not None:
            login(request,user)
            return redirect('/base')
         else:
             messages.info(request,'invalid information')
             return redirect('login')
    else:
         return render(request,'view/login.html')
                
def logoutpage(request):
    logout(request)
    return redirect('login')


def book(request):
    books= Book.objects.all()
    myFilter = bookFilter(request.GET,queryset=books)
    books = myFilter.qs
    page= request.GET.get('page',1)
    paginator = Paginator(books, 2)
    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        books = paginator.page()
    except EmptyPage:
       books = paginator.page(paginator.num_pages)
    context ={
        'books':books,
        'myFilter':myFilter,
    }
    return render(request,'library/book.html',context)

def author(request):
    authors = Author.objects.all()
    myFilter = authorFilter(request.GET,queryset=authors)
    authors = myFilter.qs
    context={
        'authors':authors,
        'myFilter':myFilter
    }
    return render(request,'library/author.html',context)

def category(request):
    categories = Category.objects.all()
    myFilter = categoryFilter(request.GET,queryset=categories)
    categories = myFilter.qs
    context={
        'categories':categories,
        'myFilter':myFilter
    }
    return render(request,'library/category.html',context)

def publication(request):
    publishers=Publication.objects.all()
    myFilter = publishFilter(request.GET,queryset=publishers)
    publishers=myFilter.qs
    context = {
        'publishers':publishers,
        'myFilter':myFilter
    }
    return render(request,'library/publication.html', context)


def transaction(request):
    return render(request,'library/transaction.html')

def student(request):
    return render(request,'library/student.html')

def teacher(request):
    return render(request,'library/teacher.html')

def addBook(request):
    form = bookForm()
    if request.method == 'POST':
        form = bookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/book')


    context = {'form':form}
    return render(request,'library/addbook.html',context)

def addAuthor(request):
    form = authorForm()
    if request.method == 'POST':
        form = authorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/author')


    context = {'form':form}
    return render(request,'library/addauthor.html',context)


def addCategory(request):
    form = categoryForm()
    if request.method == 'POST':
        form = categoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/category')
    
    context = {'form':form}
    return render(request,'library/addcategory.html',context)

def addPublication(request):
    form = publishForm()
    if request.method == 'POST':
        form = publishForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/publication')


    context = {'form':form}
    return render(request,'library/addpublication.html',context)

def updateBook(request,pk):
    book = Book.objects.get(id=pk)
    form = bookForm(instance=book)
    if request.method == 'POST':
        form = bookForm(request.POST,instance=book)
        if form.is_valid():
            form.save()
            return redirect('/book')
    context = {
        'form':form
        }
    return render(request,'library/addbook.html',context)


def updateAuthor(request,pk):
    author = Author.objects.get(id=pk)
    form = authorForm(instance=author)
    if request.method == 'POST':
        form = authorForm(request.POST,instance=author)
        if form.is_valid():
            form.save()
            return redirect('/author')
    context = {'form':form}
    return render(request,'library/addauthor.html',context)

def updateCategory(request,pk):
    category = Category.objects.get(id=pk)
    form = categoryForm(instance=category)
    if request.method == 'POST':
        form =categoryForm(request.POST,instance=category)
        if form.is_valid():
            form.save()
            return redirect('/category')
    context = {'form':form}
    return render(request,'library/addcategory.html',context)

def updatePublication(request,pk):
    publication = Publication.objects.get(id=pk)
    form = publishForm(instance=publication)
    if request.method == 'POST':
        form = publishForm(request.POST,instance=publication)
        if form.is_valid():
            form.save()
            return redirect('/publication')

    context = {'form':form}
    return render(request,'library/addpublication.html',context)

def deleteBook(request,pk):
    form = Book.objects.get(id=pk)
    if request.method == 'POST':
        form.delete()
        return redirect('/book') 
    test = {
        'form':form
    }
    return render(request,'library/deletebook.html',test)

def deleteAuthor(request,pk):
    form = Author.objects.get(id=pk)
    if request.method == 'POST':
        form.delete()
        return redirect('/author') 
    test = {
        'form':form
    }
    return render(request,'library/deleteauthor.html',test)

def deleteCategory(request,pk):
    form = Category.objects.get(id=pk)
    if request.method == 'POST':
        form.delete()
        return redirect('/category') 
    test = {
        'form':form
    }
    return render(request,'library/deletecategory.html',test)


def deletePublication(request,pk):
    form = Publication.objects.get(id=pk)
    if request.method == 'POST':
        form.delete()
        return redirect('/publication') 
    test = {
        'form':form
    }
    return render(request,'library/deletepublication.html',test)

