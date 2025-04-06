from django.db import models

class Incident(models.Model):
    SEVERITY_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    severity = models.CharField(max_length=10, choices=SEVERITY_CHOICES)
    reported_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table='ai_safety_incidents'
    
    
    def __str__(self):
        return self.title
