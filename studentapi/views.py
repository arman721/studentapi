import io

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from studentapi.models import *
from studentapi.serializer import StudentSerializer


@csrf_exempt
def Studentapi(request):
    if request.method=='GET':
        data=request.body
        stream=io.BytesIO(data)
        print(stream)
        python_data=JSONParser().parse(stream)
        print(python_data)
        id=python_data.get("id",None)
        if id is not None:
            stu=Students.objects.get(id=id)
            serializer=StudentSerializer(stu)
            json_data=JSONRenderer().render(serializer.data)
            return HttpResponse(json_data)
        stu=Students.objects.all()
        serializer=StudentSerializer(stu,many=True)
        json_data=JSONRenderer().render(serializer.data)
        return HttpResponse(json_data)
    
    if request.method=='POST':
        data=request.body
        stream=io.BytesIO(data)
        python_data=JSONParser().parse(stream)
        serializer=StudentSerializer(data=python_data,many=True)
        if serializer.is_valid():
            serializer.save()
            res={"msg":"data saved"}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data)
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data)
    if request.method=="PUT":
        data=request.body
        stream=io.BytesIO(data)
        python_data=JSONParser().parse(stream)
        id=python_data["id"]
        stu=Students.objects.get(id=id)
        serializer=StudentSerializer(stu,data=python_data,partial=True)
        if serializer.is_valid():
            serializer.save()
            data={"msg":"data updated"}
            json_data=JSONRenderer().render(data)
            return HttpResponse(json_data)
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data)
    if request.method=="DELETE":
        data=request.body
        stream=io.BytesIO(data)
        python_data=JSONParser().parse(stream)
        ids=python_data["id"]
        for id in ids:
            try:
                Students.objects.get(id=id).delete()
            except Students.DoesNotExist:
                res = {"msg": f"Student with ID {id} does not exist."}
                json_data = JSONRenderer().render(res)
                return HttpResponse(json_data, content_type="application/json", status=404)
       
        res={"msg":"data deleted"}
        json_data=JSONRenderer().render(res)
        return HttpResponse(json_data)