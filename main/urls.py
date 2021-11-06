from django.urls import path

from main.views import (
    main_view
)

from main.api import *


urlpatterns = [
    path('', main_view),

    path('/api/students/', students_api, name="students api"),
    path('/api/student/', add_student_api, name="add student api"),
    path('/api/student/<str:student_id>', student_api, name="student api"),

    path('/api/student_modules/<str:student_id>', get_student_modules_api, name="get student modules api"),
    path('/api/student_module/<str:student_id>', student_modules_api, name="student modules api"),

    path('/api/modules/', modules_api, name="modules api"),
    path('/api/module', add_module_api, name="add module api"),
    path('/api/module/<str:id>', module_api, name="module api"),


]