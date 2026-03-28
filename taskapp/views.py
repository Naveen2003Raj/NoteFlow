from django.shortcuts import render, redirect,get_object_or_404
from .forms import Register
from django.contrib.auth.decorators import login_required
from .models import StickyNote,Todo
from django.contrib.auth import logout

def home(request):
    return render(request, 'home.html')


def register(request):
    form = Register(request.POST )  

    if request.method == 'POST':
        if form.is_valid():
            form.save()   
            return redirect('Login')

    return render(request, 'register.html', {"form": form})


def login(request):
    return render(request, "login.html")

def page(request):
    return render(request, 'profile.html')



# CREATE + READ
@login_required
def notes(request):
    if request.method == "POST":
        description = request.POST.get('description')

        if description:
            StickyNote.objects.create(
                user=request.user,
                description=description
            )
        return redirect('notes')

    notes = StickyNote.objects.filter(user=request.user).order_by('-id')
    return render(request, 'notes.html', {'notes': notes})


# UPDATE
@login_required
def edit_note(request, id):
    note = get_object_or_404(StickyNote, id=id, user=request.user)

    if request.method == "POST":
        note.description = request.POST.get('description')
        note.save()
        return redirect('notes')

    return render(request, 'edit_note.html', {'note': note})


# DELETE
@login_required
def delete_note(request, id):
    note = get_object_or_404(StickyNote, id=id, user=request.user)
    note.delete()
    return redirect('notes')
@login_required
def todo(request):
    if request.method == "POST":
        task = request.POST.get('task')
        status = request.POST.get('status')

        if task:
            Todo.objects.create(
                user=request.user,
                task=task,
                status=status
            )
        return redirect('todo')

    todos = Todo.objects.filter(user=request.user).order_by('-id')
    return render(request, 'todo.html', {'todos': todos})


# UPDATE
@login_required
def edit_todo(request, id):
    todo = get_object_or_404(Todo, id=id, user=request.user)

    if request.method == "POST":
        todo.task = request.POST.get('task')
        todo.status = request.POST.get('status')
        todo.save()
        return redirect('todo')

    return render(request, 'edit_todo.html', {'todo': todo})


# DELETE
@login_required
def delete_todo(request, id):
    todo = get_object_or_404(Todo, id=id, user=request.user)
    todo.delete()
    return redirect('todo')

def user_logout(request):
    logout(request)
    return redirect('Login')