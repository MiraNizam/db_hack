from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from datacenter.models import Schoolkid


def get_schoolkid(kid_name):
    try:
        schoolkid = Schoolkid.objects.get(full_name__contains=kid_name)
    except Schoolkid.DoesNotExist:
        raise Exception(f"Имени {kid_name} нет в базе данных учеников, попробуйте исправить и повторить попытку.")
    except Schoolkid.MultipleObjectsReturned:
        raise Exception("Получено больше одного объекта")
    return schoolkid

