# Generated by Django 4.2.1 on 2023-06-02 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_remove_dog_dogowner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uEmail', models.EmailField(max_length=50)),
                ('uPass', models.CharField(max_length=50)),
            ],
        ),
    ]