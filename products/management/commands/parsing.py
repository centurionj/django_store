from django.core.management.base import BaseCommand

from .DateParser import DateParser


class Command(BaseCommand):
    """
    parsing товаров
    """

    help = 'Парсинг данных и добавление их в базу данных'

    def handle(self, *args, **options):
        url = 'https://tvoe.ru/catalog/mujchinam/?page=2#16291'
        date_parser = DateParser(url)
        date_parser.collect_data()
        self.stdout.write(self.style.SUCCESS('Парсинг успешно завершен.'))
