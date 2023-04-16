from datacenter.get_schoolkid import get_schoolkid
from datacenter.models import Chastisement


def remove_chastisements(kid_name):
    schoolkid = get_schoolkid(kid_name)
    chastisements = Chastisement.objects.filter(schoolkid=schoolkid.id)
    chastisements.delete()