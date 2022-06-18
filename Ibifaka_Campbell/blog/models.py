from django.db import models, migrations
from django.conf import settings
#from __future__ import unicode_literals

# Create your models here.

#def combine_names(apps, schema_editor):
    # We can't import the Person model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    #Person = apps.get_model('blog', 'Person')
    #for person in Person.objects.all():
        #person.name = '%s %s' % (person.Ibifaka, person.Campbell)
        #person.save()

#class Migration(migrations.Migration):

    #dependencies = [
       # ('blog', '0001_initial'),
   # ]

   # operations = [
        #migrations.RunPython(combine_names),
  #  ]

class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(max_length=250)
    author =models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_date = models.DateTimeField('published_date')
    published_date = models.DateTimeField('published_date')
   
   
#class Migration(migrations.Migration):
    #initial = True
   # dependencies = [
        
   # ]
   # operations = [
        ## name= "Post",
            #fields= [
               #('title', models.CharField(max_length=200)),
              # ('text',models.TextField(max_length=250)),
               #('author',models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)),
               #('created_date', models.DateTimeField('published_date'))
               #('published_date', models.DateTimeField('published_date'))
            #],
       # ),
    #] 