from django.db import models
from django.urls import reverse
from datetime import datetime

class Student(models.Model):
    ''' A model Student with fields: first name, surname, programme of study, year of study,
    student number and modules studying.

    Student number is a distinct field and module studying has a many to many relationship between
    Student and Module.
    '''
    first_name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    programme = models.CharField(max_length=255)
    year_of_study = models.IntegerField(max_length=1)
    student_number = models.CharField(max_length=9, unique=True)
    modules_studying = models.ManyToManyField('Module')
    enrolled = models.DateField(default=datetime.today())

    def __str__(self) -> str:
        '''The string representation of this object will be the full name of the Student'''
        return f'{self.first_name} {self.surname}'

    def to_dict(self):
        '''Allows the model to be returned as a dictionary which makes it easier 
        when retrieving data from the front end'''

        return {
            'id': self.student_number,
            'name': f'{self.first_name} {self.surname}',
            'programme': self.programme,
            'year_of_study': self.year_of_study,
            'api': reverse('student api', kwargs={'student_id': self.student_number}),
            'modules_api': reverse('get student modules api', kwargs={'student_id': self.student_number}),
            'delete_modules_api': reverse('student modules api', kwargs={'student_id': self.student_number}),
            'date': self.enrolled,
            'modules': self.get_modules()
        }

    def get_modules(self):
        return [
            module.to_dict()
            for module in self.modules_studying.all()
        ]


class Module(models.Model):
    ''' A model Module with fields: module code, module name, level and credits.

    Module code is a distinct field.
    '''
    module_code = models.CharField(max_length=7, unique=True)
    module_name = models.CharField(max_length=255)
    level = models.IntegerField(max_length=1)
    credits = models.IntegerField(max_length=2)
    created = models.DateField(default=datetime.today())

    def __str__(self) -> str:
        '''The string representation of this object will be the module code followed by the 
        module name'''
        return f'{self.module_code} - {self.module_name}'


    def to_dict(self):
        '''Allows the model to be returned as a dictionary which makes it easier 
        when retrieving data from the front end'''

        return {
            'id': self.module_code,
            'name': self.module_name,
            'level': self.level,
            'credits': self.credits,
            'api': reverse("module api", kwargs={'id': self.module_code}),
            'date': self.created,
        }