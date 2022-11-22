from datetime import datetime
import application.salary as salary
import application.db.people as people
import matplotlib.pyplot as plot


def graph():
    months = list(range(1, 12, 1))
    plot.plot(months, salaries)
    plot.ylabel('руб.')
    plot.xlabel('мес.')
    plot.title('выплаты с начала года')
    plot.show()


if __name__ == '__main__':
    print(datetime.now().strftime("%d-%m-%Y %H:%M"))
    emploee = people.get_employees()
    salaries = salary.calculate_salary()
    graph()
