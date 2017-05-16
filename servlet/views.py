from django.shortcuts import render
from django.views import View
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, FormView
from django.views.generic.list import ListView
from .models import Pessoa

def logoff(request):
    if 'nome' in request.session:
        del request.session['nome']
    return redirect("/servlet2")

class Servlet2View(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'servlet2.html')

    def post(self, request, *args, **kwargs):
        nome = request.POST.get('nome')
        idade = request.POST.get('idade')
        if idade != '' and int(idade) >= 18:
            return render(request, 'welcome.html', {'nome': nome, 'page_title': 'Seja bem-vindo'})
        else:
            return redirect('http://www.disney.com')

class Servlet3View(View):
    template_name = 'servlet3.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        nome = request.POST.get('nome')
        senha = request.POST.get('senha')
        if nome == '' or senha == '':
            return render(request, self.template_name, {'message': 'Preencha os dados'})
        elif nome == 'user' and senha == '123':
            return render(request, 'welcome.html', {'nome': nome, 'page_title': 'Seja bem-vindo'})
        else:
            return render(request, self.template_name, {'message': 'Nome e senha incorreta'})

class Servlet5View(View):
    template_name = 'servlet3.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'nome': request.session.get('nome', None)})

    def post(self, request, *args, **kwargs):
        nome = request.POST.get('nome')
        senha = request.POST.get('senha')
        if nome == '' or senha == '':
            return render(request, self.template_name, {'message': 'Preencha os dados'})
        elif nome == 'user' and senha == '123':
            request.session.set_expiry(60)
            request.session['nome'] = nome
            return render(request, 'welcome.html', {'nome': nome, 'page_title': 'Seja bem-vindo'})
        else:
            return render(request, self.template_name, {'message': 'Nome e senha incorreta'})

class Servlet6View(CreateView):
    model = Pessoa
    template_name = 'servlet6.html'
    fields = ['nome', 'email', 'idade']
    success_url = '/servlet7'

class Servlet7View(ListView):
    model = Pessoa
    template_name = 'servlet7.html'
