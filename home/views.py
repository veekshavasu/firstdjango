from django.shortcuts import render,redirect
from .forms import bookforms,searchform,modelbookforms
from home.models import book
from django.utils import timezone
from django.contrib import messages
# Create your views here.
#def home_view3(request):
   # return render(request,'home.html')

#def home_view(request):
   # return render(request,'signup.html')


#def home_view1(request):
    #return render(request,'login.html')


#def design(request):
    #return render(request,'home2.html')


def form_view(request):
    context=None
    msg=None
    form=None
    b= book.objects.all()
    if request.method=='POST':
        form=bookforms(request.POST)
        if form.is_valid():
            #b=book.objects(book_name=form.cleaned_data('name'),
             #   author_name=form.cleaned_data('author'),
              #  date=form.cleaned_data('date'))
            b=book.objects.Create(book_name=form.cleaned_data('name'),
                author_name=form.cleaned_data('author'),
                date=form.cleaned_data('date'))
            b.save()
            msg='Book added successfully!!!'
        else:
            msg=form.errors        
    else:
        form=bookforms()
    context={'msg':msg,'forms':form,'bk':b}
    return render(request,'forms.html',context)



def model_form(request):
    if request.method=='POST':
        form=modelbookforms(request.POST)
        if form.is_valid():
            form.save()
            msg='Book added successfully!!!'
        else:
            msg=form.errors        
    else:
        form=modelbookforms()
    context={'msg':msg,'forms':form,'bk':b}
    return render(request,'forms.html',context)


def html_form(request):
    value=''
    if request.method=='POST':
        value==request.POST.get('name')
        return render(request,'values.html',{'value':value})  
    else:
        value='wrong input'
        return render(request,'home1.html')  



def booksearch(request):
    if request.method=='POST':
        form=modelbookforms(request.POST)
        if form.is_valid():
            q=form.cleaned_data.get('q')
            b=book.objects.filter(book_name__contains=q,purchase_date=timezone.now)
            return render(request,'showtables.html',{'book':b})
    else:
        form=searchform()
        b= book.objects.all()
    return render(request,'showtables.html',{'book':b,'form':form})



def deletebook(request,id):
    b=book.objects.get(id=id)
    b.delete()
    messages.success(request,'Deleted #'+str(id)+'successfully!!')
    return redirect('/')


def editbooks(request,id):
    b=book.objects.get(id=id)
    if request.method=='POST':
        form=modelbookforms(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Book Updated Successfully!!')
            return redirect('/')
    else:
        form=modelbookforms(instance=b)
    return render(request,'editbook.html',{'form':form})