# Generated by Django 5.0.4 on 2024-05-04 18:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logistic', '0004_alter_stock_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='stock',
            options={'ordering': ['-id']},
        ),
    ]