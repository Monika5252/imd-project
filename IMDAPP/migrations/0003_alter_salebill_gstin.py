# Generated by Django 4.1.2 on 2022-12-22 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IMDAPP', '0002_alter_nonstock_category_alter_nonstock_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salebill',
            name='gstin',
            field=models.CharField(max_length=15),
        ),
    ]
