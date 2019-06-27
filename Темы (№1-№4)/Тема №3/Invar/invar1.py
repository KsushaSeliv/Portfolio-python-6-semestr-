#Разработать фрагмент программы, позволяющий получать данные о текущих курсах валют с сайта Центробанка РФ с использованием
#сервиса, который они предоставляют.Применить шаблон проектирования «Одиночка» для предотвращения отправки
#избыточных запросов к серверу ЦБ РФ.

from urllib.request import urlopen
from xml.etree import ElementTree as ET

class CurrencyBoard:
   dictionary = None

   @staticmethod
   def get():
      if CurrencyBoard.dictionary is None:
         CurrencyBoard()
      return CurrencyBoard.dictionary

   def __init__(self):
      if not CurrencyBoard.dictionary:
          currencies_ids_lst = ["R01235", "R01239", "R01820"]
          result = {}
          cur_res_xml = ET.parse(urlopen("http://www.cbr.ru/scripts/XML_daily.asp"))
          root = cur_res_xml.getroot()
          valutes = root.findall('Valute')
          for el in valutes:
              valute_id = el.get('ID')
              if str(valute_id) in currencies_ids_lst:
                  valute_cur_val = el.find('Value').text
                  result[valute_id] = valute_cur_val
          CurrencyBoard.dictionary = result
      else:
          print('Запрос уже был отправлен')

s = CurrencyBoard.get()
print (s)
a = CurrencyBoard.get()
print(a)

assert id(a) == id(s)
print(id(a), id(s))
