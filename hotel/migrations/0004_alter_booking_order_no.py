# Generated by Django 4.0.4 on 2022-04-22 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0003_remove_room_image_remove_room_image4_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='order_no',
            field=models.IntegerField(),
        ),
    ]
