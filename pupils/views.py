from django.shortcuts import render, get_object_or_404
from .models import Pupil, Grade


def pupil_list(request):
    pupils = Pupil.objects.all()
    return render(request, 'Pupils/pupil_list.html', {'pupils': pupils})


def pupil_detail(request, pk):
    pupil = get_object_or_404(Pupil, pk=pk)
    grades = Grade.objects.filter(pupil=pupil).order_by('-date')
    return render(request, 'Pupils/pupil_detail.html', {'pupil': pupil, 'grades': grades})



