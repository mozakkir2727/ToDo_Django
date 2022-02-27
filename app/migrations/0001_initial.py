# Generated by Django 4.0.2 on 2022-02-27 08:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DO',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(default='', max_length=2000)),
                ('priority', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=200)),
                ('due_date', models.DateField(default=django.utils.timezone.now)),
                ('username', models.CharField(max_length=100)),
            ],
        ),
    ]