from django.shortcuts import render, redirect
from .forms import TodoSearchForm
import requests

def todo_list(request):
    url = 'https://jsonplaceholder.typicode.com/todos'  # 接続先のapiのパスを指定
    form = TodoSearchForm(request.GET or None)
    todos = []
    search_id = None
    
    # GETリクエストの処理
    if request.method == 'GET':
        # フォームが有効かつuser_idが入力されている場合
        if form.is_valid() and form.cleaned_data.get('user_id'):
            user_id = form.cleaned_data['user_id']
            search_id = user_id
            param = {'userId': user_id}
            
            try:
                response = requests.get(url, params=param)
                response.raise_for_status()
                todos = response.json()
            except requests.exceptions.RequestException:
                # API通信エラーの場合
                todos = []
        
        # 初回アクセスまたは検索条件なしの場合は全件表示
        elif not request.GET or (form.is_valid() and not form.cleaned_data.get('user_id')):
            try:
                response = requests.get(url)
                response.raise_for_status()
                todos = response.json()
            except requests.exceptions.RequestException:
                # API通信エラーの場合
                todos = []
    
    context = {
        'form': form,
        'todos': todos,
        'search_id': search_id,
    }
    return render(request, 'todos/todo_list.html', context)