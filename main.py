import math
import sys
from numpy import sign
import pygetwindow as gw
from pynput import keyboard, mouse
from PyQt5.QtCore import Qt, QTimer, QPoint
from PyQt5.QtGui import QPainter, QFont, QFontMetrics, QPen, QCursor
from PyQt5.QtWidgets import QApplication, QWidget
import modes

GRAVITY = 0.0784
MODES = [{"name": "Normal", "trails": [{}]}] + modes.MODES
print(f"已载入{len(MODES)}个绘制模式")
FONT = QFont("等线", 12)

wind = 0
pos = (0, 0)
leftButtonPos = (0, 0)
leftButtonPressed = False
mode = 0


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 400, 400)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.WindowTransparentForInput)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateWindow)
        self.timer.start(33)
        self.power, self.angle = 0, 0

    def updateWindow(self):
        global pos, wind, leftButtonPressed

        winPos, winSize = self.pos(), self.size()
        rect = self.getWindow()
        if winPos.x() != rect[0] or winPos.y() != rect[1] or winSize.width() != rect[2] or winSize.height() != rect[3]:
            self.setGeometry(rect[0], rect[1], rect[2], rect[3])

        if leftButtonPressed:
            mousePos = self.mapFromGlobal(QCursor.pos())
            if mousePos.x() != leftButtonPos[0] and mousePos.y() != leftButtonPos[1]:
                vecX, vecY = mousePos.x() - pos[0], mousePos.y() - pos[1]
                self.power = min(100, round(100 * math.sqrt(vecX**2 + vecY**2) / (174 * self.width() / 1000)))
                self.angle = round(-math.degrees(math.atan2(vecY, vecX)))

        self.update()

    def getWindow(self):
        title = "Shellshock Live"
        try:
            window = gw.getWindowsWithTitle(title)[0]
            x, y, width, height = window.left, window.top, window.width, window.height
            return (x + 8, y + 32, width - 16, height - 40)
        except IndexError:
            return (self.x(), self.y(), self.width(), self.height())

    def drawTrail(self, painter, powerMulti=1, angleOffset=0, gravityMulti=1, hover=0, color=QPen(Qt.red, 2), dashed=False, boomerang=False):
        power = self.power * powerMulti
        angle = self.angle + angleOffset
        gravity = GRAVITY * gravityMulti * self.width() / 1000
        initialVelocity = 0.1008 * power * self.width() / 1000
        x = int(pos[0] + 10 * math.cos(math.radians(angle)) * self.width() / 1000)
        y = int(pos[1] - 10 * math.sin(math.radians(angle)) * self.width() / 1000)
        points = [QPoint(x, y)]
        vx = initialVelocity * math.cos(math.radians(angle))
        vy = -initialVelocity * math.sin(math.radians(angle))
        windEffect = 0.0001 * (wind - 36.5 * boomerang * vx) * self.width() / 1000

        for _ in range(430):
            x += vx
            y += vy
            vx += windEffect
            hover -= hover > 0 and vy > 0
            vy += gravity * ((vy < 0 or hover <= 0) - (vy > 0 and hover < 0) * hover)
            if y > self.height():
                break
            while x < 0 or x > self.width():
                x = -x if x < 0 else 2 * self.width() - x
                vx = -vx
            points.append(QPoint(round(x), round(y)))

        painter.setPen(color)
        for i in range(len(points) - 1):
            if not dashed or int(i / 2) % 2 == 1:
                painter.drawLine(points[i], points[i + 1])

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # 绘制背景
        # painter.fillRect(self.rect(), QColor(0, 0, 64, 32))

        # 绘制自己位置
        painter.setPen(QPen(Qt.red, 2))
        painter.drawEllipse(QPoint(pos[0], pos[1]), 10 * self.width() / 1000, 10 * self.width() / 1000)

        # 绘制运动轨迹
        for trail in MODES[mode]["trails"]:
            self.drawTrail(painter, **trail)

        # 绘制文本信息
        painter.setPen(QPen(Qt.white))
        painter.setFont(FONT)
        metrics = QFontMetrics(FONT)
        text = f"{self.power}, {sign(self.angle)*(90-abs(90-abs(self.angle)))}"
        painter.drawText(int(pos[0] - metrics.width(text) / 2), int(pos[1] + 40 * self.width() / 1000), text)
        text = f"wind: {wind}"
        painter.drawText(int(pos[0] - metrics.width(text) / 2), int(pos[1] + 40 * self.width() / 1000 + 15), text)
        text = f"mode: {MODES[mode]['name']}"
        painter.drawText(int(pos[0] - metrics.width(text) / 2), int(pos[1] + 40 * self.width() / 1000 + 30), text)


def onKeyboardPress(key):
    global wind, mode
    try:
        if key.vk in range(96, 106):  # 小键盘的数字键 0-9 的键码是 96~105
            num = key.vk - 96
            if abs(wind) == 10 and num == 0:
                wind *= 10
            else:
                wind = sign(wind) * (abs(wind) * 10 % 100) + (1 if wind >= 0 else -1) * num
        elif key.vk == 109:  # 小键盘的减号键
            wind = -wind
        if key.char.isdigit():  # 大键盘的数字键
            if int(key.char) <= len(MODES):
                mode = int(key.char) - 1
    except AttributeError:
        pass


def onMouseClick(x, y, button, pressed):
    global leftButtonPos, leftButtonPressed, pos
    if button == mouse.Button.right and pressed:
        posCursor = QCursor.pos()
        window = QApplication.topLevelWidgets()[0]
        if window.geometry().contains(posCursor):
            pos = (window.mapFromGlobal(posCursor).x(), window.mapFromGlobal(posCursor).y())
    elif button == mouse.Button.left:
        leftButtonPressed = pressed
        if pressed:
            posCursor = QCursor.pos()
            window = QApplication.topLevelWidgets()[0]
            leftButtonPos = (window.mapFromGlobal(posCursor).x(), window.mapFromGlobal(posCursor).y())


listenerKeyboard = keyboard.Listener(on_press=onKeyboardPress)
listenerKeyboard.start()
listenerMouse = mouse.Listener(on_click=onMouseClick)
listenerMouse.start()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyWindow()
    ex.show()
    sys.exit(app.exec_())
