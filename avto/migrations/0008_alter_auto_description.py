# Generated by Django 5.0.6 on 2024-07-20 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avto', '0007_alter_auto_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auto',
            name='description',
            field=models.TextField(verbose_name='описание'),
        ),
    ]
