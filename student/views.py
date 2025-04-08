from django.shortcuts import render, redirect
from app.models import StudentModel

def home(request):
    if request.method == 'POST':
        nm = request.POST.get('name')
        ag = request.POST.get('age')
        fs = request.POST.get('fees')
        record = StudentModel(name=nm, age=ag, fees=fs)
        record.save()
    data = StudentModel.objects.all()
    return render(request, "index.html", {'data': data})

def delete(request, id):
    data = StudentModel.objects.get(pk = id)
    data.delete()
    return redirect('/')

def update(request, id):
    data = StudentModel.objects.get(pk = id)
    if request.method == 'POST':
        nm = request.POST.get('name')
        ag = request.POST.get('age')
        fs = request.POST.get('fees')
        record = StudentModel(pk=id, name=nm, age=ag, fees=fs)
        record.save()
        data = {}
    return render(request, "update.html", {'data': data})