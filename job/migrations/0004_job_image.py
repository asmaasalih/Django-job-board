# Generated by Django 4.0.3 on 2022-03-28 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0003_category_job_experience_job_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='image',
            field=models.ImageField(default='', upload_to='media'),
            preserve_default=False,
        ),
    ]
