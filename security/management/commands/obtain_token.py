import sys

from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'Create new jwt token for the requested user'

    def add_arguments(self, parser):
        parser.add_argument('filter', type=str, help='ex: pk=7 or username=apollo or email=foo@bar')

    def _parse_filter(self, filter_value):
        sep_index = str(filter_value).find('=')
        if sep_index == -1:
            raise ValueError("'{}' is not a valid filter".format(filter_value))
        lookup_field, lookup_value = filter_value[0:sep_index], filter_value[sep_index + 1:]
        return {
            lookup_field: lookup_value
        }

    def handle(self, *args, **options):
        try:
            from rest_framework_jwt.settings import api_settings
            from django.contrib.auth import get_user_model
            user = get_user_model().objects.filter(**self._parse_filter(options['filter']))
            if len(user) == 0:
                raise CommandError("There is no user with the given filter")
            if len(user) > 1:
                raise CommandError("There are more than one user with the given filter")
            user = user[0]
            jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
            jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

            payload = jwt_payload_handler(user)
            token = jwt_encode_handler(payload)
            self.stdout.write(token)
        except Exception as exp:
            self.stderr.write("Unable to obtain token because {}".format(str(exp)))
            sys.exit(1)
