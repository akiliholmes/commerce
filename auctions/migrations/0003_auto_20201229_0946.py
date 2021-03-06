# Generated by Django 3.0.8 on 2020-12-29 17:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_auctions_bids_comments_listings'),
    ]

    operations = [
        migrations.AddField(
            model_name='listings',
            name='ended',
            field=models.BooleanField(default=None),
        ),
        migrations.AddField(
            model_name='listings',
            name='image',
            field=models.URLField(default=None),
        ),
        migrations.AddField(
            model_name='listings',
            name='starting_bid',
            field=models.IntegerField(default=5.0),
        ),
        migrations.AddField(
            model_name='listings',
            name='watchlist',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='comments',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
