from django.shortcuts import get_object_or_404, redirect, render
from .models import Item
from .forms import ItemForm


def get_todo_list(request):
    """render todo list"""
    items = Item.objects.all()
    context = {
        "items": items
    }
    return render(request, "todo/todo_list.html", context)


def add_item(request):
    """render todo list"""
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("get_todo_list")

    form = ItemForm()
    context = {
        "form": form
    }

    return render(request, "todo/add_item.html", context)


def edit_item(request, item_id):
    """render edit item"""
    item = get_object_or_404(Item, id=item_id)
    if request.method == "POST":
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
        return redirect("get_todo_list")

    form = ItemForm(instance=item)
    context = {
        "form": form
    }
    return render(request, "todo/edit_item.html", context)


def toggle_item(request, item_id):
    """toggle done status"""
    item = get_object_or_404(Item, id=item_id)
    item.done = not item.done
    item.save()
    return redirect("get_todo_list")


def delete_item(request, item_id):
    """delete item"""
    item = get_object_or_404(Item, id=item_id)
    item.delete()
    return redirect("get_todo_list")
