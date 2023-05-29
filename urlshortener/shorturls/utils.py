import requests
from django.conf import settings


def generate_short_url(original_url):
    response = requests.post(
        url=settings.BITLY_API_ADDRESS,
        headers={"Authorization": f"Bearer {settings.BITLY_API_TOKEN}",
                 "Content-Type": "application/json"},
        json={"long_url": original_url}
    )
    if response.status_code == 200:
        return response.json().get('link')
    else:
        return None


def get_shortened_url(shortened_url_key):
    return f"{settings.BITLY_ADDRESS}/{shortened_url_key}"
