# Generated by Django 4.0.5 on 2022-06-26 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Familiar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cedula_identidad', models.IntegerField()),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('fecha_nacimiento', models.DateField()),
            ],
        ),
    ]
