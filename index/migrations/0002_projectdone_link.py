# Generated by Django 2.2.4 on 2019-08-08 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectdone',
            name='link',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
    ]
