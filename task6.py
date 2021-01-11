start_km = int(input('стартовый результат, км'))
finish_km = int(input('требуемый результат, км'))
result_days = 1

while start_km < finish_km:
    # я знаю что тут не правильно, не могу понять какую формулу применить.
    start_km += start_km + (start_km * 0.1)
    result_days += int(result_days + start_km)
    print(result_days)

