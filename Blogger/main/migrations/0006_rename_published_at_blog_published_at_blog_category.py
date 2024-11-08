# Generated by Django 5.1.2 on 2024-11-04 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_blog_published_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='Published_at',
            new_name='published_at',
        ),
        migrations.AddField(
            model_name='blog',
            name='category',
            field=models.CharField(choices=[('TECH', 'Technology'), ('BUS', 'Business'), ('LIFE', 'Lifestyle'), ('EDU', 'Education'), ('HEALTH', 'Health'), ('ENT', 'Entertainment')], default='TECH', max_length=10),
        ),
    ]
