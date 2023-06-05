# Generated by Django 4.2.1 on 2023-06-05 17:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="useraccountmodel",
            name="bio",
            field=models.TextField(default=None),
        ),
        migrations.AddField(
            model_name="useraccountmodel",
            name="is_brand",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="useraccountmodel",
            name="is_email_verified",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="useraccountmodel",
            name="is_influencer",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="useraccountmodel",
            name="registered_date",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name="InfluencerModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("account_name", models.CharField(max_length=150)),
                ("phone", models.CharField(max_length=20)),
                ("domain", models.CharField(max_length=150)),
                (
                    "intro_ad_price",
                    models.DecimalField(decimal_places=2, max_digits=20),
                ),
                (
                    "review_ad_price",
                    models.DecimalField(decimal_places=2, max_digits=20),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="BrandModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("brand_name", models.CharField(max_length=300)),
                ("cin", models.CharField(max_length=40)),
                ("gstin", models.CharField(max_length=40)),
                ("address", models.TextField()),
                ("designation", models.CharField(max_length=100)),
                ("is_verified", models.BooleanField(default=False)),
                ("date_joined", models.DateTimeField(auto_now_add=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]