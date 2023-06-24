from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Cat, User
from .form import CatForm, RegistrationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView



def index(request):
    return render(request, 'base.html')


def home(request):
    return render(request, 'about/home.html', c)


def kinds(request):
    cats = Cat.objects.all()
    c = {"cats1": cats}
    return render(request, 'about/cat_album.html', c)


def new_cat(request):
    is_edit = False
    if request.method == 'POST':
        form = CatForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print('all right')
            return redirect('about:kinds')
        else:
            print('wrong!')
            HttpResponse(form.errors)
    else:
        form = CatForm()
    return render(request, 'about/form.html', {'form': form, 'is_edit': is_edit})


def edit_cat(request, cat_id):
    is_edit = True
    cat = get_object_or_404(Cat, id=cat_id)
    if request.method == 'POST':
        form = CatForm(request.POST, request.FILES, instance=cat)
        if form.is_valid():
            form.save()
            return redirect('about:cat_detail', cat_id=cat_id)
    else:
        form = CatForm(instance=cat)
    return render(request, 'about/form.html', {'form': form, 'cat': cat, 'is_edit': is_edit})


def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('about:profile')
    else:
        form = RegistrationForm()
    return render(request, 'about/reg_user.html', {'form': form})



@login_required()
def profile(request):
    user = request.user
    return render(request, 'about/profile.html', {'user': user})


class CustomLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'about/auth_user.html'


def card_of_cat(request, cat_id):
    cat = get_object_or_404(Cat, id=cat_id)
    return render(request, 'about/cat_detail.html', {'cat': cat})
