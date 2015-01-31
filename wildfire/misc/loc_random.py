import random
from heatmap.models import tweet

import django
django.setup()

for t in tweet.objects.all():
    t.lng = random.uniform(-118.4814, -117.3000)
    t.lat = random.uniform(33.7683, 34.1561)
    t.save()