import logging
from django.core.management.base import BaseCommand
from django.utils import timezone

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    
    def handle(self, *args, **options):
        today = timezone.now()
        log_message = f"helou cron job executing at {today}"
        logger.info(log_message)
        print(log_message) 
