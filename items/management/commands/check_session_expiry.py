from django.core.management.base import BaseCommand
from django.contrib.sessions.models import Session
from datetime import datetime
from django.utils import timezone
class Command(BaseCommand):
    help = 'Check the time remaining for session expiry'

    def handle(self, *args, **options):
        current_time = timezone.now()

        # Query sessions from the database
        sessions = Session.objects.filter(expire_date__gt=current_time)

        for session in sessions:
            remaining_time = (session.expire_date - current_time).total_seconds()
            self.stdout.write(f"Session {session.session_key} expires in {remaining_time} seconds")
