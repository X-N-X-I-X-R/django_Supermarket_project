# Generated by Django 4.2.6 on 2023-11-06 12:25

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("back", "0006_delete_customer"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Order",
            new_name="Customer_orders",
        ),
    ]
