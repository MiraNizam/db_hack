from datacenter.get_schoolkid import get_schoolkid
from datacenter.models import Mark


def fix_marks(kid_name):
    schoolkid = get_schoolkid(kid_name)
    marks = Mark.objects.filter(schoolkid=schoolkid.id, points__in=[2, 3])
    for mark in marks:
        mark.points = 5
        mark.save()