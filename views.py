from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound
from .models import Customers

def index(request):
    return render(request, 'index.html')


def index_wrapper(request):
    return render(request, 'hello/mypage.html')
# Create your views here.

# получение данных из бд
def mypage(request):
    customers = Customers.objects.all()
    return render(request, "mypage.html", {"customers": customers})


# сохранение данных в бд
def create(request):
    if request.method == "POST":
        customer = Customers()
        customer.first_name = request.POST.get('first_name', '')
        customer.last_name = request.POST.get('last_name', '')
        customer.address = request.POST.get('address', "")
        customer.phone_number = request.POST.get('phone_number', '')
        customer.save()
    return HttpResponseRedirect("/")


# изменение данных в бд
def edit(request, id):
    try:
        customer = Customers.objects.get(id=id)

        if request.method == "POST":
            customer.first_name = request.POST.get("first_name")
            customer.last_name = request.POST.get("last_name")
            customer.address = request.POST.get("address")
            customer.phone_number = request.POST.get("phone_number")
            customer.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "furnitures.html", {"customer": customer})
    except Customers.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")

def delete(request, id):
    try:
        customer = Customers.objects.get(id=id)
        customer.delete()
        return HttpResponseRedirect("/")
    except Customers.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")

def mypage(request):
    return render(request, 'mypage.html')

def furnitures(request):
    return render(request, 'furnitures.html')

def about(request):
    return render(request, 'about.html')
def about_wrapper(request):
    return render(request, 'hello/about.html')
def auth(request):
    return render(request, 'auth.html')
def uslugi(request):
    return render(request, 'uslugi.html')


