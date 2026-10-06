from django.http import JsonResponse
from django.shortcuts import render
from django.template.context_processors import csrf
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

from myapp.models import Employee
class Employeelist(View):
    def get(self,request):
        qs= Employee.objects.all().values()
        
        e=list(qs)

        return JsonResponse(data=e)

from json import loads
@method_decorator(csrf_exempt,name='dispatch')
class EmployeeCreate(View):
    def post(self,request):
        data=loads(request.body)
        # i=data['emp_id']
        # n=data['name']
        # a=data['age']
        # g=data['gender']
        # p=data['place']
        # j=data['joining_date']
        # s=data['salary']
        # d=data['designation']

        e=Employee.objects.create(**data)
        e.save()
        return JsonResponse({'message':'created'})