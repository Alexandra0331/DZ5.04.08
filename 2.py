# Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины:
# имена str, ставка int, премия str с указанием процентов вида «10.25%».
# В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения.
# Сумма рассчитывается как ставка умноженная на процент премии

def generate_salary_dict(names_list, salarys_list, awards_list):
    return {name: salary * (1 + float(bonus.strip('%')) / 100) for name, salary,
            bonus in zip(names_list, salarys_list, awards_list)}

names = ["Alex", "Elena", "Mark"]
salarys = [60_000, 150_000, 90_000]
awards = ["10.25", "10.00", "10.50%"]

salarys_dict = generate_salary_dict(names, salarys, awards)
print(salarys_dict)