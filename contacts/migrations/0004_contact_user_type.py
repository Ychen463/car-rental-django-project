# Generated by Django 4.2.6 on 2023-11-17 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("contacts", "0003_alter_contact_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="contact",
            name="user_type",
            field=models.CharField(
                choices=[("Individual", "Individual"), ("Enterprise", "Enterprise")],
                default="Individual",
                max_length=10,
            ),
        ),
    ]
