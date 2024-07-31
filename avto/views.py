
from django.http import Http404
from django.shortcuts import render, get_object_or_404,redirect
from avto.models import Auto, Body
from django.core.paginator import Paginator
from django.http import HttpResponse
from .forms import PostForm

def index(request):
    auto = Auto.objects.filter(is_published=True)

    search = request.GET.get('search')
    
    if search:
        auto = auto.filter(title__icontains=search)

    Body = (request.GET.get('body', ''))

    if Body:
        auto = auto.filter(car_body__id=Body)

    page = int(request.GET.get('page', 1))
    page_size = int(request.GET.get('page_size', 3))
 
    pagin = Paginator(auto, page_size)
    auto = pagin.get_page(page) 

    return render(request, 'index.html', {'auto': auto})

def details_auto(request, id):
    # auto = Auto.objects.all()
    try:
        auto = Auto.objects.get(id=id, is_published=True)
    except Auto.DoesNotExist as e:
        raise Http404

    return render(request, 'details_auto.html', {'auto': auto})


  
from django.shortcuts import render, redirect
from avto.forms import PostForm
from avto.models import Auto
def delete_post(request, id):
    pradact = get_object_or_404(Auto, id=id)
    pradact.delete()
    return redirect('/auto/')

def blog_post(request,):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES) 
        if form.is_valid():
            form.save()
            return redirect('/auto/')
    else:
        form = PostForm()

    return render(request, 'blog_post.html', {'form': form})


def edit_post(request, id):
    auto = get_object_or_404(Auto, id=id)
    
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=auto)
        if form.is_valid():
            form.save()
            return redirect('/auto/') 
    else:
        form = PostForm(instance=auto)
    
    return render(request, 'edit_post.html', {'form': form, 'auto': auto})