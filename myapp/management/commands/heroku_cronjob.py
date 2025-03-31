from django.core.management.base import BaseCommand
from django.utils import timezone

class Command(BaseCommand):
    
    def handle(self, *args, **options):
        today=timezone.now()
        print("helou cron job executing at {}",today)