# Generated by Django 3.0.7 on 2020-07-07 19:07

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200707_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='body',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Corpo do texto'),
        ),
    ]
