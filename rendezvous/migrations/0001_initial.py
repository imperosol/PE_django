# Generated by Django 3.2.6 on 2021-08-18 16:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('patient', '0001_initial'),
        ('vaccin', '0001_initial'),
        ('centre', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RDV',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('injection', models.PositiveIntegerField()),
                ('centre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='centre.centre')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.patient')),
                ('vaccin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vaccin.vaccin')),
            ],
        ),
    ]