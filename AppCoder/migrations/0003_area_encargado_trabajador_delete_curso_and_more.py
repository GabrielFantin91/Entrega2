# Generated by Django 4.1.3 on 2022-12-02 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0002_entregable_remove_profesor_entregado_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('numero', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='encargado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='SOME STRING', max_length=30)),
                ('apellido', models.CharField(default='SOME STRING', max_length=30)),
                ('email', models.EmailField(default='SOME STRING', max_length=30)),
                ('profesion', models.CharField(default='SOME STRING', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='trabajador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='SOME STRING', max_length=30)),
                ('apellido', models.CharField(default='SOME STRING', max_length=30)),
            ],
        ),
        migrations.DeleteModel(
            name='curso',
        ),
        migrations.DeleteModel(
            name='entregable',
        ),
        migrations.DeleteModel(
            name='estudiante',
        ),
        migrations.DeleteModel(
            name='profesor',
        ),
    ]
