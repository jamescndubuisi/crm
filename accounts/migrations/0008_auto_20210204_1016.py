# Generated by Django 3.1.5 on 2021-02-04 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20210204_0941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='note',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]