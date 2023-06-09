# Generated by Django 3.2 on 2023-05-30 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_order_detail_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='session_id',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='order_detail',
            name='print_color',
            field=models.CharField(choices=[('Full Color', 'Full Color'), ('Black & White Color', 'Black & White Color')], max_length=50, verbose_name='Print Color'),
        ),
    ]
