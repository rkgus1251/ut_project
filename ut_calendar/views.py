from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpRequest
import base.views

from .models import Date
from .forms import ScheduleForm


def index(request: HttpRequest):
    schedule_list = Date.objects.filter(user=request.user).order_by('-date')

    context = {'schedule_list': schedule_list}
    return render(request, 'schedule_list.html', context)


def detail(request: HttpRequest, date_id):
    date = get_object_or_404(Date, pk=date_id)
    date.user = request.user

    context = {
        'date': date,
    }
    return render(request, 'schedule_detail.html', context)


def schedule_create(request):
    if request.method == 'POST':
        form = ScheduleForm(request.POST)
        if form.is_valid():
            date = form.save(commit=False)
            date.user = request.user
            date.save()
            return redirect(base.views.index)
    else:
        form = ScheduleForm()
    context = {'form': form}
    return render(request, 'schedule_form.html', context)
