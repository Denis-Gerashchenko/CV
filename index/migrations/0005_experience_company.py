# Generated by Django 2.2.4 on 2019-08-10 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0004_experience_job_done'),
    ]

    operations = [
        migrations.AddField(
            model_name='experience',
            name='company',
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
    ]
