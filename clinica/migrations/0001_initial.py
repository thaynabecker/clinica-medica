# Generated by Django 5.2.3 on 2025-06-23 14:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataConsulta', models.DateField()),
                ('tipoConsulta', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Especialidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('dataNascimento', models.DateField()),
                ('cpf', models.CharField(max_length=15)),
                ('sexo', models.CharField(max_length=9)),
                ('telefone', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Exame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipoExame', models.CharField(max_length=45)),
                ('dataExame', models.DateField()),
                ('descricaoExame', models.TextField()),
                ('consultaExame', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='clinica.consulta')),
            ],
        ),
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('formacao', models.CharField(max_length=150)),
                ('telefone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=200)),
                ('crm', models.CharField(max_length=10)),
                ('especialidades', models.ManyToManyField(to='clinica.especialidade')),
            ],
        ),
        migrations.AddField(
            model_name='consulta',
            name='medicoConsulta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='clinica.medico'),
        ),
        migrations.AddField(
            model_name='consulta',
            name='pacienteConsulta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='clinica.paciente'),
        ),
        migrations.CreateModel(
            name='Receita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataReceita', models.DateField()),
                ('descricaoReceita', models.CharField(max_length=450)),
                ('consultaReceita', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='clinica.consulta')),
            ],
        ),
        migrations.CreateModel(
            name='Medicamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('dosagem', models.CharField(max_length=15)),
                ('receitaMedicamento', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='clinica.receita')),
            ],
        ),
        migrations.CreateModel(
            name='ReceitaMedicamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.TextField()),
                ('quantidade', models.IntegerField()),
                ('medicamento', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='clinica.medicamento')),
            ],
        ),
    ]
