from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from clinica.views import ConsultaViewSet, EspecialidadeViewSet, ExameViewSet, MedicamentoViewSet, MedicoViewSet, PacienteViewSet, ReceitaViewSet, ReceitaMedicamentoViewSet

router = DefaultRouter()
router.register(r'consultas', ConsultaViewSet)
router.register(r'especialidades', EspecialidadeViewSet)
router.register(r'exames', ExameViewSet)
router.register(r'medicamentos', MedicamentoViewSet)
router.register(r'medicos', MedicoViewSet)
router.register(r'pacientes', PacienteViewSet)
router.register(r'receitas', ReceitaViewSet)
router.register(r'receitas-medicamentos', ReceitaMedicamentoViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
]