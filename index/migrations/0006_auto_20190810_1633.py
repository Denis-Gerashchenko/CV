# Generated by Django 2.2.4 on 2019-08-10 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0005_experience_company'),
    ]

    operations = [
        migrations.RenameField(
            model_name='experience',
            old_name='work_expirience',
            new_name='work_experience',
        ),
    ]
