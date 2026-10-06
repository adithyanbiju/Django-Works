import math

from django.shortcuts import render

# Create your views here.
from django.views import View
import math

class Home(View):

    def get(self,request):
        return render(request,'first.html')

class Add(View):
    def get(self,request):
        return render(request,'add.html')
    def post(self,request):

        data=request.POST
        n=int(data['n'])
        i=int(data['i'])

        s=n+i

        print(s)

        context={'result':s}

        return render(request,'add.html',context)

class Fact(View):
    def get(self,request):
        return render(request,'fact.html')
    def post(self,request):

        data=request.POST
        n=int(data['n'])

        f=math.factorial(n)

        print(f)

        context={'result':f}

        return render(request,'fact.html',context)

