# Generated by Django 2.2.7 on 2020-05-29 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='visible',
            field=models.BooleanField(default=True),
        ),
    ]
