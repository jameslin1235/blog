# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-14 00:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('sampleblog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='approved_comment',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='email',
        ),
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=10),
        ),
        migrations.AddField(
            model_name='comment',
            name='comment_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.AddField(
            model_name='comment',
            name='dislikes',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='likes',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sampleblog.Comment'),
        ),
        migrations.AddField(
            model_name='comment',
            name='slug',
            field=models.SlugField(default=10),
        ),
        migrations.AddField(
            model_name='post',
            name='dislikes',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default=10),
        ),
        migrations.AddField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default=10, upload_to=''),
        ),
        migrations.AlterField(
            model_name='category',
            name='category',
            field=models.CharField(choices=[('Economics', 'Economics'), ('Finance', 'Finance'), ('Pet', 'Pet'), ('Gaming', 'Gaming'), ('Nature', 'Nature'), ('Medical', 'Medical'), ('Social Media', 'Social Media'), ('Sports', 'Sports'), ('Science', 'Science'), ('Technology', 'Technology'), ('History', 'History'), ('Travel', 'Travel'), ('Fashion', 'Fashion'), ('Music', 'Music'), ('Movie', 'Movie'), ('Education', 'Education'), ('Health', 'Health')], max_length=50),
        ),
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='profile',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]