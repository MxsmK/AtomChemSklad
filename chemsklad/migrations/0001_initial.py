# Generated by Django 3.2.5 on 2021-07-28 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='React',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('qual', models.CharField(max_length=20)),
                ('date', models.DateField()),
                ('prov', models.CharField(max_length=20)),
                ('srok', models.DateField(null=True)),
            ],
        ),
    ]
