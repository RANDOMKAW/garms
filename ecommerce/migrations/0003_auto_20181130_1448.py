# Generated by Django 2.0 on 2018-11-30 14:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0002_article_prix'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['date'], 'verbose_name': 'article'},
        ),
        migrations.AddField(
            model_name='article',
            name='URL',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='categorie',
            field=models.CharField(max_length=42, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name="Date d'upload"),
        ),
        migrations.AlterField(
            model_name='article',
            name='collection',
            field=models.CharField(max_length=42, null=True),
        ),
    ]
