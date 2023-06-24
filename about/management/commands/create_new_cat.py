from django.core.management.base import BaseCommand
from about.models import Cat
import json


with open("all_cats.json", "r") as f:
    CATS = json.load(f)


class Command(BaseCommand):
    help = 'Add default cats' # Описание команды

    def handle(self, *args, **kwargs):
        # Проходим по всем именам и создаём для каждого имени кота
        for cat in CATS:
            cat_object = Cat(abb=cat['id'], name=cat['name'], temperament=cat['temperament'], description=cat['description'], wikipedia_url=cat['wikipedia_url'])
            cat_object.save()

        print('All default cats updated. Have a nice day!')
