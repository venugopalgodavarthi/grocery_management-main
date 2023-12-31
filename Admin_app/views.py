from django.shortcuts import render, redirect
from admin_app.models import category_items, product_item
from admin_app.forms import product_form, category_form
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.

#   ============ CATEGORY Register, List, Update, Delete


def category_register_view(request):
    form = category_form()
    if request.method == 'POST' and request.FILES:
        form = category_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Category is added.")
        else:
            messages.error(request, "Category is not added.")
    return render(request=request, template_name='category_register.html', context={'form': form})


def category_list_view(request):
    res = category_items.objects.all()
    return render(request=request, template_name='category_list.html', context={'data': res})


def category_update_view(request, pk):
    res = category_items.objects.get(cat_id=pk)
    form = category_form(instance=res)
    if request.method == 'POST' or request.FILES:
        res = category_items.objects.get(cat_id=pk)
        form = category_form(request.POST, request.FILES, instance=res)
        if form.is_valid():
            form.save()
            messages.success(request, "Category is Updated.")
        else:
            messages.error(request, "Category is not Updated.")
    return render(request=request, template_name='category_update.html', context={'data': form, 'res': res})


def category_delete_view(request, pk):
    res = category_items.objects.get(cat_id=pk)
    if request.method == 'POST':
        if category_items.objects.get(cat_id=pk).delete():
            messages.success(request, "Category Deleted")
        else:
            messages.error(request, "Category is not Deleted")
        return redirect('/admin_app/category_list')
    return render(request=request, template_name='category_delete.html', context={'data': res})


#   ============ (item) PRODUCT Register, List, Update, Delete
def item_register_view(request):
    form = product_form()
    if request.method == 'POST' and request.FILES:
        form = product_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Product added")
        else:
            messages.error(request, "Product is not added")
        return redirect('/admin_app/p_list/')
    return render(request=request, template_name='item_register.html', context={'form': form})


def item_list_view(request):
    category = category_items.objects.all()
    res = product_item.objects.all()
    return render(request=request, template_name='item_list.html', context={'data': res, 'category': category})


def item_details_view(request):
    if request.method == 'POST':
        res = product_item.objects.filter(cat_id=request.POST['cat_list'])
    return render(request=request, template_name='item_list.html', context={'data': res})


def item_update_view(request, pk):
    res = product_item.objects.get(item_id=pk)
    form = product_form(instance=res)
    if request.method == "POST":
        res = product_item.objects.get(item_id=pk)
        form = product_form(request.POST, request.FILES, instance=res)
        if form.is_valid():
            form.save()
            messages.success(request, "Product Updated")
        else:
            messages.error(request, "Product is not Updated")
        return redirect('/admin_app/p_list')
    return render(request=request, template_name='item_update.html', context={'form': form, 'res': res})


def item_delete_view(request, pk):
    res = product_item.objects.get(item_id=pk)
    if request.method == 'POST':
        if product_item.objects.get(item_id=pk).delete():
            messages.success(request, "Product Deleted")
        else:
            messages.error(request, "Product is not deleted")
        return redirect('/admin_app/p_list')
    return render(request=request, template_name='item_delete.html', context={'data': res})
