from django.contrib import admin

from main.models import Student, Module

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['student_number', 'first_name', 'surname', 'programme', 'year_of_study']
    list_filter = ['programme', 'year_of_study']

@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ['module_code', 'module_name', 'level', 'credits']
    list_filter = ['level']