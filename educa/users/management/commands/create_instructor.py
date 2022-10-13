from allauth.account.models import EmailAddress
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.core.management.base import BaseCommand, CommandError

User = get_user_model()


class Command(BaseCommand):
    """
    Create the basic superuser
    `docker-compose -f local.yml run --rm django python manage.py create_instructor`
    """

    help = "Seed database with an 'INSTRUCTOR' user"

    def handle(self, *args, **options):

        if not settings.DEBUG:
            raise CommandError(
                "This command cannot be run when settings DEBUG == False,"
                + " to guard against accidental use on production."
            )

        # Local Instructor User
        if User.objects.filter(email="instructor@email.com").exists():
            print("The instructor local default user already exists.")
        else:
            self.stdout.write("Creating local INSTRUCTOR user...")
            create_local_instructor_user()
            add_user_to_group()
            self.stdout.write("Local INSTRUCTOR user was created")


def create_local_instructor_user():
    User.objects.create_user(email="instructor@email.com", password="testpass123")
    EmailAddress.objects.create(
        # User is selected in this way because it must be a MaterialsUser Instance
        user=User.objects.get(email="instructor@email.com"),
        email="instructor@email.com",
        verified=True,
        primary=True,
    )


def add_user_to_group():
    user = User.objects.get(email="instructor@email.com")
    group = Group.objects.get(name="Instructors")
    group.user_set.add(user)
