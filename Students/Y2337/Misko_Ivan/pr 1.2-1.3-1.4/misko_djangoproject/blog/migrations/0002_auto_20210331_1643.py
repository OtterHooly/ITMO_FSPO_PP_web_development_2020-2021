# Generated by Django 3.1.6 on 2021-03-31 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ownership',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]