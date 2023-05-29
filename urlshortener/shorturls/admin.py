from django.contrib import admin

from urlshortener.shorturls.models import URL


class URLAdmin(admin.ModelAdmin):
    list_display = ('original_url', 'shortened_url', 'created_at', 'times_followed', 'last_accessed')
    ordering = ('-created_at',)

admin.site.register(URL, URLAdmin)
