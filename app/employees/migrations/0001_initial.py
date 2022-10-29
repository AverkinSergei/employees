# Generated by Django 4.1.2 on 2022-10-28 14:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('departments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='name')),
            ],
            options={
                'verbose_name': 'position',
                'verbose_name_plural': 'positions',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.CharField(max_length=100, verbose_name='fio')),
                ('joined_date', models.DateField(verbose_name='joined_date')),
                ('salary', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='salary')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='staff', to='departments.department', verbose_name='department')),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='employees', to='employees.position', verbose_name='position')),
            ],
            options={
                'verbose_name': 'employee',
                'verbose_name_plural': 'employees',
            },
        ),
    ]
