# Generated by Django 3.2 on 2021-07-10 09:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(blank=True, default='def_user.jpg', upload_to='account/profiles/', verbose_name='Avatar')),
                ('phone', models.CharField(max_length=64, verbose_name='Phone Number')),
                ('gender', models.CharField(choices=[('Erkek', 'Erkek'), ('Zenan', 'Zenan')], default='Erkek', max_length=5)),
                ('bio', models.TextField(blank=True, verbose_name='Biography')),
                ('age', models.PositiveSmallIntegerField(null=True, verbose_name='Age')),
                ('velayat', models.CharField(choices=[('Aşgabat', 'Aşgabat'), ('Balkan', 'Balkan'), ('Ahal', 'Ahal'), ('Mary', 'Mary'), ('Lebap', 'Lebap'), ('Daşoguz', 'Daşoguz')], default='Aşgabat', max_length=10)),
                ('country', models.CharField(max_length=64, verbose_name='Country')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('is_celler', models.BooleanField(default=False)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Profile',
                'verbose_name_plural': 'Profiles',
                'ordering': ('-created',),
            },
        ),
    ]
