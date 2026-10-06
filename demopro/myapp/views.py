from django.contrib.admin.actions import delete_selected
from django.db.models import Model
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

class GoodMorning(View):
    def get(self, request):
          data={"Message":"Good Morning"}
          return JsonResponse(data)



class HelloWorld(View):
    def get(self,request):
        data = {"Message": "Hello World"}
        return JsonResponse(data)



class GoodEvening(View):
    def get(self,request):
        data = {"Message": "Good Evening"}
        return JsonResponse(data)




class UserDetails(View):

    def get(self,request):
        data =[
        {'name':"Adhi",'age':21,'place':'ekm'},
        {'name': "Akhilesh", 'age': 22, 'place': 'ekm'},
        {'name': "Aadhil", 'age': 23, 'place': 'ekm'}

        ]

        return JsonResponse(data,safe=False)


#Apiview for reading all student record

from myapp.models import Student

class StudentList(View):
    def get(self,request):
        s=list(Student.objects.all().values())

        return JsonResponse(s,safe=False)

#apiview for creating a new student record

from json import loads

@method_decorator(csrf_exempt,name="dispatch")
class StudentCreate(View):
    def post(self,request):
        data=loads(request.body)  #coverts json data into python native type

        r=data['roll_no']
        n=data['name']
        a=data['age']
        p=data['place']
        m=data['marks']

        s=Student.objects.create(roll_no=r,name=n,age=a,place=p,marks=m)
        s.save()

        return JsonResponse({"message":"Inserted Data successfully"})

#api view for reading a specific record
class StudentDetails(View):
    def get(self,request,i):
        s=list(Student.objects.filter(id=i).values())  #json to dictionary
        if s:
            return JsonResponse(s,safe=False)
        else:
            return JsonResponse({"message":"No Student Data"})

@method_decorator(csrf_exempt,name='dispatch')
class StudentDelete(View):
    def delete(self,request,i):
        s=Student.objects.get(id=i)
        s.delete()
        return JsonResponse({"Message":"Delete successfully"})

import json
@method_decorator(csrf_exempt,name='dispatch')
class Studentfullupdate(View):
    def put(self,request,i):
                                                     #request.body-data coming from client app
                                                     #loads used to translate coming json data into
                                                     #python native/dictonaryt
        data=json.loads(request.body)

        print(data)
        try:
            s=Student.objects.get(id=i)


            s.roll_no=data['roll_no']
            s.name=data['name']
            s.age=data['age']
            s.place=data['place']
            s.marks=data['marks']
            s.save()
            return JsonResponse({'message':'updated successfully'})
        except:
            return JsonResponse({'message':"No student Data"})

        
@method_decorator(csrf_exempt,name='dispatch')
class Studentpartialupdate(View):
    def patch(self,request,i):
        data=json.loads(request.body)
        try:
                s=Student.objects.get(id=i)
                if 'roll_no' in data:
                 s.roll_no=data['roll_no']
                if 'name' in data:
                 s.name=data['name']
                 if 'age' in data:
                  s.age=data['age']
                if 'place' in data:
                 s.place=data['place']
                if 'marks' in data:
                 s.marks=data['marks']
                 s.save()

                return JsonResponse({'message':'Update partially'})
        except:
                return JsonResponse({'message':'No student data'})