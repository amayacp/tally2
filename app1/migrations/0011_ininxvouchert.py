# Generated by Django 4.0.5 on 2022-09-09 07:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0010_rename_account_inincvouchert_iaccount_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ininxvouchert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ivdate', models.DateField()),
                ('iparticular', models.CharField(max_length=255)),
                ('iunder', models.CharField(max_length=255, null=True)),
                ('iaccount', models.CharField(max_length=255)),
                ('ivouchertype', models.CharField(max_length=255)),
                ('ivoucherno', models.IntegerField()),
                ('idebit', models.IntegerField(null=True)),
                ('icredit', models.IntegerField(null=True)),
                ('iledger', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.ledgercreation')),
            ],
        ),
    ]
