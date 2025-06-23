from rest_framework.serializers import ModelSerializer
from .models import Consulta, Especialidade, Exame, Medicamento, Medico, Paciente, Receita, ReceitaMedicamento

class ConsultaSerializer(ModelSerializer):
    class Meta:
        model = Consulta
        fields = '__all__'
    
class EspecialidadeSerializer(ModelSerializer):
    class Meta:
        model = Especialidade
        fields = '__all__'

class ExameSerializer(ModelSerializer):
    class Meta:
        model = Exame
        fields = '__all__'


class MedicamentoSerializer(ModelSerializer):
    class Meta:
        model = Medicamento
        fields = '__all__'

class MedicoSerializer(ModelSerializer):
    class Meta:
        model = Medico
        fields = '__all__'

class PacienteSerializer(ModelSerializer):
    class Meta:
        model = Paciente
        fields = '__all__'

class ReceitaSerializer(ModelSerializer):
    class Meta:
        model = Receita
        fields = '__all__'

class ReceitaMedicamentoSerializer(ModelSerializer):
    class Meta:
        model = ReceitaMedicamento
        fields = '__all__'
