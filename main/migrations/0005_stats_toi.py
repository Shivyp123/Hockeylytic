# Generated by Django 3.1.2 on 2020-12-14 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_remove_stats_toi'),
    ]

    operations = [
        migrations.AddField(
            model_name='stats',
            name='toi',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
