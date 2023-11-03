# Generated by Django 4.2.4 on 2023-11-03 08:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('complain_app', '0002_complain_fk_consumer'),
        ('user_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StaffUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('designation', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='staff_image/')),
                ('employee_id', models.CharField(max_length=100)),
                ('work_location', models.CharField(max_length=100)),
                ('fk_department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='complain_app.department')),
                ('fk_organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='complain_app.organization')),
                ('fk_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Staff Users',
                'db_table': 'staff_user',
            },
        ),
    ]
