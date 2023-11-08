# Generated by Django 4.2.6 on 2023-11-07 10:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("back", "0009_rename_user_customer_orders_user_id"),
    ]

    operations = [
        migrations.CreateModel(
            name="OrderItems",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("quantity", models.PositiveIntegerField()),
                ("item_price", models.FloatField()),
            ],
        ),
        migrations.RenameField(
            model_name="customer_orders",
            old_name="user_id",
            new_name="user",
        ),
        migrations.DeleteModel(
            name="OrderDetails",
        ),
        migrations.AddField(
            model_name="orderitems",
            name="order",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="back.customer_orders"
            ),
        ),
        migrations.AddField(
            model_name="orderitems",
            name="product",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="back.product",
            ),
        ),
    ]