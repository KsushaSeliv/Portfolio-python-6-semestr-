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
        qrcode.png('qrcode.png', module_color = module_color, background=background,scale=scale)

        
        
    elif file_format == 'svg':
        qrcode.svg('qrcode.svg', module_color = module_color, background=background,scale=scale)

itog = input('Cтрока: ')

Qr(itog, (0,50,99), (2,5,6), file_format = 'png', scale = 8)

    
    
    
    
    
#2 версия (строка задаётся внутри кода)
import qrcode
import pyqrcode
import png
from PIL import Image


qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data('https://vk.com/selivanovka')
qr.make(fit=True)

img = qr.make_image()
img.save('qr.png')
