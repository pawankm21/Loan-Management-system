# Generated by Django 3.2.3 on 2021-06-02 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loanapp', '0004_auto_20210602_0720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='account_number',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
