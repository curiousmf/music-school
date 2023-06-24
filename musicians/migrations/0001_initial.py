# Generated by Django 4.2.1 on 2023-06-24 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('surname', models.CharField(max_length=30)),
                ('age', models.PositiveIntegerField()),
                ('course', models.CharField(max_length=30)),
                ('instrument', models.CharField(choices=[('g', 'Гитара'), ('v', 'Скрипка'), ('p', 'Пианино'), ('d', 'Барабан')], max_length=30)),
                ('progress', models.IntegerField()),
                ('payment', models.BooleanField()),
            ],
        ),
    ]