# Generated by Django 3.2.4 on 2021-06-20 15:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0003_auto_20210621_0040'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
