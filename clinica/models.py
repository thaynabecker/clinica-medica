from django.db import models

class Especialidade(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    def __str__(self):
        return f'{self.nome} - {self.descricao}.'

class Medico(models.Model):
    nome = models.CharField(max_length=50)
    formacao = models.CharField(max_length=150)
    telefone = models.CharField(max_length=15)
    email = models.EmailField(max_length=200)
    crm = models.CharField(max_length=10)
    especialidades = models.ManyToManyField(Especialidade)   
    def __str__(self):
        return f'Doutor {self.nome}, Formado em {self.formacao} \n Telefone: {self.telefone} \n Email: {self.email} \n Crm: {self.crm} \n Especialidades: {self.especialidades}.'

class Paciente(models.Model):
    nome = models.CharField(max_length=50)
    dataNascimento = models.DateField()
    cpf = models.CharField(max_length=15)
    sexo = models.CharField(max_length=9)
    telefone = models.CharField(max_length=15)   
    def __str__(self):
        return f'Paciente {self.nome}, Data de nascimento: \n {self.dataNascimento} \n CPF: {self.cpf} \n Sexo: {self.sexo} \n Telefone: {self.telefone}'

class Consulta(models.Model):
    dataConsulta = models.DateField()
    tipoConsulta = models.CharField(max_length=45)
    pacienteConsulta = models.ForeignKey(Paciente, on_delete=models.PROTECT)
    medicoConsulta = models.ForeignKey(Medico, on_delete=models.PROTECT) 
    def __str__(self):
        return f'Data da consulta: {self.dataConsulta} \n Tipo da consulta: {self.tipoConsulta} \n Paciente: {self.pacienteConsulta} \n  Médico: Dr. {self.medicoConsulta} '

class Receita(models.Model):
    dataReceita = models.DateField()
    descricaoReceita = models.CharField(max_length=450)
    consultaReceita = models.ForeignKey(Consulta, on_delete=models.PROTECT)
    def __str__(self):
        return f'Data da receita: {self.dataReceita} \n Descrição: {self.descricaoReceita} \n Receita feita na consulta: {self.consultaReceita}'

class Medicamento(models.Model):
    nome = models.CharField(max_length=50)
    dosagem = models.CharField(max_length=15)
    receitaMedicamento = models.ForeignKey(Receita, on_delete=models.PROTECT)   
    def __str__(self):
        return f'Medicamento: {self.nome} \n Dosagem: {self.dosagem}'

class ReceitaMedicamento(models.Model):
    medicamento = models.OneToOneField(Medicamento, on_delete=models.CASCADE)
    descricao = models.TextField()
    quantidade = models.IntegerField()
    def __str__(self):
        return f'Bula do medicamento: {self.medicamento} - {self.descricao}. \n Nesse medicamento contém {self.quantidade}'

class Exame(models.Model):
    tipoExame = models.CharField(max_length=45)
    dataExame = models.DateField()
    descricaoExame = models.TextField()
    consultaExame = models.ForeignKey(Consulta, on_delete=models.PROTECT)
    def __str__(self):
        return f'Data do exame: {self.dataExame} \n Tipo do exame: {self.tipoExame} \n - {self.descricaoExame} /n Exame agendado na consulta: {self.consultaExame}'