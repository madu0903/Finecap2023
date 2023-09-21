from django.shortcuts import render, get_object_or_404, redirect
from .models import Reserva
from .forms import ReservaForm    

# def reserva_listar(request):
#     reservas = Reserva.objects.all().order_by('data')
#     context = {
#         'reservas': reservas
#     }
#     return render(request, 'cadastro/index.html', context)

def reserva_listar(request):
    reservas = Reserva.objects.all().order_by('data')
    if(request.GET.get('nome_empresa')):
        reservas = reservas.filter(nome_empresa__contains=request.GET.get('nome_empresa'))
    if(request.GET.get('quitado')):
        reservas = reservas.filter(quitado=True)
    if(request.GET.get('valor')):
        reservas = reservas.filter(stand__valor=request.GET.get('valor'))
    if(request.GET.get('data')):
        reservas = reservas.filter(data__date=request.GET.get('data'))
    context ={
        'reservas':reservas
    }
    return render(request, "cadastro/index.html",context)

def reserva_remover(request, id):
    produto = get_object_or_404(Reserva, id = id)
    produto.delete()
    return redirect('index')

def reserva_criar(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            print(form.errors)
    else:
        form = ReservaForm()

    return render(request, 'cadastro/form.html', {'form': form})

def reserva_detalhar(request,id):
    reserva = get_object_or_404(Reserva, id=id)
    context={
        'reserva' : reserva,
    }
    return render(request,'cadastro/detalhe.html',context)



