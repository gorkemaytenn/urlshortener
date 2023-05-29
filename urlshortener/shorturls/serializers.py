from rest_framework import serializers

from urlshortener.shorturls.models import URL


class URLSerializer(serializers.ModelSerializer):
    class Meta:
        model = URL
        read_only_fields = ('shortened_url', 'created_at',
                            'times_followed', 'last_accessed')
        fields = ('original_url', 'shortened_url', 'created_at',
                  'times_followed', 'last_accessed')
