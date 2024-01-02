# Generated by Django 5.0 on 2023-12-30 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadedfile',
            name='file_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='uploadedfile',
            name='name',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]