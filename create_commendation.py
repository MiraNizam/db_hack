import random

from django.core.exceptions import ObjectDoesNotExist

from datacenter.get_schoolkid import get_schoolkid
from datacenter.models import Subject, Lesson, Commendation


def create_commendation(kid_name, subject):
    commendation_samples = [
        "Молодец!",
        "Отлично!",
        "Хорошо!",
        "Гораздо лучше, чем я ожидал!",
        "Ты меня приятно удивил!",
        "Великолепно!",
        "Прекрасно!",
        "Ты меня очень обрадовал!",
        "Именно этого я давно ждал от тебя!",
        "Сказано здорово – просто и ясно!",
        "Ты, как всегда, точен!",
        "Очень хороший ответ!",
        "Талантливо!",
        "Я поражен!"
    ]
    schoolkid = get_schoolkid(kid_name)
    year_of_study_kid = schoolkid.year_of_study
    group_letter_kid = schoolkid.group_letter
    try:
        lesson = Lesson.objects.filter(
            year_of_study=year_of_study_kid,
            group_letter=group_letter_kid,
            subject__title=subject
        ).order_by("-date").first()
    except Lesson.DoesNotExist:
        print(f"Предмет {subject} не найден, попробуйте исправить и повторить попытку.")
    commendation = Commendation.objects.create(
        text=random.choice(commendation_samples),
        schoolkid=schoolkid,
        subject=lesson.subject,
        teacher=lesson.teacher,
        created=lesson.date)
