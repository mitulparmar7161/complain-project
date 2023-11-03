# Generated by Django 4.2.4 on 2023-11-03 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complain_app', '0004_complain_complain_priority_complain_complain_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complain_traking',
            name='assigned_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='complain_traking',
            name='complain_closed_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='complain_traking',
            name='complain_reopened_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='complain_traking',
            name='expected_resolve_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='complain_traking',
            name='reviewed_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='complain_traking',
            name='work_end_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='complain_traking',
            name='work_start_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
