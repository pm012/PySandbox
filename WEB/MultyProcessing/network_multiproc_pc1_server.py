from multiprocessing.managers import BaseManager

class QueueManager(BaseManager): pass

# Реєструємо словник, щоб до нього можна було звертатися по мережі
shared_dict = {}
QueueManager.register('get_shared_dict', callable=lambda: shared_dict)

# Запускаємо сервер на порту 50000 з паролем для безпеки
# 192.168.1.50 current pc local ip address
manager = QueueManager(address=('192.168.1.50', 50000), authkey=b'secret_password')
server = manager.get_server()
print("Сервер запущено. Чекаємо на комп'ютери-воркери...")
server.serve_forever() # Сервер працює і тримає словник у своїй пам'яті
