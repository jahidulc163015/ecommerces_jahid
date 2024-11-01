# Generated by Django 4.2.16 on 2024-10-23 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_billing_alter_contact_email_alter_contact_message_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vegetables',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='vegetables/')),
            ],
        ),
    ]
