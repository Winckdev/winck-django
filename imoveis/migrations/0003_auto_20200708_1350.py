# Generated by Django 3.0.7 on 2020-07-08 16:50

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('imoveis', '0002_auto_20200707_1620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imoveis',
            name='itens',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Churrasqueira', 'Churrasqueira'), ('Piscina', 'Piscina'), ('Playground', 'Playground'), ('Academia', 'Academia'), ('Bosque', 'Bosque'), ('Jardim', 'Jardim'), ('Ar condicionado', 'Ar condicionado'), ('Salão de festas', 'Salão de festas'), ('Medição de água individualizada', 'Medição de água individualizada')], max_length=119),
        ),
        migrations.AlterField(
            model_name='imoveis',
            name='preco',
            field=models.CharField(default='0', max_length=12, verbose_name='Preço'),
        ),
        migrations.AlterField(
            model_name='imoveis',
            name='thumb',
            field=models.ImageField(blank=True, default='e404.png', upload_to='imoveis', verbose_name='Capa'),
        ),
        migrations.AlterField(
            model_name='imoveisimage',
            name='image',
            field=models.ImageField(blank=True, default='e404.png', upload_to='imoveis', verbose_name='Fotos'),
        ),
    ]
