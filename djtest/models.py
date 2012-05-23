from django.db import models
from django.core.urlresolvers import reverse


class PressNew(models.Model):
    "News for press department"

    title = models.CharField(max_length=256)
    media = models.CharField(max_length=100)
    pubdate = models.DateField(auto_now=True)

    url = models.URLField()
    img = models.FileField(upload_to='uploads/%Y/%m/%d/%H/%M/%S/')
    comment = models.TextField()

    @property
    def imgurl(self):
        return reverse('djtest.views.pressimg', args=[self.id])

    def __unicode__(self):
        return "PressNew id: {0} title: {1}".format(self.id, self.title)
