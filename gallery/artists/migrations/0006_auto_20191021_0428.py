# Generated by Django 2.2.6 on 2019-10-21 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0005_artist_painter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='painter',
            field=models.ImageField(blank=True, upload_to='static/img'),
        ),
    ]