from django.shortcuts import render
from django.template.context_processors import request
from django.templatetags.i18n import language

# Create your views here.
from django.views import View
from django.http import HttpResponse
from books.models import Books

class Home(View):
    def get(self,response):
        return render(request,'home.html')

class Add_book(View):
    def get(self,request):
        return render(request, 'book.html')
    def post(self,request):
        data=request.POST
        t=data['title']
        a=data['author']
        p=data['price']
        l=data['language']
        s=data['pages']

        b=Books.objects.create(title=t,author=a,price=p,language=l,pages=s)

class view_books(View):
    def get(self,request):
        books=Books.objects.all()
        context={'books':books}
        return  render(request,view_books.html,context)