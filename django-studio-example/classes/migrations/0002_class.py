# Generated by Django 4.0.1 on 2022-01-11 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('time', models.CharField(blank=True, max_length=10, null=True)),
                ('length', models.IntegerField(blank=True, null=True)),
                ('teacher', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
