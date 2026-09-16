from multiprocessing.managers import BaseManager
import os

class QueueManager(BaseManager): pass
QueueManager.register('get_shared_dict')

# Підключаємося до головного комп'ютера за його IP
manager = QueueManager(address=('192.168.1.50', 50000), authkey=b'secret_password')
manager.connect()

# Отримуємо проксі-об'єкт того самого словника, що лежить на Комп'ютері №1!
m = manager.get_shared_dict()

# Комп'ютер №2 робить якісь важкі обчислення локально...
result = 42 ** 10 

# ...і відправляє результат назад на Комп'ютер №1 по мережі:
m['computer_2_result'] = result
