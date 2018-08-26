from django.db import models

class teachers(models.Model):
    teacher_name = models.CharField(max_length=200)
    location_id = models.IntegerField()
    subject_id = models.IntegerField()

class students(models.Model):
    student_name = models.CharField(max_length=200)
    location_id = models.IntegerField()
    subject_id = models.IntegerField()

class progress(models.Model):
    student_id = models.IntegerField()
    subject_id = models.IntegerField()
    date = models.DateField()
    type_classwork = models.BooleanField()
    type_homework = models.BooleanField()
    comments = models.CharField(max_length=200)
    hwd = models.IntegerField(default=0)
    teacher_id = models.IntegerField(default=0)

class location(models.Model):
    location_name = models.CharField(max_length=200)

class subject(models.Model):
    subject_name = models.CharField(max_length=200)