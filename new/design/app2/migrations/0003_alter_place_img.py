# Generated by Django 5.0.1 on 2024-01-17 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0002_alter_place_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='app2/image'),
        ),
    ]