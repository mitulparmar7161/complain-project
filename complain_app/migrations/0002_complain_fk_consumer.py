# Generated by Django 4.2.4 on 2023-11-03 08:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('complain_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='complain',
            name='fk_consumer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]