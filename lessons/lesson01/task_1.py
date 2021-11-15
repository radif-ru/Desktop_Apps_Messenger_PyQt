"""
1. Написать функцию host_ping(), в которой с помощью утилиты ping
будет проверяться доступность сетевых узлов.
Аргументом функции является список, в котором каждый сетевой узел
должен быть представлен именем хоста или ip-адресом.
В функции необходимо перебирать ip-адреса и проверять
их доступность с выводом соответствующего сообщения
(«Узел доступен», «Узел недоступен»). При этом ip-адрес
сетевого узла должен создаваться с помощью функции ip_address().
"""

# воспользуемся пинг-командой со следуюшими параметрами:
'''
-w интервал

Определяет в миллисекундах время ожидания получения сообщения с эхо-ответом, 
которое соответствует сообщению с эхо-запросом. Если сообщение с эхо-ответом 
не получено в пределах заданного интервала, то выдается сообщение об ошибке 
"Request timed out". Интервал по умолчанию равен 4000 (4 секунды).

-n счетчик
Задает число отправляемых сообщений с эхо-запросом. По умолчанию - 4.
'''

from ipaddress import ip_address
from subprocess import Popen, PIPE
from socket import gethostbyname, gaierror


def host_ping(list_ip_addresses, timeout=500, requests=1):
    """
    Функция проверяет доступность сетевых узлов
    :param list_ip_addresses: список ip адресов и доменных имён
    :param timeout: таймаут запросов, 500 = 0.5 сек
    :param requests: количество запросов
    :return []: возврат словаря с доступными и недоступными узлами
    """
    results = {'Доступные узлы': "", 'Недоступные узлы': ""}  # словарь с результатами
    for address in list_ip_addresses:
        try:
            address = ip_address(address)
        # обойдем такие исключения
        # ValueError: 'yandex.ru' does not appear to be an IPv4 or IPv6 address
        except ValueError:
            address = get_host_by_name(address, get_ip_address=True)
        process = Popen(f"ping {address} -w {timeout} -n {requests}", shell=False, stdout=PIPE)
        process.wait()
        # проверяем код завершения подпроцесса
        if process.returncode == 0:
            results['Доступные узлы'] += f"{str(address)}\n"
            result_string = f'{address} - Узел доступен'
        else:
            results['Недоступные узлы'] += f"{str(address)}\n"
            result_string = f'{address} - Узел недоступен'
        print(result_string)
    return results


def get_host_by_name(address, get_ip_address=False):
    """
    Функция преобразует доменное имя к ip адресу
    :param address: доменное имя
    :param get_ip_address: если True преобразование ip адреса к объекту с помощью ip_address.ip_address
    :return: возврат цифрового ip адреса или объекта адреса в зависимости от get_ip_address
    """
    try:
        # преобразуем доменное имя к ip-адресу
        ip = gethostbyname(address)
        print(f'*** Доменное имя: {address} преобразовано в ip-адрес: {ip} ***')
        if get_ip_address:
            ip = ip_address(ip)
        return ip
        # обойдём исключение: socket.gaierror: [Errno 11001] getaddrinfo failed
    except gaierror:
        print(f'!!! Не удалось получить ip адрес по доменну имени: {address}. Проверьте корректность !!!')


if __name__ == '__main__':
    ip_addresses = ['radif.ru', 'googadle.com', 'yandex.ru', 'google.com', '2.2.2.2', '192.168.0.100', '192.168.0.101']
    host_ping(ip_addresses)

"""
Результат:

*** Доменное имя: radif.ru преобразовано в ip-адрес: 45.89.230.30 ***
45.89.230.30 - Узел доступен
!!! Не удалось получить ip адрес по доменну имени: googadle.com. Проверьте корректность !!!
googadle.com - Узел недоступен
*** Доменное имя: yandex.ru преобразовано в ip-адрес: 77.88.55.55 ***
77.88.55.55 - Узел доступен
*** Доменное имя: google.com преобразовано в ip-адрес: 216.58.210.142 ***
216.58.210.142 - Узел доступен
2.2.2.2 - Узел недоступен
192.168.0.100 - Узел недоступен
192.168.0.101 - Узел недоступен
"""
