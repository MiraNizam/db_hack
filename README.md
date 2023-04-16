# db_hack
  ## Взлом электронного дневника

В репозитории собрано несколько скриптов для работы с [электронным дневником](https://github.com/MiraNizam/e-diary).

А именно: 
* [get_schoolkid.py](get_schoolkid.py) - запускается других скриптах автоматически, с его помощью получаем данные по ученику. 
* [fix_marks.py](fix_marks.py) - запускаем когда необходимо изменить оценки
* [remove_chastisements.py](remove_chastisements.py) - запускаем, когда нужно удалить несправедливое замечание
* [create_commendation.py](create_commendation.py) - ну а тут мы создаем, заслуженную похвалу

### Начало работы: 

Чтобы запустить скрипт нужно положить файлы с кодом в [datacenter](https://github.com/MiraNizam/e-diary/tree/master/datacenter) и подключить через import.

### Запуск:

Все команды проводить в Django Shell, запускаем его командой:
```
python manage.py shell
```
### Скрипт fix_marks.py

Скрипт поможет избавиться от плохих оценок. Он исправит двойки и тройки на пятерки. 

Импортируем необходимые объекты и функцию из скрипта:
```
>>> from datacenter.models import Mark
>>> from datacenter.fix_marks import fix_marks
```
Запускаем функцию, уточняя Имя и Фамилию ученика:
```
>>> fix_marks("Фролов Иван")
```
### Скрипт remove_chastisements.py

Скрипт поможет избавиться от несправедливых замечаний. Он безболезненно удалит их. 

Импортируем необходимые объекты и функцию из скрипта:
```
>>> from datacenter.get_schoolkid import get_schoolkid
>>> from datacenter.models import Chastisement
```
Запускаем функцию, уточняя Имя и Фамилию ученика:
```
>>> remove_chastisements("Фролов Иван")
```

### Скрипт create_commendation.py

Скрипт поможет сделать похвалу, когда это забыли сделать учителя.
К последнему уроку!

Импортируем необходимые объекты и функцию из скрипта:
```
>>> import random
>>> from datacenter.get_schoolkid import get_schoolkid
>>> from datacenter.models import Subject, Lesson, Commendation
```

Запускаем функцию, уточняя Имя и Фамилию ученика и предмет:
```
>>> create_commendation("Фролов Иван", "Музыка")
```

### Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org/).


