# Используйте этот файл, если Вам нужна просто прямая, работающая по алгоритму Брезенхема
# Для выполнения практической работы номер 2 используйте файл "triangleCheck.py"
import random
from PIL import Image, ImageDraw #Подключим необходимые библиотеки

image = Image.open("bear.jpg") #Открываем изображение
draw = ImageDraw.Draw(image) #Создаем инструмент для рисования
width  = image.size[0] #Определяем ширину 
height = image.size[1] #Определяем высоту 	
pix = image.load() #Выгружаем значения пикселей
def sign(x): # знак числа
        if x > 0:
                return 1
        if x < 0:
                return -1
        return 0
def line(x1, y1, x2, y2):  # рисуем линию из точки (x1,y1) в точку (x2,y2)
        dX = abs(x2 - x1)
        dY = abs(y2 - y1)
        if dX >= dY: # если наклон по X больше Y, то X меняем на 1 и смотрим Y
            if x1 > x2: # если точка 2 правее точки 1, меняем их местами
                    x1, x2 = x2, x1
                    y1, y2 = y2, y1
            err = 0 # накапливаемая "ошибка"
            dErr = dY
            y = y1
            dirY = sign(y2 - y1)
            for x in range(x1, x2 + 1):
                    draw.point((x,y),(0,0,0))
                    err += dErr
                    if err + err >= dX:
                            y += dirY
                            err -= dX
        else: # если наклон по Y больше, то, наоборот, Y меняем на 1 и смотрим X
            if y1 > y2: # если точка 2 ближе точки 1, меняем их местами
                    x1, x2 = x2, x1
                    y1, y2 = y2, y1
            err = 0 # накапливаемая "ошибка"
            dErr = dX
            x = x1
            dirX = sign(x2 - x1)
            for y in range(y1, y2 + 1):
                    draw.point((x,y),(0,0,0))
                    err += dErr
                    if err + err >= dY:
                            x += dirX
                            err -= dY
line(0,0,width-1,height-1)
line(0,height-1,width-1,0)
line(width//2,0,0,height//2)
line(width//2,height-1,0,height//2)

line(width//2,height-1,0,0)
line(width//2,0,width-1,height-1)
line(width-1,0,width//2,height-1)
line(width//2,0,0,height-1)
image.show()
#image.save("result.jpg")
del draw
