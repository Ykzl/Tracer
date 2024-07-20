from PyQt5.QtGui import QColor, QPen

MODES = []

MODES.append(
    {
        "name": "Boomerang",
        "trails": [
            {"color": QPen(QColor(192, 192, 192, 255), 2), "boomerang": True},
        ],
    }
)

MODES.append(
    {
        "name": "Gravies",
        "trails": [
            {"gravityMulti": 1.375, "color": QPen(QColor(255, 255, 255, 255), 2)},
            {"gravityMulti": 1.225, "color": QPen(QColor(0, 255, 0, 255), 2)},
            {"gravityMulti": 1.075, "color": QPen(QColor(255, 255, 0, 255), 2)},
            {"gravityMulti": 0.925, "color": QPen(QColor(0, 128, 255, 255), 2)},
            {"gravityMulti": 0.775, "color": QPen(QColor(255, 0, 0, 255), 2)},
            {"gravityMulti": 0.625, "color": QPen(QColor(255, 255, 255, 255), 2)},
            {"gravityMulti": 1.3, "color": QPen(QColor(255, 255, 0, 255), 1), "dashed": True},
            {"gravityMulti": 1.1, "color": QPen(QColor(0, 128, 255, 255), 1), "dashed": True},
            {"gravityMulti": 0.9, "color": QPen(QColor(255, 0, 0, 255), 1), "dashed": True},
            {"gravityMulti": 0.7, "color": QPen(QColor(255, 255, 255, 255), 1), "dashed": True},
        ],
    }
)

MODES.append(
    {
        "name": "Half Gravity",
        "trails": [
            {"powerMulti": 0.7, "gravityMulti": 0.5, "color": QPen(QColor(0, 128, 255, 255), 2)},
        ],
    }
)
MODES.append(
    {
        "name": "Hover+Battering Ram",
        "trails": [
            {"hover": -4, "color": QPen(QColor(128, 0, 255, 255), 2), "dashed": True},
            {"hover": 40, "color": QPen(QColor(128, 128, 255, 255), 1)},
            {"hover": 50, "color": QPen(QColor(128, 128, 255, 255), 2)},
        ],
    }
)
MODES.append(
    {
        "name": "Split",
        "trails": [
            {},
            {"angleOffset": +5.7, "color": QPen(QColor(255, 128, 0, 255), 2)},
            {"angleOffset": -5.7, "color": QPen(QColor(255, 128, 0, 255), 2)},
            {"angleOffset": +11.4, "color": QPen(QColor(255, 255, 0, 255), 1)},
            {"angleOffset": -11.4, "color": QPen(QColor(255, 255, 0, 255), 1)},
            {"angleOffset": +2.85, "color": QPen(QColor(128, 255, 0, 255), 1), "dashed": True},
            {"angleOffset": +8.55, "color": QPen(QColor(255, 0, 255, 255), 1), "dashed": True},
            {"angleOffset": +14.25, "color": QPen(QColor(128, 255, 0, 255), 1), "dashed": True},
            {"angleOffset": -2.85, "color": QPen(QColor(128, 255, 0, 255), 1), "dashed": True},
            {"angleOffset": -8.55, "color": QPen(QColor(255, 0, 255, 255), 1), "dashed": True},
            {"angleOffset": -14.25, "color": QPen(QColor(128, 255, 0, 255), 1), "dashed": True},
        ],
    }
)
