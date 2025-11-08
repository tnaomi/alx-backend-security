# ip_tracking/middleware.py
from ipware import get_client_ip
from .models import RequestLog, BlockedIp

class IPLoggingMiddleware:
    """Middleware that logs IP address, timestamp, and request path."""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        client_ip, is_routable = get_client_ip(request)

        if client_ip:
            if BlockedIp.objects.filter(ip_address=client_ip).exists():
                from django.http import HttpResponseForbidden
                return HttpResponseForbidden("Your IP has been blocked.")
            RequestLog.objects.create(
                ip_address=client_ip,
                path=request.path
            )

        response = self.get_response(request)
        return response
