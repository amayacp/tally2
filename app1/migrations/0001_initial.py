# Generated by Django 4.0.5 on 2022-09-03 10:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cred',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('credit', models.IntegerField()),
                ('debit', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='debit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('credit', models.IntegerField()),
                ('debit', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='GroupModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=225)),
                ('group_alias', models.CharField(max_length=225, null=True)),
                ('group_under', models.CharField(max_length=225)),
                ('nature', models.CharField(max_length=255, null=True)),
                ('gross_profit', models.CharField(max_length=255, null=True)),
                ('sub_ledger', models.BooleanField(default=False)),
                ('debit_credit', models.BooleanField(default=False)),
                ('calculation', models.BooleanField(default=False)),
                ('invoice', models.CharField(blank=True, max_length=225, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='grunder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('und', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items', models.CharField(max_length=255)),
                ('quantity', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='led',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('openam', models.IntegerField()),
                ('penam', models.IntegerField()),
                ('due', models.DateField()),
                ('overd', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ledgercreation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True)),
                ('alias', models.CharField(max_length=255, null=True)),
                ('under', models.CharField(max_length=255)),
                ('bank_details', models.CharField(max_length=255)),
                ('mname', models.CharField(max_length=255, null=True)),
                ('address', models.CharField(max_length=255, null=True)),
                ('country', models.CharField(max_length=255, null=True)),
                ('state', models.CharField(max_length=255, null=True)),
                ('pincode', models.IntegerField(null=True)),
                ('pan_no', models.IntegerField(null=True)),
                ('registration_type', models.CharField(max_length=255, null=True)),
                ('gst_uin', models.IntegerField(null=True)),
                ('set_alter_gstdetails', models.CharField(max_length=255, null=True)),
                ('ac_holder_nm', models.CharField(max_length=255, null=True)),
                ('acc_no', models.IntegerField(null=True)),
                ('ifsc_code', models.IntegerField(null=True)),
                ('swift_code', models.IntegerField(null=True)),
                ('bank_name', models.CharField(max_length=255, null=True)),
                ('branch', models.CharField(max_length=255, null=True)),
                ('SA_cheque_bk', models.CharField(max_length=255, null=True)),
                ('Echeque_p', models.CharField(max_length=255, null=True)),
                ('occ_set_odl', models.CharField(max_length=255, null=True)),
                ('occ_ac_holder_nm', models.CharField(max_length=255, null=True)),
                ('occ_acc_no', models.IntegerField(null=True)),
                ('occ_ifsc_code', models.IntegerField(null=True)),
                ('occ_swift_code', models.IntegerField(null=True)),
                ('occ_bank_name', models.CharField(max_length=255, null=True)),
                ('occ_branch', models.CharField(max_length=255, null=True)),
                ('occ_SA_cheque_bk', models.CharField(max_length=255, null=True)),
                ('occ_Echeque_p', models.CharField(max_length=255, null=True)),
                ('od_set_odl', models.CharField(max_length=255, null=True)),
                ('od_ac_holder_nm', models.CharField(max_length=255, null=True)),
                ('od_acc_no', models.IntegerField(null=True)),
                ('od_ifsc_code', models.IntegerField(null=True)),
                ('od_swift_code', models.IntegerField(null=True)),
                ('od_bank_name', models.CharField(max_length=255, null=True)),
                ('od_branch', models.CharField(max_length=255, null=True)),
                ('od_SA_cheque_bk', models.CharField(max_length=255, null=True)),
                ('od_Echeque_p', models.CharField(max_length=255, null=True)),
                ('statutory_details', models.CharField(max_length=255, null=True)),
                ('type_of_ledger', models.CharField(max_length=100, null=True)),
                ('rounding_method', models.CharField(max_length=100, null=True)),
                ('rounding_limit', models.IntegerField(blank=True, default=None, null=True)),
                ('GST_Applicable', models.CharField(max_length=100, null=True)),
                ('Alter_GST_Details', models.CharField(max_length=100, null=True)),
                ('Appropriate', models.CharField(max_length=100, null=True)),
                ('Types_of_supply', models.CharField(max_length=100, null=True)),
                ('type_duty_tax', models.CharField(max_length=100, null=True)),
                ('tax_type', models.CharField(max_length=100, null=True)),
                ('percentage_of_calcution', models.CharField(max_length=100, null=True)),
                ('rond_method', models.CharField(max_length=100, null=True)),
                ('rond_limit', models.IntegerField(blank=True, default=None, null=True)),
                ('balance_billbybill', models.CharField(max_length=100, null=True)),
                ('credit_period', models.CharField(max_length=100, null=True)),
                ('creditdays_voucher', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='payitems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items', models.CharField(max_length=255)),
                ('quantity', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='vouchert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vdate', models.DateField()),
                ('particular', models.CharField(max_length=255)),
                ('account', models.CharField(max_length=255)),
                ('vouchertype', models.CharField(max_length=255)),
                ('voucherno', models.IntegerField()),
                ('debit', models.IntegerField(blank=True)),
                ('credit', models.IntegerField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='receivable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('party_name', models.CharField(max_length=255)),
                ('pending_amound', models.IntegerField()),
                ('due_date', models.DateField()),
                ('overdue', models.IntegerField(null=True)),
                ('items', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.items')),
            ],
        ),
        migrations.CreateModel(
            name='payable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('party_name', models.CharField(max_length=255)),
                ('pending_amound', models.IntegerField()),
                ('due_date', models.DateField()),
                ('overdue', models.IntegerField(null=True)),
                ('items', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.payitems')),
            ],
        ),
    ]
