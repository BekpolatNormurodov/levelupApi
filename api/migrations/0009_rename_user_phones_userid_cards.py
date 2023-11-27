# Generated by Django 4.2.6 on 2023-10-26 07:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_remove_users_age_users_birthday'),
    ]

    operations = [
        migrations.RenameField(
            model_name='phones',
            old_name='user',
            new_name='userId',
        ),
        migrations.CreateModel(
            name='Cards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank', models.CharField(max_length=100, null=True)),
                ('phone', models.IntegerField(null=True)),
                ('number', models.CharField(max_length=100, null=True)),
                ('date', models.CharField(max_length=100, null=True)),
                ('fullname', models.CharField(max_length=100, null=True)),
                ('userId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.users')),
            ],
        ),
    ]
