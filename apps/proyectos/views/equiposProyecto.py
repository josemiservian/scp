# Django
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from django.core.paginator import Paginator

#Decoradores
from scp.decorators import allowed_users

#Modelos
from apps.proyectos.models import EquipoProyecto, MiembroEquipoProyecto

# Forms
from apps.proyectos.forms import FormCrearEquipo, FormAddMiembro, EquipoForm, MiembroForm

#Filtros
from apps.proyectos.filtros import EquipoProyectoFilter

# Create your views here.

class CrearEquipo(FormView):
    """ Vista de creacion de Clientes"""

    template_name = 'equiposProyecto/crear-equipo.html'
    form_class = FormCrearEquipo
    success_url = reverse_lazy('proyectos:squads-listar')

    def form_valid(self, form):
        """Save form data."""
        form.save()
        return super().form_valid(form)


class AddMiembro(FormView):
    """ Vista para añadir miembro al equipo"""

    template_name = 'equiposProyecto/add.html'
    form_class = FormAddMiembro
    success_url = reverse_lazy('proyectos:squads-integrantes')

    def form_valid(self, form):
        """Save form data."""
        form.save()
        return super().form_valid(form)


#FUNCIONES
@login_required(login_url='cuentas:login')
@allowed_users(action='add_miembroequipoproyecto')
def add_integrante(request, pk):
	
    MiembroFormSet = inlineformset_factory(
        EquipoProyecto, 
        MiembroEquipoProyecto,
        fields=('empleado','rol','tarifa_asignada'),
        can_delete=False,
        extra=5)
    equipo = EquipoProyecto.objects.get(id=pk)
    formset = MiembroFormSet(queryset=MiembroEquipoProyecto.objects.none(),instance=equipo)
    if request.method =='POST':
        formset = MiembroFormSet(request.POST, instance=equipo)
        if formset.is_valid():
            formset.save()
            #return listar_integrantes(request, pk)
            return redirect('proyectos:squads-listar')
    context = {'formset':formset}
    return render(request, 'equiposProyecto/add2.html', context)

@login_required(login_url='cuentas:login')
@allowed_users(action='view_miembroequipoproyecto')
def listar_integrantes(request, pk):

    integrantes = MiembroEquipoProyecto.objects.filter(equipo_proyecto=pk)
    return render(request, 'equiposProyecto/integrantes.html', {'integrantes':integrantes,'pk':pk})

@login_required(login_url='cuentas:login')
@allowed_users(action='delete_miembroequipoproyecto')
def borrar_integrante(request, pk):
	
    integrante = MiembroEquipoProyecto.objects.get(id=pk)

    if request.method == "POST":
        id_equipo = integrante.equipo_proyecto.id
        integrante.delete()
        return listar_integrantes(request, id_equipo)

    context = {'integrante':integrante}
    return render(request, 'equiposProyecto/borrar-integrante.html', context)

@login_required(login_url='cuentas:login')
@allowed_users(action='add_equipoproyecto')
def crear_equipo(request):

	form = FormCrearEquipo

	if request.method == 'POST':
		form = FormCrearEquipo(request.POST)
		if form.is_valid():
			form.save()
			return redirect('proyectos:squads-listar')

	context = {'form':form}
	return render(request, 'equiposProyecto/crear-equipo.html', context)

@login_required(login_url='cuentas:login')
@allowed_users(action='view_equipoproyecto')
def listar_equipos(request):

    equipos = EquipoProyecto.objects.all()

    filtros = EquipoProyectoFilter(request.GET, queryset=equipos)

    equipos = filtros.qs

    paginator = Paginator(equipos, 10)

    page = request.GET.get('page')

    equipos = paginator.get_page(page)

    return render(request, 'equiposProyecto/equipos.html', {'equipos':equipos, 'filtros':filtros})

@login_required(login_url='cuentas:login')
@allowed_users(action='change_equipoproyecto')
def actualizar_equipo(request, pk):

	equipo = EquipoProyecto.objects.get(id=pk)
    #miembros = MiembroEquipoProyecto.objects.get(equipo_proyecto=equipo.id)
	form = EquipoForm(instance=equipo)

	if request.method == 'POST':
		form = EquipoForm(request.POST, instance=equipo)
		if form.is_valid():
			form.save()
			return redirect('proyectos:squads-equipos')

	context = {'form':form}
	return render(request, 'equiposProyecto/modificar.html', context)


@login_required(login_url='cuentas:login')
@allowed_users(action='delete_equipoproyecto')
def borrar_equipo(request, pk):
	
    equipo = EquipoProyecto.objects.get(id=pk)
    if request.method == "POST":
        equipo.delete()
        return redirect('proyectos:squads-equipos')
        
    context = {'equipo':equipo}
    return render(request, 'equiposProyecto/borrar-equipo.html', context)


