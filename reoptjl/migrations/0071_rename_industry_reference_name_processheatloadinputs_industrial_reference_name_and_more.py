# Generated by Django 4.0.7 on 2024-10-27 04:32

import django.contrib.postgres.fields
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reoptjl', '0070_merge_20240925_0600'),
    ]

    operations = [
        migrations.RenameField(
            model_name='processheatloadinputs',
            old_name='industry_reference_name',
            new_name='industrial_reference_name',
        ),
        migrations.RemoveField(
            model_name='processheatloadinputs',
            name='blended_industry_reference_names',
        ),
        migrations.RemoveField(
            model_name='processheatloadinputs',
            name='blended_industry_reference_percents',
        ),
        migrations.AddField(
            model_name='processheatloadinputs',
            name='blended_industrial_reference_names',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(blank=True, choices=[('Chemical', 'Chemical'), ('Warehouse', 'Warehouse'), ('FlatLoad', 'Flatload'), ('FlatLoad_24_5', 'Flatload 24 5'), ('FlatLoad_16_7', 'Flatload 16 7'), ('FlatLoad_16_5', 'Flatload 16 5'), ('FlatLoad_8_7', 'Flatload 8 7'), ('FlatLoad_8_5', 'Flatload 8 5')], null=True), blank=True, default=list, help_text='Used in concert with blended_industrial_reference_percents to create a blended load profile from multiple Industrial reference facility/sector types.', size=None),
        ),
        migrations.AddField(
            model_name='processheatloadinputs',
            name='blended_industrial_reference_percents',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1.0)]), blank=True, default=list, help_text='Used in concert with blended_industrial_reference_names to create a blended load profile from multiple Industrial reference facility/sector types. Must sum to 1.0.', size=None),
        ),
    ]
