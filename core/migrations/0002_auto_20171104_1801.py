# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-04 20:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('nome', models.CharField(max_length=120, primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=80)),
                ('celular', models.CharField(max_length=11)),
                ('curso', models.ForeignKey(db_column='sigla_curso', on_delete=django.db.models.deletion.CASCADE, to='core.Curso')),
            ],
            options={
                'db_table': 'Aluno',
            },
        ),
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('nome', models.CharField(max_length=240, primary_key=True, serialize=False)),
                ('carga_horaria', models.SmallIntegerField()),
                ('teoria', models.DecimalField(decimal_places=2, max_digits=3)),
                ('pratica', models.DecimalField(decimal_places=2, max_digits=3)),
                ('ementa', models.TextField()),
                ('competencias', models.TextField()),
                ('habilidades', models.TextField()),
                ('conteudo', models.TextField()),
                ('bibliografia_complementar', models.TextField()),
                ('bibliografia_basica', models.TextField()),
            ],
            options={
                'db_table': 'Disciplina',
            },
        ),
        migrations.CreateModel(
            name='DisciplinaOfertada',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ano_grade', models.SmallIntegerField()),
                ('semestre', models.CharField(max_length=1)),
                ('disciplina', models.ForeignKey(db_column='nome_disicplina', on_delete=django.db.models.deletion.CASCADE, to='core.Disciplina')),
            ],
            options={
                'db_table': 'DisciplinaOfertada',
            },
        ),
        migrations.CreateModel(
            name='Periodo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ano_grade', models.SmallIntegerField()),
                ('semestre_grade', models.CharField(max_length=1)),
                ('numero', models.SmallIntegerField()),
            ],
            options={
                'db_table': 'Periodo',
            },
        ),
        migrations.CreateModel(
            name='PeriodoDisciplina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ano_grade', models.SmallIntegerField()),
                ('semestre_grade', models.CharField(max_length=1)),
                ('disciplina', models.ForeignKey(db_column='nome_disicplina', on_delete=django.db.models.deletion.CASCADE, to='core.Disciplina')),
                ('periodo', models.ForeignKey(db_column='numero_periodo', on_delete=django.db.models.deletion.CASCADE, to='core.Periodo')),
            ],
            options={
                'db_table': 'PeriodoDisciplina',
            },
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('ra', models.IntegerField(primary_key=True, serialize=False)),
                ('apelido', models.CharField(max_length=30, null=True, unique=True)),
                ('nome', models.CharField(max_length=120)),
                ('email', models.CharField(max_length=80)),
                ('celular', models.CharField(max_length=11)),
            ],
            options={
                'db_table': 'Professor',
            },
        ),
        migrations.CreateModel(
            name='Turma',
            fields=[
                ('ano_grade', models.SmallIntegerField()),
                ('turno', models.CharField(max_length=15)),
                ('id', models.CharField(max_length=1, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'Turma',
            },
        ),
        migrations.RenameField(
            model_name='gradecurricular',
            old_name='sigla_curso',
            new_name='curso',
        ),
        migrations.AlterUniqueTogether(
            name='gradecurricular',
            unique_together=set([('curso', 'ano', 'semestre')]),
        ),
        migrations.AddField(
            model_name='periodo',
            name='gradeCurricular',
            field=models.ForeignKey(db_column='sigla_curso', on_delete=django.db.models.deletion.CASCADE, to='core.GradeCurricular'),
        ),
        migrations.AlterUniqueTogether(
            name='periododisciplina',
            unique_together=set([('periodo', 'ano_grade', 'semestre_grade', 'periodo', 'disciplina')]),
        ),
        migrations.AlterUniqueTogether(
            name='periodo',
            unique_together=set([('gradeCurricular', 'ano_grade', 'semestre_grade', 'numero')]),
        ),
    ]