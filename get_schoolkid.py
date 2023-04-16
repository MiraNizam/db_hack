from datacenter.models import Schoolkid


def get_schoolkid(kid_name):
    schoolkid = Schoolkid.objects.get(full_name__contains=kid_name)
    return schoolkid

