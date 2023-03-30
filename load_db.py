# multi_search/load_db.py
import sys
import os

from faker import Faker
import django

from multi_search.models import Name

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'global_esearch.settings')
os.system("set DJANGO_SETTINGS_MODULE=global_esearch.settings")

django.setup()
print(sys.path)

fake = Faker()
for i in range(500):
    company_name = fake.company()
    company = Name(name=company_name)
    company.save()
