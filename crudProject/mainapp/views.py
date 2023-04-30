from django.shortcuts import render,redirect
from mainapp.models import student_model
from mainapp.forms import student_form
from django.http import HttpResponse




# Create your views here.
def index_view(request):
    return render(request,'index.html')



def table_view(request):
    data=student_model.objects.all()
    return render(request,'info.html',{'data':data})





def form_view(request):
    form=student_form()
    if request.method =='POST':
        form=student_form(request.POST)
        if form.is_valid():
            form.save()#commit=True
            return render(request,'index.html')
    return render(request,'form.html',{'form':form})


def delete_view(request,id):
    student=student_model.objects.get(id=id)
    student.delete()
    return redirect('/')
   


def update_view(request,id):
    student=student_model.objects.get(id=id)
    form=student_form(instance=student)
    if request.method == 'POST':
        form=student_form(request.POST,instance=student)
        if form.is_valid():
            form.save()
            return redirect('/info')
    return render(request,'update.html',{'form':form})
