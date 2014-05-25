from optparse import make_option
from django.core.management.base import BaseCommand, CommandError, NoArgsCommand

class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('--file', '-f', dest='file',
            help='Please provide a directory path for your csv.'),
    )
    help = 'Help text goes here'

    def handle(self, **options):
         print "This is a command"