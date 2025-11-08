from django.db import models

class RequestLog(models.Model):
    """Keeps an access log
    """
    ip_address = models.GenericIPAddressField()
    timestamp = models.DateTimeField(auto_now_add=True)
    path = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.ip_address} accessed {self.path} at {self.timestamp}"

class BlockedIp(models.Model):
    """Stores blocked IP addresses
    """
    ip_address = models.GenericIPAddressField(unique=True)
    blocked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Blocked IP: {self.ip_address} at {self.blocked_at}"