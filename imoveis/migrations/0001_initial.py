# Generated by Django 3.0.7 on 2020-07-06 20:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Imoveis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome do Imóvel')),
                ('slug', models.SlugField(unique=True)),
                ('tipo', models.CharField(choices=[('Apartamento', 'Apartamento'), ('Casa', 'Casa'), ('Sobrado', 'Sobrado'), ('Kitnet', 'Kitnet'), ('Terreno', 'Terreno')], default='', max_length=100, verbose_name='Tipo')),
                ('areaP', models.CharField(default='0', max_length=10, verbose_name='Área Privativa')),
                ('areaT', models.CharField(default='0', max_length=10, verbose_name='Área Total')),
                ('endereco', models.CharField(default='', max_length=100, verbose_name='Endereço')),
                ('num', models.IntegerField(default=0, verbose_name='Número')),
                ('bairro', models.CharField(choices=[('Centro', 'Centro'), ('Exposição', 'Exposição'), ('Desvio Rizzo', 'Desvio Rizzo'), ('Cristo Redentor', 'Cristo Redentor'), ('Panazzolo', 'Panazzolo')], default='', max_length=100)),
                ('preco', models.IntegerField(default=0, verbose_name='Preço')),
                ('desc', models.TextField(verbose_name='Descrição')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('itens', multiselectfield.db.fields.MultiSelectField(choices=[('Churrasqueira', 'Churrasqueira'), ('Piscina', 'Piscina'), ('Playground', 'Playground'), ('Academia', 'Academia'), ('Bosque', 'Bosque'), ('Jardim', 'Jardim')], max_length=55)),
                ('quartos', models.IntegerField(default=0)),
                ('banheiros', models.IntegerField(default=0)),
                ('vagas', models.IntegerField(default=0, verbose_name='Vagas de Garagem')),
                ('thumb', models.ImageField(blank=True, default='default.jpg', upload_to='imoveis', verbose_name='Capa')),
                ('image_list', models.CharField(blank=True, default='', max_length=400, verbose_name='Fotos')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Imóveis',
            },
        ),
        migrations.CreateModel(
            name='ImoveisImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, default='default.png', upload_to='imoveis', verbose_name='Fotos')),
                ('imovel', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='imoveis.Imoveis')),
            ],
            options={
                'verbose_name_plural': 'Imagens (Imóveis)',
            },
        ),
    ]
