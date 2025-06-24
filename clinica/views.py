from rest_framework.viewsets import ModelViewSet
from .models import Consulta, Exame, Especialidade, Medicamento, Medico, Paciente, Receita, ReceitaMedicamento
from .serializers import ConsultaSerializer, ExameSerializer, EspecialidadeSerializer, MedicamentoSerializer, MedicoSerializer, PacienteSerializer, ReceitaSerializer, ReceitaMedicamentoSerializer

class ConsultaViewSet(ModelViewSet):
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer

class ExameViewSet(ModelViewSet):
    queryset = Exame.objects.all()
    serializer_class = ExameSerializer

class EspecialidadeViewSet(ModelViewSet):
    queryset = Especialidade.objects.all()
    serializer_class = EspecialidadeSerializer

class MedicamentoViewSet(ModelViewSet):
    queryset = Medicamento.objects.all()
    serializer_class = MedicamentoSerializer

class MedicoViewSet(ModelViewSet):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer

class PacienteViewSet(ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

class ReceitaViewSet(ModelViewSet):
    queryset = Receita.objects.all()
    serializer_class = ReceitaSerializer

class ReceitaMedicamentoViewSet(ModelViewSet):
    queryset = ReceitaMedicamento.objects.all()
    serializer_class = ReceitaMedicamentoSerializer