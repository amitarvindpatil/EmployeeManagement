# Generated by Django 2.2.4 on 2019-11-30 07:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('emp_app', '0010_auto_20191105_2139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeelist',
            name='designations',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='designations', to='designation.Designation'),
        ),
    ]
