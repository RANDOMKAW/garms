# Generated by Django 2.0 on 2019-01-07 16:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0018_auto_20190107_1115'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='promoslideshow',
            name='marque',
        ),
    ]
