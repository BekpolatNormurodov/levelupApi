# Generated by Django 4.2.7 on 2023-11-27 07:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0028_users_delete_book'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='name',
            new_name='surname',
        ),
    ]
