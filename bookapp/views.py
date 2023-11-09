from django.shortcuts import render,redirect
from django.views.generic import View
from bookapp.models import Books
from bookapp.forms import BookCreateForm,BookChangeForm

# Create your views here.

class BookCreateView(View):
    def get(self,request,*args,**kwargs):
        form=BookCreateForm()
        return render(request,"book_add.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=BookCreateForm(request.POST)
        if form.is_valid():
            Books.objects.create(**form.cleaned_data)
            print("'book created")
            return render(request,"book_add.html",{"form":form})
        else:
            return render(request,"book_add.html",{"form":form})
        
class BookListView(View):
    def get(self,request,*args,**kwargs):
        qs=Books.objects.all()
        return render(request,"book_list.html",{"books":qs})
    
class BookDetailView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Books.objects.get(id=id)
        return render(request,"book_detail.html",{"book":qs})
    
class BookDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Books.objects.filter(id=id).delete()
        return redirect('book-list')
    
class BookUpdateView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        obj=Books.objects.get(id=id)
        form=BookChangeForm(instance=obj)
        return render(request,"book_edit.html",{"form":form})

    
    

