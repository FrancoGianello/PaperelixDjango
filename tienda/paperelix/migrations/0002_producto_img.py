# Generated by Django 4.1.6 on 2023-02-16 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paperelix', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='img',
            field=models.ImageField(default='productos/paperelix.png', upload_to='productos'),
        ),
    ]
