# Generated by Django 3.0 on 2020-06-02 04:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('userpage', '0026_following_follower'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
