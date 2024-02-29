from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.views.generic.edit import  FormView

# Create your views here.


class CustomLoginView(LoginView):
    template_name = 'login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('index')
    

class RegisterPage(FormView):
    template_name = 'register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('index')
        return super(RegisterPage, self).get(*args, **kwargs)
    

def logout_view(request):
    logout(request)
    return redirect('index')


def index(request):
     context = {
         'title': 'Главная страница сайта' 
         }
     return render(request, 'index.html', context)


# Представления для работы с авторами 
def author_list(request):
    return render(request, 'author_list.html')


def display_authors(request):
    authors = Author.objects.all()

    context = {
        'authors': authors,
        'header': 'Автор' 
    }   

    return render(request, 'author_list.html', context)


def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('author_list')
    else:
        form = AuthorForm()
        context = {
            'form': form,
            'header': 'Автор'
        }   
        return render(request, 'add_author.html', context)


def author_detail(request, pk):
    author = get_object_or_404(Author, pk=pk)

    context = {
        'author': author,
    }

    return render(request, 'author_detail.html', context)



def edit_author(request, pk):
    author = get_object_or_404(Author, pk=pk)

    if request.method == 'POST':
        form = AuthorForm(request.POST, instance=author)

        if form.is_valid():
            form.save()
            return redirect('author_list')
    else:
        form = AuthorForm(instance=author)
    
    context = {
        'form': form,
        'header': 'Редактирование автора'
    }   
    return render(request, 'edit_author.html', context)


def delete_author(request, pk):
    author = get_object_or_404(Author, pk=pk)
    author.delete()
    return redirect("author_list")



# Представления для работы со статьями
def article_list(request):
    pass
def display_articles(request):
    pass
def add_article(request):
    pass
def article_detail(request):
    pass
def edit_article(request):
    pass
def delete_article(request):
    pass