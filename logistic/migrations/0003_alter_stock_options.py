# Generated by Django 5.0.4 on 2024-05-04 17:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logistic', '0002_alter_stock_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='stock',
            options={'ordering': ['pk']},
        ),
    ]