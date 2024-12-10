from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .models import Category
from .forms import PostForm, AuthorForm, CategoryForm, SearchForm
from django.http import HttpResponse

def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})

def create_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AuthorForm()
    return render(request, 'create_author.html', {'form': form})

def create_category(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        if name and description: 
            Category.objects.create(name=name, description=description)
            return redirect('home')  # Redirige al home o donde prefieras
        else:
            return HttpResponse("Invalid data", status=400)
    return render(request, 'create_category.html')

def search(request):
    form = SearchForm()
    results = None
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Post.objects.filter(title__icontains=query)
    return render(request, 'search_results.html', {'form': form, 'results': results})

def read_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'read_more.html', {'post': post})
