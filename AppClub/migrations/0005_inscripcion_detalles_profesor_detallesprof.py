# Generated by Django 5.1.3 on 2024-12-26 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppClub', '0004_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='inscripcion',
            name='detalles',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profesor',
            name='detallesProf',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]