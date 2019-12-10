# Generated by Django 2.2.3 on 2019-12-10 03:20

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('user_type', models.CharField(choices=[('CU', 'Customer'), ('RM', 'Restaurant Manager')], default='CU', max_length=2)),
                ('contact', models.CharField(default='n/a', max_length=11, verbose_name='Contact Numbers')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('CatID', models.CharField(max_length=30, primary_key=True, serialize=False, verbose_name='Category ID')),
                ('CatName', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('RestoID', models.CharField(default='none', max_length=30, primary_key=True, serialize=False, unique=True, verbose_name='Restaurant ID')),
                ('Open_time', models.TimeField(default='0:0', null=True, verbose_name='Opening Time')),
                ('Closing_time', models.TimeField(default='0:0', null=True, verbose_name='Closing Time')),
                ('Address', models.CharField(default='none', max_length=100, verbose_name='Address')),
                ('Landline', models.CharField(default='none', max_length=10, verbose_name='Landline')),
                ('Contact', models.CharField(default='none', max_length=11, verbose_name='Contact')),
                ('Rating', models.IntegerField(default=0)),
                ('WaitTime1_4', models.IntegerField(default=0)),
                ('WaitTime5_8', models.IntegerField(default=0)),
                ('WaitTime9_12', models.IntegerField(default=0)),
                ('Category', models.ManyToManyField(related_name='Restaurants', to='webapp.Categories')),
                ('MngID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Manager ID')),
            ],
        ),
        migrations.CreateModel(
            name='WaitListEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=30, verbose_name='Last Name')),
                ('PaxCount', models.IntegerField(default=1)),
                ('TimeIn', models.DateTimeField(auto_now_add=True, verbose_name='Time In')),
                ('TimeOut', models.DateTimeField(auto_now=True, null=True, verbose_name='Time Out')),
                ('Seated', models.BooleanField(default=False, verbose_name='Seated')),
                ('WaitTime', models.IntegerField(default=None, null=True)),
                ('RestoID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='WaitListEntry', to='webapp.Restaurant')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('ReviewID', models.CharField(max_length=30, primary_key=True, serialize=False, unique=True, verbose_name='ReviewID')),
                ('Rating', models.IntegerField()),
                ('ReviewDetail', models.CharField(default='no Review', max_length=300)),
                ('RestoID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.Restaurant')),
            ],
        ),
    ]
