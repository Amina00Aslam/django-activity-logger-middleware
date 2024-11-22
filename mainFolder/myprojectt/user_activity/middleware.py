import datetime

from django.http import HttpRequest, HttpResponse
from rest_framework.response import Response

from .models import RequestLog


class RequestLoggingMiddleware:
    def __init__(self, get_response: callable):
        self.get_response = get_response

    def __call__(self, request: HttpRequest) -> HttpResponse:
        """ Process the request, log the details, and return the response """

        response = self.get_response(request)

        # Extract details for logging
        user = request.user if request.user.is_authenticated else None
        ip_address = request.META.get('REMOTE_ADDR')
        url = request.build_absolute_uri()
        method = request.method
        status_code = response.status_code
        timestamp = datetime.datetime.now()

        # Log the request
        RequestLog.objects.create(
            user=user,
            ip_address=ip_address,
            url=url,
            method=method,
            timestamp=timestamp,
            status_code=status_code
        )

        return response
