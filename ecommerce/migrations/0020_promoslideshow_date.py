# Generated by Django 2.0 on 2019-01-07 17:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0019_remove_promoslideshow_marque'),
    ]

    operations = [
        migrations.AddField(
            model_name='promoslideshow',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name="Date d'upload"),
        ),
    ]