from django.db import migrations
from django.contrib.sessions.models import Session

def delete_sessions(*args):
    Session.objects.all().delete()

class Migration(migrations.Migration):
    dependencies = [
        ('todolist_app', '005_create_priorities'),
    ]
    operations = [
        migrations.RunPython(delete_sessions),
    ]