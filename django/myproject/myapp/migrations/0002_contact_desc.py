# Generated by Django 3.2.8 on 2021-10-16 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='desc',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
