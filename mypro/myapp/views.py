from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

# def first(request):
#     return HttpResponse("first page")
# def second(request):
#     return HttpResponse("second page")

from django.views import View
from django.views.static import directory_index

# class First(View):
#
#     def get(self,request):
#
#         return HttpResponse("""
#
#        <h1>First page</h1>
#        <h1>hello</h1>
#         """)
#
# class Second(View):
#     def get(self,request):
#
#         return HttpResponse("<h1>second page</h1>")
#
from myapp.models import Person
from myapp.models import Movie

class First(View):
    def get(self,request):
        # data = [{"name": "adithyan", "age": "21","place":"ekm"},
        #         {"name": "abin", "age": "21", "place": "alp"},
        #          {"name": "akhil", "age": "21", "place": "tvm"}]
        data = Person.objects.all()
        context={'data':data}

        return render(request,'first.html',context)


class Second(View):
    def get(self,request):
        data1 = {"name": "ajith", "age": "32","place":"ktm"}


        return render(request,'second.html',context=data1)

class Movie_list(View):
    def get(self,request):
        data=Movie.objects.all()
        context = {'data': data}
        return render(request, 'movie.html', context)

class Add_movie(View):
    def get(self,request):
        return render(request, 'addmovie.html')
    def post(self,request):
        print(request.POST)
        data=request.POST
        n=data['n']
        d=data['i']
        y=data['y']
        print(n,d,y)
        m=Movie.objects.create(movie=n,director=d,year=y)
        m.save()

        return render(request, 'addmovie.html')


