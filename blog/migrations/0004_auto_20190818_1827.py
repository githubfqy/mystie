# Generated by Django 2.2.4 on 2019-08-18 10:27

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20190818_1733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
