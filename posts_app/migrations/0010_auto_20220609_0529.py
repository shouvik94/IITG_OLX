# Generated by Django 3.2.5 on 2022-06-08 23:59

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts_app', '0009_alter_product_created_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='created_date',
        ),
        migrations.AddField(
            model_name='product',
            name='buyer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='purchases', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='product',
            name='creating_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 8, 23, 59, 27, 304956, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='product',
            name='selling_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='product_pics/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_details',
            field=models.TextField(blank=True),
        ),
    ]