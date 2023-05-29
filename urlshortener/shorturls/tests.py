from unittest.mock import patch

from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from urlshortener.shorturls.factories import URLFactory
from urlshortener.shorturls.models import URL


class URLShortenerViewSetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.shorturls_create_url = "/api/shorturls/"
        self.shorturls_detail_url = "/api/shorturls/"

    def mock_generate_short_url(self):
        return "https://bit.ly/test"

    def test_create_empty_url(self):
        response = self.client.post(path=self.shorturls_create_url, data={})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(URL.objects.count(), 0)

    def test_create_valid_url(self,):
        with patch("shorturls.views.generate_short_url", return_value=self.mock_generate_short_url()):
            valid_url = "https://example.com/"
            response = self.client.post(path=self.shorturls_create_url, data={
                                        "original_url": valid_url})
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
            self.assertEqual(URL.objects.count(), 1)
            self.assertEqual(response.data.get("shortened_url"),
                             self.mock_generate_short_url())

    def test_create_existing_valid_url(self,):
        obj = URLFactory()
        response = self.client.post(self.shorturls_create_url, {
                                    "original_url": obj.original_url})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(URL.objects.count(), 1)
        self.assertEqual(response.data.get("shortened_url"), obj.shortened_url)

    def test_create_invalid_url(self):
        invalid_url = "example"
        response = self.client.post(self.shorturls_create_url, {
                                    "original_url": invalid_url})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(URL.objects.count(), 0)

    def test_retrieve_existing_url(self):
        obj = URLFactory(original_url="https://example.com/", shortened_url="https://bit.ly/test")
        key = obj.shortened_url.split('/')[-1]
        response = self.client.get(self.shorturls_detail_url + key + '/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['original_url'], obj.original_url)

    def test_retrieve_non_existing_url(self):
        response = self.client.get('/api/shorturls/non-existing-url/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
