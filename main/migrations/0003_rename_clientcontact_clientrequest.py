# Generated by Django 3.2.5 on 2021-07-18 19:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_clientcontact'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ClientContact',
            new_name='ClientRequest',
        ),
    ]
