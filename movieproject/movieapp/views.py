
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import movie
from .forms import movieForm
# Create your views here.
def demo(request):
    result=movie.objects.all()
    context={
        'key':result
    }
    return render(request,"index.html",context)

def detail(request,movie_id):
    var=movie.objects.get(id=movie_id)
    return render(request,"detail.html",{'key':var})

def add(request):
    if request.method=='POST':
        name=request.POST.get('name')
        image=request.FILES['image']
        desc=request.POST.get('desc')
        year=request.POST.get('year')
        user=movie(name=name,image=image,desc=desc,year=year)
        user.save()
    return render(request,"add.html")
def update(request,id):
    Movie=movie.objects.get(id=id)
    form=movieForm(request.POST or None, request.FILES, instance=Movie)
    if form.is_valid():
        form.save()
        return redirect('/')

    return render(request,"update.html",{'form':form,'movie':Movie })
def delete(request,id):
    if request.method=='POST':
        movieVar=movie.objects.get(id=id)
        movieVar.delete()
        return redirect('/')
    return render(request,"delete.html")