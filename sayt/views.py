from django.shortcuts import render, redirect
from .models import Ekologiya, Category, Menyu, Katalog, News
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreationForm, NewsForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

menyu = Menyu.objects.all()

def logout_user(request):
    logout(request)
    messages.info(request,'Siz tizimdan chiqdingiz')
    return redirect('login')
def register_user(request):
    form = CustomUserCreationForm()
    contex = {
        'form': form
    }
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request,user)
            messages.success(request,"Tizimga xush kelibsiz")
            return redirect('home')
        else:
            print("Foydanaluvchi ro'yxatdan o'tmadi")
    return render(request,'users/register.html',contex)

def login_user(request):
    if request.user.is_authenticated:
        return redirect('home')
        messages.success(request,"Tizimga xush kelibsiz")
    if request.method =="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            print('Bunday login va parol mavjud emas')

    return render(request,"users/login.html")

def addpage(request):
    menyu = Menyu.objects.all()
    return render(request, 'sayt/addpage.html',
                  {'title': 'Yangiliklarni kiritish', 'category': 'category', 'menyu': menyu})


def index(request):
    news = News.objects.all().order_by('-created_at')
    category = Category.objects.all()
    context={
        'news': news,
        'title': 'Asosiy sahifa',
        'category': category,
        'menyu': menyu
    }
    return render(request, 'sayt/index.html', context=context)

@login_required(login_url='login')
def news(request):
    newsa = News.objects.all().order_by('-created_at')
    page = request.GET.get('page')
    num_of_items = 3
    paginator = Paginator(newsa, num_of_items)
    try:
        newsa = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        newsa = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        newsa = paginator.page(page)
        pagen = 'paginator.page_range'

    context = {
        'news': newsa,
        'title': 'Asosiy sahifa',
        'menyu': menyu,
        'paginator': paginator,


    }
    return render(request, 'sayt/news.html', context=context)


@login_required(login_url='login')
def registr(request):

    reg = Katalog.objects.all().order_by('soato')
    context={
        'ekologiya':reg,
        'title':'Registr bo\'limi'
    }
    return render(request, 'sayt/reg.html',context=context)

def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    categories = Category.objects.all()
    categorys = Category.objects.get(pk=category_id)
    title = categorys.title + " - yangiliklari sahifasi"
    context = {
        'news': news,
        'categories': categories,
        'categorys': categorys,
        'menyu': menyu,
        'title': title,
    }
    return render(request, template_name='sayt/category.html', context=context,)
def view_news(request, news_id):
    news_item = News.objects.get(pk=news_id)
    return render(request, 'sayt/view_news.html', {'news_item': news_item })

def add_news(request):
    if request.method == 'POST':
        form=NewsForm(request.POST)
        if form.is_valid():
            news = form.save()
            return redirect(news)
    else:
        form = NewsForm()
    return render(request, 'sayt/add_news.html', {'form':form})
