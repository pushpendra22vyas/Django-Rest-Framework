from django.shortcuts import render
from .models import Student
from .serializer import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse

# Create your views here.

def student_detail(request,pk):
    stu = Student.objects.get(id = pk)
    serializer = StudentSerializer(stu)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')
    # return JsonResponse(serializer.data,safe=True)       # When safe = True , the data must be in form of Dictionary. When data is not in dictionary form we use safe = False


def students_detail(request):
    stu = Student.objects.all()
    # print(stu)
    # <QuerySet [<Student: Pushpendra>, <Student: Ethan Hunt>, <Student: Toney Stark>]>
    serializer = StudentSerializer(stu,many = True)
    # print(serializer)
    # StudentSerializer(<QuerySet [<Student: Pushpendra>, <Student: Ethan Hunt>, <Student: Toney Stark>]>, many=True):
    # name = CharField(max_length=100)
    # roll_no = IntegerField()
    # city = CharField(max_length=100)
    ####################################################################################
    # print(serializer.data)
    # [OrderedDict([('name', 'Pushpendra'), ('roll_no', 22), ('city', 'Udaipur')]), 
    # OrderedDict([('name', 'Ethan Hunt'), ('roll_no', 20), ('city', 'California')]),
    # OrderedDict([('name', 'Toney Stark'), ('roll_no', 20), ('city', 'New York')])]
    json_data = JSONRenderer().render(serializer.data)
    # print(json_data)
    # [{"name":"Pushpendra","roll_no":22,"city":"Udaipur"},
    # {"name":"Ethan Hunt","roll_no":20,"city":"California"},
    # {"name":"Toney Stark","roll_no":20,"city":"New York"}]
    return HttpResponse(json_data, content_type='application/json')

