# Generated by Django 3.2.4 on 2021-06-20 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0004_board_created_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='hit',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
