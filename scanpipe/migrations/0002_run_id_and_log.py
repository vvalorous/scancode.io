# Generated by Django 3.1.5 on 2021-01-27 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scanpipe', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='run',
            name='run_id',
            field=models.CharField(blank=True, editable=False, max_length=16),
        ),
        migrations.AddField(
            model_name='run',
            name='log',
            field=models.TextField(blank=True, editable=False),
        ),
    ]
