from django.contrib import admin
from tweetapp.models import Tweet
# Register your models here.


class TweetAdmin(admin.ModelAdmin):
    pass

admin.site.register(Tweet,TweetAdmin)