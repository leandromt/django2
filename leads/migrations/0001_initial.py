# Generated by Django 3.0.2 on 2020-01-25 04:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Operadora',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255, verbose_name='Nome')),
            ],
            options={
                'verbose_name': 'Operadora',
            },
        ),
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
            ],
            options={
                'verbose_name': 'Tipo',
            },
        ),
        migrations.CreateModel(
            name='Lead',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255, verbose_name='Nome')),
                ('email', models.CharField(max_length=255, verbose_name='Email')),
                ('vidas', models.IntegerField(verbose_name='Quantidade de vida')),
                ('operadora', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='leads.Operadora', verbose_name='Operadora')),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='leads.Tipo', verbose_name='Tipo')),
            ],
            options={
                'verbose_name': 'Lead',
            },
        ),
    ]
