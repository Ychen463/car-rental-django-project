# Generated by Django 4.2.7 on 2023-12-07 23:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("payments", "0005_payment_discounted_amount"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="payment",
            name="status",
        ),
    ]
