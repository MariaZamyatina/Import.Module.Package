### Домашняя работа к лекции «Import. Module. Package»

[Задание](https://github.com/netology-code/py-homeworks-advanced/tree/master/1.Import.Module.Package)

-----------
Разработана структуру программы "Бухгалтерия".
main.py;
application/salary.py;
application/db/people.py;
main.py - основной модуль для запуска программы.
В модуле salary.py функция calculate_salary.
В модуле people.py функция get_employees.

Знакомство с модулем datetime. При вызове функций модуля main.py выводить текущую дату.

В качестве дополнительного пакета используется matplotlib и в файле requirements.txt указан с актуальной версией.

Создан рядом с файлом main.py модуль dirty_main.py и импортированы функции с помощью конструкции:
 from package.module import *
