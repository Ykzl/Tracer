# Tracer

## 公告 (Announcement)

补充于2026年9月：
Supplemented in September 2026:

本软件将不再更新。
This software will no longer be updated.

它的原理仅仅是一个附加在游戏窗口上的透明窗体，不读取游戏的任何内容。这也决定了它已经难以在功能性上更进一步。
It works simply as a transparent window attached to the game window and does not read any content from the game. This also means that it is difficult for it to advance any further functionally.

当然，我们还可以为它适配更多种类的武器，比如让它预测并显示“海鸥”拉的屎，“3D炸弹”的距离，“加特林”、“青蛙”、“Rocker”等随机散弹的范围，“Bumper Bombs”的发弹源位置和反弹位置。
Of course, we could still adapt it for more types of weapons, such as making it predict and display the poop dropped by the "Seagull", the distance of the "3D Bomb", the spread range of random scatter shots such as the "Gatling", "Frog", and "Rocker", and the launch source position and bounce positions of "Bumper Bombs".

但也就仅此而已了。我们无法通过合理的方式获取游戏内的地形和障碍物的信息。无论是图像识别，还是人工输入，效果都非常，非常，非常差。
But that's all there is to it. We cannot obtain information about the terrain and obstacles in the game in any reasonable way. Whether through image recognition or manual input, the results are very, very, very poor.

面对圆形反弹板和黑洞，只要软件得到的信息和游戏内实际的信息有一丁点误差，对预测的结果的影响都是灾难性的。
In the face of circular bumpers and black holes, as long as there is even the slightest discrepancy between the information obtained by the software and the actual information in the game, the impact on the prediction results is catastrophic.

因此，本软件将不再更新。让我们期待未来可能会出现的，直接从游戏内存中读取信息的，可以准确预测圆形反弹板和黑洞的辅助软件吧。
Therefore, this software will no longer be updated. Let us look forward to the possible future assistant software that reads information directly from the game memory and can accurately predict circular bumpers and black holes.

以下为原本的Readme.md。
Below is the original Readme.md.

## 介绍 (Introduction)

Tracer 是一个用于预测和显示游戏 Shellshock Live 中子弹弹道的工具。

Tracer is a tool for predicting and displaying the trajectories of bullets in the game Shellshock Live.

## 操作方法 (Usage)

0. 工具的窗口会自动对齐到游戏窗口。The tool window will automatically align with the game window.
1. 鼠标右键点击自己所在的位置。Right-click to mark your position.
2. 鼠标左键拖动调整力量和角度。Left-click and drag to adjust power and angle.
3. 按住Left Alt后鼠标左键拖动调整风力的大小和方向(或使用小键盘数字键和减号键直接进行设置)(或使用鼠标滚轮)。Left-click and drag while Holding Left Alt key to adjust the size and direction of the wind (or use the numeric keypad numbers and minus key to set it directly)(or use mouse wheel).
4. 大键盘数字键设置不同的绘制模式。Use the main keyboard numeric keys to set different drawing modes.

## 绘制模式 (Drawing Modes)

工具预设了以下模式：

The tool has the following predefined modes:

-   **Boomerang Mode**
-   **Gravies Mode**
-   **Half Gravity Mode**
-   **Hover+Battering Ram Mode**
-   **Split Mode**

你可以在 `modes.py` 文件里查阅、增加、修改和删除绘制模式。

You can view, add, modify, and delete drawing modes in the `modes.py` file.

## 许可证 (License)

该项目采用 MIT 许可证开源。详情请见[许可证](LICENSE)文件。

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
