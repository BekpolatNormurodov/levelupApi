# Generated by Django 4.2.6 on 2023-10-25 06:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_phones_users_delete_blacklist_phones_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='phones',
            name='test',
        ),
        migrations.AddField(
            model_name='phones',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.users'),
        ),
    ]