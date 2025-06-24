from django.contrib import admin
from .models import Especialidade, Medico, Paciente, Consulta, Receita, Medicamento, ReceitaMedicamento, Exame

admin.site.register(Especialidade)
admin.site.register(Medico)
admin.site.register(Paciente)
admin.site.register(Consulta)
admin.site.register(Receita)
admin.site.register(Medicamento)
admin.site.register(ReceitaMedicamento)
admin.site.register(Exame)
