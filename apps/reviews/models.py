from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class Review(models.Model):
    review_title = models.CharField(max_length=100, blank=True, default='')
    username = models.CharField(max_length=100, blank=True, default='')
    review_date = models.DateTimeField(auto_now_add=True)
    product = models.CharField(max_length=60, blank=True, default='')
    image_url = models.UrlField(blank=True, null=True)
    user_review = models.CharField(max_length=500, blank=True, default='')
    

    class Meta:
        ordering = ('review_date',)

    def __str__(self):
        return self.product