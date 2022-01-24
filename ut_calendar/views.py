from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

import base.views
from .models import Date
from .forms import ScheduleForm
from base.views import index


def index(request) :
    schedule_list = Date.objects.order_by('-date')
    context = {'schedule_list': schedule_list}
    return render(request, 'schedule_list.html', context)


def detail(request, date_id) :
    date = get_object_or_404(Date, pk=date_id)
    context = {'date' : date}
    return render(request, 'schedule_detail.html', context)


def schedule_create(request) :
    if request.method == 'POST' :
        form = ScheduleForm(request.POST)
        if form.is_valid() :
            date = form.save(commit=False)
            date.save()
            return redirect(base.views.index)
    else :
        form = ScheduleForm()
    context = {'form' : form}
    return render(request, 'schedule_form.html', context)


def ex(request) :
    return render(request, 'calendar.html')