# Generated by Django 2.0 on 2018-12-06 14:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0013_auto_20181206_1404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='marque',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.Marque'),
        ),
    ]
