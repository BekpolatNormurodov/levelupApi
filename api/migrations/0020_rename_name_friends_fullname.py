# Generated by Django 4.2.6 on 2023-11-07 08:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0019_alter_friends_index'),
    ]

    operations = [
        migrations.RenameField(
            model_name='friends',
            old_name='name',
            new_name='fullname',
        ),
    ]
