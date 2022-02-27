from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import redirect, render
from.models import DO
# Create your views here.


def index(request):
    return render(request, 'index.html', {})


def display(request):
    print(request.POST)
    if request.method == "POST":
        username = request.POST["username"]
        title = request.POST["title"]
        description = request.POST["description"]
        priority = request.POST["priority"]
        category = request.POST["category"]
        due_date = request.POST["due_date"]
        print(username, title, description, priority, category, due_date)
        s = DO(username=username, title=title, description=description,
               priority=priority, category=category, due_date=due_date)
        s.save()
        data = DO.objects.all()
        return render(request, "show.html", {"data": data})
    else:
        data = DO.objects.all()
        return render(request, "show.html", {"data": data})


def mark(request, id):
    value = DO.objects.get(pk=id)
    value.status = True
    value.save()
    data = DO.objects.filter(status=False)
    return render(request, 'done.html', {'data': data})


def update(request, id):

    value = DO.objects.get(pk=id)
    if request.method == "POST":
        username = request.POST["username"]
        title = request.POST["title"]
        description = request.POST["description"]
        priority = request.POST["priority"]
        category = request.POST["category"]
        due_date = request.POST["due_date"]
        DO.objects.filter(id=id).update(username=username, title=title,
                                        description=description, priority=priority, category=category, due_date=due_date)
        data = DO.objects.all()
        return redirect("show")

    return render(request, 'update.html', {"value": value})


def delete(request, id):
    DO.objects.get(pk=id).delete()
    return redirect("show")


def update_done(request, id):
    todo = DO.objects.get(pk=id)
    todo.status = True
    todo.save()
    return redirect("show")
