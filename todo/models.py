from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    tags = models.CharField(max_length=100, verbose_name='#Тэги', blank=True)
    rating = models.IntegerField(null=True, blank=True)
    public = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    album = models.TextField(default='',null=True, blank=True)
    class Meta:
        ordering = ['id']

    def __str__(self):
        return str(self.id) + ' ' + self.title


def id_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/photos/<prj_id>/<filename>
    return 'photos/{0}/{1}'.format(instance.prj_id.id, filename)


class Comment(models.Model):
    name = models.CharField(max_length=100, verbose_name='Ваше имя:')
    comment = models.TextField(verbose_name='Ваш отзыв:')
    public = models.BooleanField(default=False, verbose_name='Опубликован')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
