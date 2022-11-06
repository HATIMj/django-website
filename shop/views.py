from django.shortcuts import render, HttpResponse, redirect
from .forms import *
from time import time
from math import ceil
from .models import *
import json
# Create your views here.


def aindex(request):#it adds products
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("/success")
    else:
        form = ImageForm()

    return render(request, 'addpors.html', {'form': form})

def checkout(request):#for cart products pay
    if request.method == "POST":
        b1 = request.POST.get('joj', 'off')
        b2 = request.POST.get('jo', 'off')
        email = request.POST.get('emale')
        name = request.POST.get("naam")
        address = request.POST.get('pata')
        city = request.POST.get('shehar')
        state = request.POST.get('state')
        zip0 = request.POST.get('zip')
        items=request.POST.get('items')
        order_id=request.POST.get('iorder')
        order = Orders(approved=False,order_id=order_id,name=name , email=email,items=items,
                       address=address, city=city, state=state, zip_code=zip0)
        if b2=="on":
            order.approved=True
            order.save()
            return redirect("/orders")
        elif b1=="on":
            order.save()
            return render(request,'proof.html')
        
    return render(request,'chko.html')
def showproducts(request):#showing products on products page
    if request.method == "GET":
        images = Image.objects.all()
        n = len(images)
        k = n//4+ceil(n/4-n//4)

        return render(request, "product.html", {'shop_image': images, 'range': range(1, n)})
def orders(request):#orders and tracking system
    itemz=Orders.objects.filter(name='Jashandeep Singh9')
    s=[]    
    for i in itemz:
       m=json.loads(i.items)
       if type(m)==list:
          for i in m:
            s.append(i)
          s.append(1)
       else:    
          for j,k in m.items():
             s.append([k['name'],k['price']*k['q'],i.Tracker])
     
    return render(request,"orders.html",{'price':s})



def check(request, myid):#an individual product page
    imag = Image.objects.filter(id=myid)

    return render(request, "check.html", {'image': imag[0]})
def done(request):
    if request.method=="POST":
        return HttpResponse("jm")
    return render(request,'proof.html')


def pay(request, paid):
    imag = Image.objects.filter(id=paid)
    
    if request.method == "POST":
        b1 = request.POST.get('joj', 'off')
        b2 = request.POST.get('jo', 'off')
        email = request.POST.get('emale')
        name = request.POST.get("naam")
        address = request.POST.get('pata')
        city = request.POST.get('shehar')
        state = request.POST.get('state')
        zip0 = request.POST.get('zip')
        items = ["{0}".format(imag[0].name),imag[0].price]

        order = Orders(approved=False, name=name, items=items, email=email,
                       address=address, city=city, state=state, zip_code=zip0)

        if b1 == 'on':
            order.save()
            return render(request,'proof.html',{'image':imag[0]})
            

        if b2 == "on":
            order.approved = True
            order.save()
            return redirect("/orders")

    return render(request, "chko.html", {'image': imag[0]})
