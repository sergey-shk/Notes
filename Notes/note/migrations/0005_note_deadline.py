# Generated by Django 3.0.5 on 2020-08-02 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0004_remove_note_deadline'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='deadline',
            field=models.DateTimeField(default=None),
        ),
    ]
