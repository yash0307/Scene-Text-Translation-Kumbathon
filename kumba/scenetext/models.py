from django.db import models
import pickle
import sys
from imp import reload
import shelve

#reload(sys)
#sys.setdefaultencoding("ISO-8859-1")

# Create your models here.
class Image(models.Model):
    image = models.ImageField(
        upload_to="images/"
    )
    image_class = models.IntegerField(
        blank=False,
    	default = 0,
    )

class Annotation(models.Model):
    image_class = models.IntegerField(
		    blank = False,
		    default = 0,
		    )
    text = models.CharField(max_length=60,
        blank=True, 
        null=True
    )

with open('/home/yash/kumba-server/kumba/scenetext/orb.pickle', 'rb') as f:
	des, filenames, frequency = pickle.load(f)
