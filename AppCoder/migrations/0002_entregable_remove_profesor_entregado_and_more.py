# Generated by Django 4.1.3 on 2022-12-01 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='entregable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('fecha_entrega', models.DateField()),
                ('entregado', models.BooleanField()),
            ],
        ),
        migrations.RemoveField(
            model_name='profesor',
            name='entregado',
        ),
        migrations.RemoveField(
            model_name='profesor',
            name='fecha_entrega',
        ),
        migrations.AddField(
            model_name='profesor',
            name='apellido',
            field=models.CharField(default='SOME STRING', max_length=30),
        ),
        migrations.AddField(
            model_name='profesor',
            name='email',
            field=models.EmailField(default='SOME STRING', max_length=30),
        ),
        migrations.AddField(
            model_name='profesor',
            name='profesion',
            field=models.CharField(default='SOME STRING', max_length=30),
        ),
        migrations.AlterField(
            model_name='profesor',
            name='nombre',
            field=models.CharField(max_length=30),
        ),
    ]
