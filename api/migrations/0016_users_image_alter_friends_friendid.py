# Generated by Django 4.2.6 on 2023-11-06 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_friends_friendid'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='friends',
            name='friendId',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
