# Generated by Django 3.2.14 on 2022-07-21 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0005_rename_user_lastname_message_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='contact',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='message',
            name='text',
            field=models.CharField(max_length=440),
        ),
    ]
