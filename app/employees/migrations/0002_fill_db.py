# Generated by Django 4.1.2 on 2022-10-28 14:53
# ./manage.py makemigrations employees --empty --name=fill_db

from decimal import Decimal
from logging import getLogger

from departments.models import Department
from django.contrib.auth import get_user_model
from django.db import Error, migrations, transaction
from django.utils import timezone
from employees.models import Employee, Position

User = get_user_model()

logger = getLogger(__name__)


def create_staff(level: int, department: Department, employees_count: int = 2000, base_salary: int = 50000):
    position = Position.objects.create(name=f'pos-{level}')
    staff = []
    for j in range(1, employees_count + 1):
        emp_index = j
        salary = j * base_salary
        staff.append(Employee(
            fio=f'fio-{level}-{emp_index}', position=position, joined_date=timezone.now().date(),
            salary=Decimal(str(salary)), department=department,
        ))
    Employee.objects.bulk_create(staff)
    print(department, level)


def create_departments_tree(root_dep: Department, level: int = 5):
    if level > 0:
        for i in range(1, 3):
            dep = Department.objects.create(name=f'Department-{level}-{i}', parent=root_dep)
            create_staff(level, dep)
            d = level - 1
            create_departments_tree(root_dep=dep, level=d)


def fill_db(apps, schema_editor):
    if schema_editor.connection.alias != 'default':
        return
    try:
        with transaction.atomic():
            User.objects.create_superuser(username='admin', email='admin@mail.com', password='admin')
            root_dep = Department.objects.create(name='root')
            create_staff(6, root_dep)
            create_departments_tree(root_dep=root_dep)

    except Error as e:
        logger.error(str(e))


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(fill_db, reverse_code=migrations.RunPython.noop),
    ]