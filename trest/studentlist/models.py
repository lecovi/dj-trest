from django.db import models
from django.utils import timezone


class DocType(models.Model):
    doc_type = models.CharField(max_length=50)

    def __str__(self):
        return self.doc_type


class Student(models.Model):
    name = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    doc_type = models.ForeignKey(DocType, on_delete=models.CASCADE)
    doc_number = models.IntegerField()
    email = models.EmailField()
    created_on = models.DateTimeField('created on', auto_now_add=True)
    updated_on = models.DateTimeField('updated on', default=timezone.now)

    def __str__(self):
        return '{}, {} <{}>'.format(self.lastname, self.name, self.email)

