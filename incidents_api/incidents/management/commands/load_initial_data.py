from django.core.management.base import BaseCommand
from incidents.models import Incident

class Command(BaseCommand):
    help = 'Load initial data into the database'

    def handle(self, *args, **options):
        incidents = [
            {
                'title': 'Model bias detected',
                'description': 'The AI model showed significant bias against certain demographic groups.',
                'severity': 'High'
            },
            {
                'title': 'Data leakage',
                'description': 'Training data was found to contain information from the test set.',
                'severity': 'Medium'
            },
            {
                'title': 'Minor performance drop',
                'description': 'Model performance decreased slightly in the latest evaluation.',
                'severity': 'Low'
            }
        ]
        
        for incident_data in incidents:
            Incident.objects.create(**incident_data)
        
        self.stdout.write(self.style.SUCCESS('Successfully loaded initial data'))