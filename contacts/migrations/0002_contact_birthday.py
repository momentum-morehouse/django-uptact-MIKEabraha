# Generated by Django 3.0.8 on 2020-07-06 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='birthday',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
