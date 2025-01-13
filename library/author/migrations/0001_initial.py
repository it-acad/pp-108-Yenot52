from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        # Include any external dependencies if needed.
    ]

    operations = [
        # CustomUser Model
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('password', models.CharField(default=None, max_length=255)),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('first_name', models.CharField(default=None, max_length=20)),
                ('last_name', models.CharField(default=None, max_length=20)),
                ('middle_name', models.CharField(default=None, max_length=20)),
                ('email', models.CharField(default=None, max_length=100, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('role', models.IntegerField(choices=[(0, 'visitor'), (1, 'admin')], default=0)),
                ('is_active', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),

        # Authors Model
        migrations.CreateModel(
            name='Authors',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=20)),
                ('surname', models.CharField(blank=True, max_length=20)),
                ('patronymic', models.CharField(blank=True, max_length=20)),
                ('books', models.ManyToManyField(related_name='authors', to='book.book')),
            ],
        ),
    ]
