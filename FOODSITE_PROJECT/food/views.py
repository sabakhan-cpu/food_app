from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.template import loader
from . import forms
from . import models



from food.models import Item


# Create your views here.
def greet(resquest):
    return HttpResponse("This is DJango APp!")

def process(request):
    return HttpResponse("We are processing the request!")

def item(request):
    item_list=Item.objects.all()  #data
    # temp=loader.get_template('food/index.html')  #template
    context={
        'item_list': item_list
    }
    return render(request,'food/index.html',context)

def detail(request,item_id):
    item=Item.objects.get(pk=item_id)
    context={
        'item':item,
    }
    return render(request,'food/item_detail.html',context)

def add_item(request):
    form=forms.ItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("food:item")
    
    return render(request,'food/item_form.html',context={'form':form})

def update_item(request,id):
    item=Item.objects.get(id=id)
    form=forms.ItemForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect("food:item")
    
    return render(request,'food/item_form.html', context={'form':form,'item':item})

def delete_item(request,id):
    item=Item.objects.get(id=id)
    form=forms.ItemForm(request.POST or None,instance=item)

    if form.is_valid():
        form.save()
        return redirect("food:item")
    
    return render(request,'food/item_form.html', context={'form':form,'item':item})

   


