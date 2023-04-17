from django.core.exceptions import ObjectDoesNotExist
from datacenter.models import Schoolkid


def get_schoolkid(kid_name):
    try:
        schoolkid = Schoolkid.objects.get(full_name__contains=kid_name)
    except Schoolkid.DoesNotExist:
        print(f"Имени {kid_name} нет в базе данных учеников, попробуйте исправить и повторить попытку.")
    return schoolkid

