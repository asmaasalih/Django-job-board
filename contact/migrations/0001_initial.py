# Generated by Django 4.0.3 on 2022-05-14 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=50)),
                ('phone_number', models.IntegerField(max_length=20)),
                ('emai', models.EmailField(max_length=50)),
            ],
        ),
    ]
