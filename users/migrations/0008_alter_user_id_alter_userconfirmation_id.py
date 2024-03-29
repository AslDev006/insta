# Generated by Django 4.2.5 on 2023-10-11 04:14

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_user_id_alter_userconfirmation_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.UUIDField(default=uuid.UUID('86fb5a85-24f3-4561-bda2-30832a48c496'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='userconfirmation',
            name='id',
            field=models.UUIDField(default=uuid.UUID('86fb5a85-24f3-4561-bda2-30832a48c496'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
