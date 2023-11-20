# Generated by Django 4.2.6 on 2023-11-20 00:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("contacts", "0004_contact_user_type"),
        ("orders", "0006_order_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="contacts.contact"
            ),
        ),
    ]