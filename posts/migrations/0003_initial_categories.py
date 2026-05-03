from django.db import migrations

def create_initial_categories(apps, schema_editor):
    Category = apps.get_model('posts', 'Category')
    categories = ['Technology', 'AI & ML', 'Web Development', 'Programming', 'Design', 'Business']
    for name in categories:
        Category.objects.create(name=name, slug=name.lower().replace(' ', '-'))

class Migration(migrations.Migration):
    dependencies = [
        ('posts', '0002_initial'),
    ]

    operations = [
        migrations.RunPython(create_initial_categories),
    ]
