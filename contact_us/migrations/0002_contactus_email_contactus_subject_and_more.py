# Generated by Django 5.1.2 on 2024-10-24 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_us', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactus',
            name='email',
            field=models.CharField(default='example@example.com', max_length=30),
        ),
        migrations.AddField(
            model_name='contactus',
            name='subject',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='phone',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
    ]