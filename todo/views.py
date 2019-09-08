from django.shortcuts import render

from .models import Todo
from .forms import TodoForm

# Create your views here.
def index(request):
	todo_all = Todo.objects.order_by('id')
	form  =  TodoForm()
	context = {'todo_list' : todo_all,'form':form}

	return render(request,'todo/index.html',context)