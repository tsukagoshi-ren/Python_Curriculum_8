from django.shortcuts import render, redirect
from .forms import TodoSearchForm
import requests

def index(request):
    return render(request, 'todos/index.html')


def todo_list(request):
    url = 'https://jsonplaceholder.typicode.com/todos'#接続先のapiのパスを指定
    if request.method == 'GET':
        form = TodoSearchForm(request.GET)
        if form.is_valid():
            user_id = form.cleaned_data['user_id']
            param = { 'userId':user_id }
            response = requests.get(url,params = param)
            response.raise_for_status()

            todos = response.json()
            context = {
                'form': form,
                'todos': todos,
                'search_id': user_id,
            }
            return render(request, 'todos/todo_list.html', context)
        else:
            response = requests.get(url)
            response.raise_for_status()
            todos = response.json()
            context = {
                'form': form,
                'todos': todos,
            }
            return render(request, 'todos/todo_list.html', context)
    else:
        form = TodoSearchForm()
        context = {
                'form': form,
                'todos': [],
            }
        return render(request, 'todos/todo_list.html', context)
        
        