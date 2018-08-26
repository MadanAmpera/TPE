from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader

from .models import students
from .models import progress
from .models import subject
from .models import teachers

def students_show(request):
    students_list = students.objects.all()
    template = loader.get_template('progress_app/students.html')
    context = {
        'students_list': students_list,
    }
    return render(request, 'progress_app/students.html', context)
def progress_view(request, student_id):
    try:
        student = students.objects.get(pk = student_id)
        progress_data = progress.objects.get(student_id = student_id)
        subject_data = subject.objects.get(pk = progress_data.subject_id)
        teacher_name = teachers.objects.get(pk=progress_data.teacher_id)
    except students.DoesNotExist:
        raise Http404("invalid student id")
    return render(request, 'progress_app/progress.html', {
        'student': student,
        'progress_data': progress_data,
        'subject_data':subject_data,
        'teacher_name':teacher_name
    })
