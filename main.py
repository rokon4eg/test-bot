from time import sleep
from logic import do_action, get_intent, env

if __name__ == '__main__':
    env['name_to_call'] = 'Иван Иванович'  # Обращение к пользователю
    env['company_name'] = 'Рога и копыта'  # От имени какой компании звоним
    env['entry_point'] = 'hello'  # Начальная точка входа в скрипт
    env['do'] = True  # Выполняем пока истина
    env['ask'] = True  # Спрашиваем ответа пользователя пока истина
    while env['do']:
        do_action(env['entry_point'], company_name=env['company_name'], fio=env['name_to_call'])
        if env['ask']:
            resp = input()
            if resp.lower() == 'q':
                exit()
        else:
            sleep(0.5)
            resp = ''
        get_intent(env['logic_unit'], resp.lower())
    print('Полученные сущности и теги:', env['entity'])
