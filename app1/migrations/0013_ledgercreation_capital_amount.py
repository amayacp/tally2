# Generated by Django 4.0.6 on 2022-09-15 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0012_inincvouchert_iopeningbal_ininxvouchert_iopeningbal_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ledgercreation',
            name='capital_amount',
            field=models.IntegerField(null=True),
        ),
    ]
