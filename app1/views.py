from django.shortcuts import render,HttpResponse
from app1 import models


def student(req):
    stulist=models.Student.objects.all()
    clslist=models.Classes.objects.all()
    return render(req,'student.html',{'stulist':stulist,'clslist':clslist})

def add_student(req):
    response={'status':True,'message':None,'data':None}
    try:
        s=req.POST.get('stuname')
        a=req.POST.get('age')
        g=req.POST.get('gender')
        c=req.POST.get('clsid')
        obj=models.Student.objects.create(
            stuname=s,
            age=a,
            gender=g,
            cs_id=c,
        )
        response['data']=obj.id
    except Exception as e:
        response['status']=False
        response['message']='用户输入错误'
    import json
    result=json.dumps(response,ensure_ascii=False)
    return HttpResponse(result)

def del_student(req):
    ret={'status':True}
    try:
        nid=req.GET.get('nid')
        models.Student.objects.filter(id=nid).delete()
    except Exception as e:
        ret['ststus'] = False
    import json
    return HttpResponse(json.dumps(ret))