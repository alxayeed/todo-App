from django.shortcuts import render,redirect
from django.views.decorators.http import require_POST

from .models import Todo
from .forms import TodoForm

# Create your views here.
def index(request):
	todo_all = Todo.objects.order_by('id')
	form  =  TodoForm()
	context = {'todo_list' : todo_all,'form':form}

	return render(request,'todo/index.html',context)

@require_POST
def addTodo(request):
	form = TodoForm(request.POST)

	print(request.POST['text'])
	if form.is_valid():
		new_todo = Todo(text=request.POST['text'])
		new_todo.save()

	return redirect('index')

def todoComplete(request,todo_id):
	todo = Todo.objects.get(pk=todo_id)
	print(todo)
	todo.completed = True
	todo.save()

	return redirect('index')

def deleteCompleted(request):
	Todo.objects.filter(completed = True).delete()

	return redirect('index')
