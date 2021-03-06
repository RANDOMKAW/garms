# Generated by Django 2.0 on 2018-12-04 08:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0008_auto_20181203_1756'),
    ]

    operations = [
        migrations.CreateModel(
            name='Marque',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomMarque', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100, null=True)),
                ('description', models.TextField(null=True)),
                ('image', models.ImageField(null=True, upload_to='photos/')),
            ],
            options={
                'verbose_name': 'marque',
                'ordering': ['nomMarque'],
            },
        ),
        migrations.AlterField(
            model_name='article',
            name='marque',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.Marque'),
        ),
    ]
