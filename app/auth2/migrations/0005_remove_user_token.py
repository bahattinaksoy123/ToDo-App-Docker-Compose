# Generated by Django 4.0.1 on 2022-01-12 11:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth2', '0004_alter_user_token'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='token',
        ),
    ]
