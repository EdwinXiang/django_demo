# Generated by Django 5.0.2 on 2024-07-26 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='demo_feild',
            field=models.TextField(default='demo'),
        ),
        migrations.AlterField(
            model_name='author',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
    ]
