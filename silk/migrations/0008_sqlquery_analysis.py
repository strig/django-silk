# Generated by Django 2.2.17 on 2020-11-26 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('silk', '0007_sqlquery_identifier'),
    ]

    operations = [
        migrations.AddField(
            model_name='sqlquery',
            name='analysis',
            field=models.TextField(blank=True, null=True),
        ),
    ]