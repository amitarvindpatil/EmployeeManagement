# Generated by Django 2.2.4 on 2019-10-31 11:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('designation', '0002_auto_20191012_2131'),
        ('role', '0001_initial'),
        ('emp_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeelist',
            name='designations',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, to='designation.Designation'),
        ),
        migrations.AddField(
            model_name='employeelist',
            name='roles',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, to='role.Role'),
        ),
    ]
