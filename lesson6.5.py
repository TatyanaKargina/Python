class Stationery:
    atr_title = 'Title'

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print('Рисуем ручкой')


class Pencil(Stationery):
    def draw(self):
        print('Рисуем карандашом')


class Handle(Stationery):
    def draw(self):
        print('Рисуем маркером')


pen = Pen()
pencil = Pencil()
handle = Handle()
pen.draw()
pencil.draw()
handle.draw()