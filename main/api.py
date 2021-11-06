from datetime import datetime
import json
from django.http import JsonResponse
from django.http.response import HttpResponse, HttpResponseBadRequest
from django.shortcuts import get_object_or_404


from .models import Student, Module

def student_modules_api(request, student_id):
    if request.method == "DELETE":
        student = get_object_or_404(Student, student_number=student_id)

        body_unicode = request.body.decode('utf8')
        body_data = json.loads(body_unicode)

        modules = body_data['modules']

        for module in modules:
            studentModule = student.modules_studying.get(module_code=module)
            student.modules_studying.remove(studentModule)

        return JsonResponse({})

    if request.method == "PUT":
        student = get_object_or_404(Student, student_number=student_id)

        body_unicode = request.body.decode('utf8')
        body_data = json.loads(body_unicode)

        module = body_data['module']

        student.modules_studying.add(Module.objects.get(module_code=module))
        student.save()

        return JsonResponse({'data': (Module.objects.get(module_code=module)).to_dict() })

    return HttpResponseBadRequest("Bad Request")

def module_api(request, id):
    if request.method == "PUT":
        module = get_object_or_404(Module, module_code=id)

        body_unicode = request.body.decode('utf8')
        body_data = json.loads(body_unicode)

        module.level = int(body_data["level"])
        module.credits = int(body_data["credits"])

        module.save()

        return JsonResponse({"success": True})

    if request.method == "DELETE":
        module = get_object_or_404(Module, module_code=id)
        module.delete()
        return JsonResponse({})
    
    return HttpResponseBadRequest("Bad Request")

def add_module_api(request):
    if request.method == "POST":
        body_unicode = request.body.decode('utf8')
        body_data = json.loads(body_unicode)

        id = body_data["id"]
        name = body_data["name"]
        level = int(body_data["level"])
        credits = int(body_data["credits"])
        created = datetime.now()

        module = Module(module_code=id, module_name=name, level=level, credits=credits, created=created)

        module.save()

        return JsonResponse({'data': module.to_dict()})

    return HttpResponseBadRequest("Bad Request")


def add_student_api(request):
    if request.method == "POST":
        body_unicode = request.body.decode('utf8')
        body_data = json.loads(body_unicode)

        
        studentId = body_data["id"]
        first_name = body_data['first_name']
        surname = body_data['surname']
        programme = body_data['programme']
        year = body_data['year']
        modules = body_data['modules']

        student = Student(student_number=studentId, first_name=first_name, surname=surname, year_of_study=year, programme=programme)
        
        student.save()

        for module in modules:
            student.modules_studying.add(Module.objects.get(module_code=module))

        print(student.to_dict())
        return JsonResponse({'data': student.to_dict()})

    return HttpResponseBadRequest("Bad Request")


def student_api(request, student_id):
    if request.method == "DELETE":
        student = get_object_or_404(Student, student_number=student_id)
        student.delete()
        return JsonResponse({})

    if request.method == "PUT":
        student = get_object_or_404(Student, student_number=student_id)
        
        body_unicode = request.body.decode('utf8')
        body_data = json.loads(body_unicode)
        
        student.first_name = body_data['first_name']
        student.surname = body_data['surname']
        student.programme = body_data['programme']
        student.year_of_study = int(body_data['year'])

        student.save()

        return JsonResponse({"success": True})

    return HttpResponseBadRequest("Bad Request")

def get_student_modules_api(request, student_id):
    student = get_object_or_404(Student, student_number=student_id)
    return JsonResponse({
        'modules': [
            student.get_modules()
        ]
    })

def students_api(request):
    return JsonResponse({
        'students': [
            student.to_dict()
            for student in Student.objects.all()
        ]
    })

def modules_api(request):
    return JsonResponse({
        'modules': [
            module.to_dict()
            for module in Module.objects.all()
        ]
    })