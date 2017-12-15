# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Course
from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    context = {
        'course': Course.objects.all()
    }
    return render(request, 'courseApp/index.html', context)

def markForDel(request, course_id):
    context={
    'course': Course.objects.get(id=course_id)
    }
    return redirect(request, 'courseApp/destroy.html')

def destroyCourse(request, course_id):
    Course.objects.get(id=course_id).delete()
    return redirect(request, 'courseApp/')

def addCourse(request):
    errors = Course.objects.validate(request.POST)
    if len(errors):
        for field, message in errors.iteritems():
            error(request, message, extra_tags=field)
        return redirect(request, '  courseApp/')
    