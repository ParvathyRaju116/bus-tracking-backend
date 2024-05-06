# Generated by Django 4.2.5 on 2024-03-12 09:18

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('user_type', models.CharField(choices=[('Admin', 'Admin'), ('Bus Owner', 'Bus Owner'), ('Passenger', 'Passenger')], default='Passenger', max_length=50)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
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
            name='Bus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='images')),
                ('Number_plate', models.CharField(max_length=500)),
                ('Engine_no', models.IntegerField()),
                ('RC_book', models.ImageField(upload_to='license')),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='BusCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Ls', 'Ls'), ('Fs', 'Fs'), ('Ordinary', 'Ordinary')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='BusRoute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField()),
                ('bus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapi.bus')),
                ('buscategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapi.buscategory')),
            ],
        ),
        migrations.CreateModel(
            name='BusRouteStops',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('busroute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapi.busroute')),
            ],
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('starts_from', models.CharField(max_length=200)),
                ('ends_at', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('customuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('email_address', models.EmailField(max_length=254)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('adminapi.customuser',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='BusOwner',
            fields=[
                ('customuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('phone', models.CharField(max_length=100, unique=True)),
                ('address', models.CharField(max_length=100)),
                ('proof', models.ImageField(upload_to='images')),
                ('is_approved', models.BooleanField(default='False')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('adminapi.customuser',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('customuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('phone', models.CharField(max_length=100, unique=True)),
                ('email_address', models.EmailField(max_length=254, unique=True)),
                ('address', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('adminapi.customuser',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Stop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stop_number', models.PositiveIntegerField()),
                ('place', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='images')),
                ('link', models.CharField(max_length=100)),
                ('route', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapi.route')),
            ],
        ),
        migrations.CreateModel(
            name='BusStopTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField()),
                ('busstop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapi.busroutestops')),
            ],
        ),
        migrations.AddField(
            model_name='busroutestops',
            name='stop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapi.stop'),
        ),
        migrations.AddField(
            model_name='busroute',
            name='route',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapi.route'),
        ),
        migrations.AddField(
            model_name='bus',
            name='buscategory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapi.buscategory'),
        ),
        migrations.CreateModel(
            name='BusDriver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=100, unique=True)),
                ('address', models.CharField(max_length=100)),
                ('license', models.ImageField(upload_to='image')),
                ('age', models.IntegerField()),
                ('dob', models.DateField()),
                ('busowner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapi.busowner')),
            ],
        ),
        migrations.AddField(
            model_name='bus',
            name='busowner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapi.busowner'),
        ),
    ]
