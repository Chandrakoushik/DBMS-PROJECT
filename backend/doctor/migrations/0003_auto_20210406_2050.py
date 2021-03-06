# Generated by Django 3.0.5 on 2021-04-06 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0002_auto_20210402_0904'),
    ]

    operations = [
        migrations.RenameField(
            model_name='crop',
            old_name='disease_symptoms',
            new_name='disease_fertilizers',
        ),
        migrations.AddField(
            model_name='crop',
            name='image_crop',
            field=models.ImageField(null=True, upload_to='images'),
        ),
        migrations.AddField(
            model_name='crop',
            name='image_disease',
            field=models.ImageField(null=True, upload_to='images'),
        ),
    ]
