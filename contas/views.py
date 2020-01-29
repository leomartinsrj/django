from django.shortcuts import render, redirect
from .models import Transacao
from .form import TransacaoForm
from .models import Document
from .form import DocumentForm

# Create your views here.
from django.http import HttpResponse
import datetime
def home(request):
    now = datetime.datetime.now()
    html = "<html><body> It is now %s.</body></html>" % now
    data = {}
    data['now'] = now
    data['transacoes'] = ['t1','t2','t3']
    return render(request,'contas/home.html', data)

   # return HttpResponse(html)
def listagem(request):
    data = {}
    data['transacoes'] = Transacao.objects.all()
    return render(request, 'contas/listagem.html', data)

def nova_transacao(request):
    data = {}
    form = TransacaoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('url_listagem')
    data['form'] = form
    return render(request, 'contas/form.html', data)
def update(request, pk):
    data = {}
    transacao = Transacao.objects.get(pk=pk)
    form = TransacaoForm(request.POST or None, instance=transacao)
    if form.is_valid():
        form.save()
        return redirect('url_listagem')
    data['form'] = form
    return render(request, 'contas/form.html', data)

def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('url_home')
    else:
        form = DocumentForm()
    return render(request, 'contas/model_form_upload.html', {
        'form': form
    })
def base(request):
    return render(request, 'contas/base.html')