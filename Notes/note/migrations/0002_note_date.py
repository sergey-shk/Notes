# Generated by Django 3.0.5 on 2020-07-15 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='date',
            field=models.DateTimeField(default=None),
        ),
    ]
