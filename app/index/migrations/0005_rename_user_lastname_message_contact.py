# Generated by Django 3.2.14 on 2022-07-21 09:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0004_auto_20220719_0847'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='user_lastname',
            new_name='contact',
        ),
    ]
