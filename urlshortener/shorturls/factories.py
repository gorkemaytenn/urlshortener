import factory
from factory.django import DjangoModelFactory

from urlshortener.shorturls.models import URL


class URLFactory(DjangoModelFactory):
    class Meta:
        model = URL

    original_url = factory.Faker('url')
    shortened_url = factory.Faker('url')