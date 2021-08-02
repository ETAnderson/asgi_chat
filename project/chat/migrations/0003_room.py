# Generated by Django 3.2.5 on 2021-08-02 15:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_rename_room_roomindex'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_name', models.CharField(max_length=140)),
                ('indexed_at', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chat.roomindex')),
            ],
        ),
    ]
