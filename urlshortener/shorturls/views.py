from django.shortcuts import get_object_or_404
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from urlshortener.shorturls.models import URL
from urlshortener.shorturls.serializers import URLSerializer
from urlshortener.shorturls.utils import generate_short_url, get_shortened_url


class URLShortenerViewset(CreateModelMixin, RetrieveModelMixin, GenericViewSet):
    """
    URL Shortener Viewset
    """
    serializer_class = URLSerializer
    queryset = URL.objects.all()
    lookup_field = 'shortened_url'

    @swagger_auto_schema(request_body=URLSerializer)
    def create(self, request):
        """Creates a short URL"""
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        original_url = serializer.validated_data['original_url']
        try:
            url = URL.objects.get(original_url=original_url)
        except URL.DoesNotExist:
            shortened_url = generate_short_url(original_url)
            if shortened_url:
                url = URL.objects.create(original_url=original_url, shortened_url=shortened_url)
            else:
                return Response({"error": "Shortened URL could not be generated. Please try again later."}, status=400)
        return Response(URLSerializer(url).data, status=201)
        


    @swagger_auto_schema(manual_parameters=[
        openapi.Parameter(
            'shortened_url_key',  
            in_=openapi.IN_PATH,  
            type=openapi.TYPE_STRING,  
            description='The unique key of the short URL.',  
        ),
    ])
    def retrieve(self, request, shortened_url=None):
        """
        Retrieves the original URL using the shortened URL unique key

        Example: 
        - Shortened URL: "https://bit.ly/45DvbHB",
        - Unique key: "45DvbHB"
        """
        url = get_shortened_url(shortened_url)
        obj = get_object_or_404(URL, shortened_url=url)
        obj.times_followed += 1
        obj.save()
        serializer = self.get_serializer(obj)
        return Response(serializer.data)
