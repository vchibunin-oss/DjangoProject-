from django.core.management import call_command
from django.core.management.base import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):
    help = "Удаление и загрузка тестовых данных из фикстуры"

    def handle(self, *args, **options):
        Product.objects.all().delete()
        Category.objects.all().delete()

        call_command("loaddata", "catalog_data.json")

        self.stdout.write(
            self.style.SUCCESS("Тестовые данные успешно загружены!")
        )