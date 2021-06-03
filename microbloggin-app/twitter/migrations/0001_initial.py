# Generated by Django 3.1.3 on 2021-05-31 18:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Publicacion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('contenido', models.CharField(default='', max_length=254)),
                ('fecha', models.DateField(auto_now_add=True)),
                ('republicacion', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='republica', to='twitter.publicacion')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_usuario', models.CharField(default='', max_length=16)),
                ('telefono', models.PositiveIntegerField()),
                ('nombre', models.CharField(default='', max_length=255)),
                ('apellido', models.CharField(default='', max_length=255)),
                ('sexo', models.CharField(choices=[('MASCULINO', 'Masculino'), ('FEMENINO', 'Femenino'), ('OTRO', 'Otro')], default='Masculino', max_length=14)),
                ('fechaNac', models.DateField(default='1930-01-01')),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Administrador',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='twitter.user')),
            ],
            bases=('twitter.user',),
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='twitter.user')),
            ],
            bases=('twitter.user',),
        ),
        migrations.CreateModel(
            name='Tendencias',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('etiqueta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='twitter.publicacion')),
            ],
        ),
        migrations.AddField(
            model_name='publicacion',
            name='mencion',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='menciona', to='twitter.usuario'),
        ),
        migrations.AddField(
            model_name='publicacion',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='realizada', to='twitter.usuario'),
        ),
        migrations.CreateModel(
            name='MensajePriv',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField(auto_now_add=True)),
                ('contenido', models.CharField(default='', max_length=254)),
                ('emisor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='emite', to='twitter.usuario')),
                ('receptor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recibe', to='twitter.usuario')),
            ],
        ),
    ]
