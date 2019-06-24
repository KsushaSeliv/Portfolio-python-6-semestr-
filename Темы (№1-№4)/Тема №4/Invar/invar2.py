#Разработать фрагмент программы с использованием библиотеки pyqrcode, позволяющей создавать изображение QR-кода на основе переданной в
#программу текстовой строки.
#Реализовать модификацию изображения генерируемого QR-кода: раскрасить фрагменты изображения в несколько случайно определяемых цветов.

import pyqrcode
import png

def Qr(content, module_color, background, file_format, scale):
#content-нужная нам строка
#module_color-wdtn qr кода
#background-фон
#file_format-формат сохраняемого qr-кода
#scale-масштаб 
    qrcode = pyqrcode.create(content)
    if file_format == 'png':
        qrcode.png('qr.png', module_color = module_color, background=background,scale=scale)
    elif file_format == 'svg':
        qrcode.svg('qr.svg', module_color = module_color, background=background,scale=scale)

result = input('Cтрока: ')
Qr(result, (0,50,99), (2,5,6), file_format = 'png', scale = 8)
