# Создание пользовательского исключения
class StepValueError(ValueError):
    pass

# Создание итератора
class Iterator:
    def __init__(self, start, stop, step=1):
        if step == 0:
            raise StepValueError('Шаг не может быть равен 0')
        self.start = start
        self.stop = stop
        self.step = step
        self.pointer = start

    def __iter__(self):
        self.pointer = self.start  # Сбрасываем pointer в начальное значение
        return self

    def __next__(self):
        # Условие окончания итерации зависит от знака шага
        if (self.step > 0 and self.pointer >= self.stop) or (self.step < 0 and self.pointer <= self.stop):
            raise StopIteration
        # Сохраняем текущее значение pointer и увеличиваем его на step
        current = self.pointer
        self.pointer += self.step
        return current

# Демонстрация работы

try:
    iter1 = Iterator(100, 200, 0)  # Неверный шаг
    for i in iter1:
        print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно')

# Другие примеры итераторов
iter2 = Iterator(-5, 2)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 0, -1)

# Итерация с помощью цикла for
for i in iter2:
    print(i, end=' ')
print()

for i in iter3:
    print(i, end=' ')
print()

for i in iter4:
    print(i, end=' ')
print()