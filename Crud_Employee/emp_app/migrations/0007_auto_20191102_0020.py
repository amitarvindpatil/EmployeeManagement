# Generated by Django 2.2.4 on 2019-11-01 18:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('emp_app', '0006_auto_20191102_0018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeelist',
            name='departments',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='department.Department'),
        ),
        migrations.AlterField(
            model_name='employeelist',
            name='designations',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='designation.Designation'),
        ),
        migrations.AlterField(
            model_name='employeelist',
            name='roles',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='role.Role'),
        ),
        migrations.AlterField(
            model_name='employeelist',
            name='user_id',
            field=models.IntegerField(default=1),
        ),
    ]
