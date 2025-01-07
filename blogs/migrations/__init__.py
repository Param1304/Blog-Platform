from django.db import migrations, models 
class Migration(migrations.Migration):
    initial = True
    dependencies=[]
    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id',models.BigAutoField(auto_created=True)),
                ('category_name',models.CharField(max_length=200)),
                ('created_at',models.DateTimeField(auto_now_add=True)),
                ('updated_at',models.DateTimeField(auto_now=True))
            ],
        ),
    ]