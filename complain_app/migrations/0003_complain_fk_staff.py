# Generated by Django 4.2.4 on 2023-11-03 08:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0002_staffuser'),
        ('complain_app', '0002_complain_fk_consumer'),
    ]

    operations = [
        migrations.AddField(
            model_name='complain',
            name='fk_staff',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='user_app.staffuser'),
            preserve_default=False,
        ),
    ]
