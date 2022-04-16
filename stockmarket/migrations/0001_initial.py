# Generated by Django 4.0.3 on 2022-04-09 19:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Market',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('market_start_time', models.DateTimeField(null=True)),
                ('market_end_time', models.DateTimeField(null=True)),
                ('market_schedule', models.CharField(choices=[('WEEKDAYS_ONLY', 'WEEKDAYS_ONLY'), ('ALL_DAYS', 'ALL_DAYS')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock_name', models.CharField(max_length=200, null=True)),
                ('stock_created_dt', models.DateTimeField(null=True)),
                ('limit_order_val', models.FloatField(null=True)),
                ('market_price', models.FloatField(null=True)),
                ('status', models.CharField(choices=[('LIMIT_ORDER_BUY', 'LIMIT_ORDER_BUY'), ('LIMIT_ORDER_SELL', 'LIMIT_ORDER_SELL'), ('BOUGHT', 'BOUGHT'), ('AVAILABLE', 'AVAILABLE')], max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Userinfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=50, null=True)),
                ('full_name', models.CharField(max_length=100, null=True)),
                ('email', models.CharField(max_length=30, null=True)),
                ('user_created_dt', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User_stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sold_dt', models.DateTimeField(auto_now_add=True, null=True)),
                ('stock_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='stockmarket.stock')),
                ('user_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='stockmarket.userinfo')),
            ],
        ),
        migrations.CreateModel(
            name='Stock_history',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price_sold', models.FloatField(null=True)),
                ('date', models.DateTimeField(null=True)),
                ('stock_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='stockmarket.stock')),
                ('user_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='stockmarket.userinfo')),
            ],
        ),
        migrations.CreateModel(
            name='Day_trade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('high_val', models.FloatField(null=True)),
                ('low_val', models.FloatField(null=True)),
                ('begin_val', models.FloatField(null=True)),
                ('stock_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='stockmarket.stock')),
            ],
        ),
    ]