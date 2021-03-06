from django.db.models.base import Model
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView

#formularios
from apps.consultas.forms import ConsulContForm
from apps.proyectos.models import Contrato

# vista del reporte
class ConsultaView(TemplateView):
    
    template_name = 'c_contratos/c_contrato.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'search_report':
                data = []
                start_date = request.POST.get('start_date', '')
                end_date = request.POST.get('end_date', '')
                search = Contrato.objects.all()
                if len(start_date) and len(end_date):
                  search = search.filter(fecha_inicio__range=[start_date, end_date])
                for s in search:
                    data.append([
                        #s.id,
                        s.nombre,
                        s.descripcion,
                        s.monto,
                        s.gastos,
                        s.horas_presupuestadas,
                        s.horas_ejecutadas,
                        s.fecha_inicio,
                        s.fecha_fin,
                        s.rentabilidad_horas,
                        s.rentabilidad_presupuesto,
                    ])
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Reporte de los Contratos'
        context['list_url'] = reverse_lazy('consultas:c_contrato')
        context['form'] = ConsulContForm()
        context['create_url'] = reverse_lazy('consultas:graficos')
        return context


