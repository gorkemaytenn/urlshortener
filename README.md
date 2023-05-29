# Django URL Shortener

A URL shortener API built with Django and Django Rest Framework.

## Features

- Create short URLs
- Retrieve original URLs using short URLs
- Keep track of the usage of each short URL

## Getting Started

### Prerequisites

- Docker
- Docker Compose

### Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/urlshortener.git
   cd urlshortener
   ```

2. Build and run the Docker containers:

   ```bash
   docker-compose up --build
   ```

   This will also apply the Django migrations and start the server.

### Usage

1. To create a short URL, send a POST request to `http://localhost:8000/api/shorturls/` with the following data:

   ```json
   {
     "original_url": "http://example.com"
   }
   ```

   This will return a response with the short URL.

2. To retrieve the original URL using a short URL, send a GET request to `http://localhost:8000/api/shorturls/{short_url}/`.

### Running tests

1. To run tests, execute the following command:

   ```bash
   docker-compose run web python manage.py test
   ```

### Documentation

API documentation can be found at `http://localhost:8000/swagger`.

---
