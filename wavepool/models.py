from django.db import models
from django.urls import reverse
from django.utils import timezone

DIVESITE_SOURCE_NAMES = {
    'retaildive': 'Retail Dive',
    'ciodive': 'CIO Dive',
    'educationdive': 'Education Dive',
    'supplychaindive': 'Supply Chain Dive',
    'restaurantdive': 'Restaurant Dive',
    'grocerydive': 'Grocery Dive',
    'biopharmadive': 'BioPharma Dive',
    'hrdive': 'HR Dive',
}


class NewsPost(models.Model):
    title = models.CharField(max_length=300)
    body = models.TextField(max_length=3000)
    source = models.URLField()
    is_cover_story = models.BooleanField(default=False)
    publish_date = models.DateField(default=timezone.now)

    @property
    def url(self):
        return reverse('newspost_detail')

    @property
    def teaser(self):
        return self.body[:150]

    @property
    def source_divesite_name(self):
        # finds the first period and then ".com". In between them is the source name and then it is cinverted into a properly formatted string
        startIndex = self.source.index(".")+1
        endIndex = self.source.index(".com")
        return DIVESITE_SOURCE_NAMES[self.source[startIndex:endIndex]]
        

    def tags(self):
        return [
            'HR', 'Diversity & Inclusion', 'Culture'
        ]
