# Generated by Django 3.2.7 on 2021-09-25 06:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('resource_url', models.URLField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('monthly_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('monthly_discount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('yearly_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('yearly_discount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('is_public', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='category_items', to='category.category')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='items', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'items',
            },
        ),
    ]
