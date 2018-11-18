from django.db import models

class ContactMessage(models.Model):
    name = models.CharField(max_length=64, blank=False, null=True)
    email = models.EmailField(blank=False, null=True)
    subject = models.CharField(max_length=128, blank=False, null=True)
    message = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Message from {}, {} | Subject: {} | Message: {}".format(self.name, self.email, self.subject, self.message)

    class Meta:
        verbose_name = "Contact message"
        verbose_name_plural = "Contact messages"
