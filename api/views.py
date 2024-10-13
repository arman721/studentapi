from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework.renderers import JSONRenderer

from api.models import Student
from api.serializer import StudentSerializer


# Create your views here.
def studentinfo(request,id):
    stu=Student.objects.get(id=id)
    serializer=StudentSerializer(stu)
    # json_data=JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data)
    return JsonResponse(serializer.data,safe=False)

def studentlist(request):
    stu=Student.objects.all()
    serializer=StudentSerializer(stu,many=True)
    # json_data=JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data)
    return JsonResponse(serializer.data,safe=False)
