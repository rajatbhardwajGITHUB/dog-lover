# Generated by Django 4.2.1 on 2023-06-02 02:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_users_info_remove_dog_dogage_alter_dog_dogowner_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dog',
            name='dogOwner',
        ),
    ]
