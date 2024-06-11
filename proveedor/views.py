from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Proveedor
from .forms import ProveedorForm

# Create your views here.
def index(request):
    proveedores = Proveedor.objects.all()
    print(proveedores)
    return render(
        request,
        'index.html',
        { 'proveedores': proveedores }
    )
    
def formulario(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST) # Aqui en el request.POST viene nombre, stock, categoria, imagen
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/proveedores')
    else:
        form = ProveedorForm()
    return render(
        request,
        'proveedor_form.html',
        {'form': form }
    )

def detail(request, proveedor_id):
    proveedor = get_object_or_404(proveedor, id=proveedor_id)
    return render(request, 'detail.html', context={'proveedor': proveedor})