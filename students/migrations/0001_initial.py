# Generated by Django 4.0.5 on 2022-06-23 13:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emailid', models.CharField(blank=True, max_length=45, null=True, unique=True)),
                ('password', models.CharField(blank=True, max_length=225, null=True)),
                ('name', models.CharField(blank=True, max_length=45, null=True)),
                ('branch', models.CharField(blank=True, max_length=45, null=True)),
                ('address', models.CharField(blank=True, max_length=500, null=True)),
                ('year', models.CharField(blank=True, max_length=45, null=True)),
                ('is_active', models.IntegerField(blank=True, null=True)),
                ('mob', models.CharField(blank=True, max_length=45, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productname', models.CharField(blank=True, max_length=500, null=True)),
                ('productdesc', models.CharField(blank=True, max_length=500, null=True)),
                ('category', models.CharField(blank=True, max_length=500, null=True)),
                ('status', models.IntegerField(blank=True, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('productage', models.CharField(blank=True, max_length=45, null=True)),
                ('img', models.FileField(default='', null=True, upload_to='student/images')),
                ('studentid', models.ForeignKey(blank=True, db_column='studentid', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='students.students')),
            ],
        ),
    ]
