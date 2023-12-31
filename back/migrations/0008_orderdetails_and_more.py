# Generated by Django 4.2.6 on 2023-11-06 18:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("back", "0007_rename_order_customer_orders"),
    ]

    operations = [
        migrations.CreateModel(
            name="OrderDetails",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("amount", models.PositiveIntegerField()),
            ],
        ),
        migrations.RenameField(
            model_name="customer_orders",
            old_name="created_at",
            new_name="createdTime",
        ),
        migrations.RemoveField(
            model_name="customer_orders",
            name="total_price",
        ),
        migrations.RemoveField(
            model_name="customer_orders",
            name="updated_at",
        ),
        migrations.AddField(
            model_name="customer_orders",
            name="user",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.DeleteModel(
            name="OrderItems",
        ),
        migrations.AddField(
            model_name="orderdetails",
            name="order",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="back.customer_orders"
            ),
        ),
        migrations.AddField(
            model_name="orderdetails",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="back.product"
            ),
        ),
    ]
