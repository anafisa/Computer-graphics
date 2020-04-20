from math import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import random
from PIL import Image, ImageDraw 

window_width = 800
window_height = 600


# Процедура инициализации
def init():
    glEnable(GL_DEPTH_TEST)
    glClearColor(1.0, 1.0, 1.0, 1.0) # Белый цвет для первоначальной закраски
    glMatrixMode(GL_PROJECTION) # Выбираем матрицу проекций
    glLoadIdentity()            # Сбрасываем все предыдущие трансформации
    gluPerspective(90, window_width / window_height, 0.001, 10) # Задаем перспективу
    global anglex, angley, anglez, zoom, filled, pix, n
    image = Image.open("map.bmp") #Открываем изображение
    n = image.size[0] #Определяем ширину 
    pix = image.load()
    anglex = 0
    angley = 0
    anglez = 0
    zoom = 1.0
    filled = 0

# Процедура обработки обычных клавиш
def keyboardkeys(key, x, y):
	global anglex, angley, anglez, zoom, filled
	if key == b'\x1b':
		sys.exit(0)
	if key == b'w':
		anglex += 5
	if key == b's':
		anglex -= 5
	if key == b'q':
		angley += 5
	if key == b'e':
		angley -= 5
	if key == b'a':
		anglez += 5
	if key == b'd':
		anglez -= 5
	if key == b'-':
		zoom /= 1.1
	if key == b'=':
		zoom *= 1.1
	if key == b' ':
		filled = 1 - filled
	glutPostRedisplay()         # Вызываем процедуру перерисовки



# Процедура рисования
def draw(*args, **kwargs):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # Очищаем экран и заливаем текущим цветом фона
    glMatrixMode(GL_MODELVIEW) # Выбираем модельно-видовую матрицу
    glLoadIdentity()           # Сбрасываем все предыдущие трансформации
    gluLookAt(0, 0, -1,        # Положение камеры
        0, 0, 0,           # Точка, на которую смотрит камера
        0, 1, 0)           # Направление "верх" камеры

    if filled == 1:
        glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
    else:
        glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    glScaled(zoom, zoom, zoom)
    
    
    global n, pix
    glPushMatrix()
    glTranslated(-2, -2, 0)
    glScaled(0.03, 0.03, 0.03)

    
    for x in range(1, n, 2):
        for y in range(1, n, 2):
            glBegin(GL_TRIANGLE_FAN)
            glColor3f(0, 0, 0)
            glVertex3d(x, y, pix[x,y]/10)
            glVertex3d(x + 1, y, pix[x + 1,y]/10)
            glVertex3d(x + 1, y + 1, pix[x + 1,y + 1]/10)
            glVertex3d(x, y + 1, pix[x,y + 1]/10)
            glVertex3d(x - 1, y + 1, pix[x - 1,y + 1]/10)
            glVertex3d(x - 1, y, pix[x - 1,y]/10)
            glVertex3d(x - 1, y - 1, pix[x - 1,y - 1]/10)
            glVertex3d(x, y - 1, pix[x,y - 1]/10)
            glVertex3d(x + 1, y - 1, pix[x + 1,y - 1]/10)
            glVertex3d(x + 1, y, pix[x + 1,y]/10)
            glEnd()
            
    glPopMatrix()
            

    glutSwapBuffers()           # Меняем буферы
    glutPostRedisplay()         # Вызываем процедуру перерисовки

glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
glutInitWindowSize(window_width, window_height)
glutInitWindowPosition(50, 50)
glutInit(sys.argv)
glutCreateWindow(b"OpenGL Second Program!")
# Определяем процедуру, отвечающую за рисование
glutDisplayFunc(draw)
# Определяем процедуру, отвечающую за обработку обычных клавиш
glutKeyboardFunc(keyboardkeys)
# Вызываем нашу функцию инициализации
init()
glutMainLoop()


