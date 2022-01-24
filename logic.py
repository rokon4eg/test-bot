from test_script import TEST_ACTIONS, TEST_SCRIPT

env = {'name_to_call': '',
       'company_name': '',
       'logic_unit': '',
       'entry_point': '',
       'entity': {},
       'do': True,
       'ask': True
       }

script = TEST_SCRIPT


def get_intent(logic_unit, text):
    score = None
    key = ''
    phrase_list = script[logic_unit]['phrase']
    if text == '':
        key = 'NULL'
    elif text.isdigit():
        for phrase in phrase_list:
            if text in phrase:
                key = phrase
                score = int(text)
                break
    elif not text.lower() in phrase_list:
        key = 'DEFAULT'
    else:
        key = text.lower()

    if not phrase_list:
        env['entry_point'] = script[logic_unit]['other_action']
    else:
        phrase_value = phrase_list[key]
        sep_index = phrase_value[0].find(',')  # Ищем ',' в скрипте, так разделены действия для повтора
        if sep_index == -1:
            env['entry_point'] = phrase_value[0]
        else:
            if env['entity'].get('repeat', False):
                env['entry_point'] = phrase_value[0][sep_index + 1:].strip()  # Если повтор, выбираем второе действие
            else:
                env['entry_point'] = phrase_value[0][0:sep_index].strip()  # иначе первое
        if len(phrase_value) > 1:  # Проверяем наличие сущностей для обновления
            new_entity = phrase_value[1]
            if score is not None:
                # в случае числовой оценки в сущность необходимо передать значение score
                [new_entity.update({key: value % score}) for key, value in new_entity.items()]
            env['entity'].update(new_entity)


def do_action(action, company_name='', fio=''):
    run_action = TEST_ACTIONS[action](script, company_name=company_name,
                                      fio=fio)  # Выполняем функцию (если определена)
    # для сооветсвующего действия из модуля actions.py и получаем кортеж необходимых переменных для формирования фразы

    for key, value in script.items():
        if action in value['action']:
            action_value = value['action'][action]
            env['logic_unit'] = key  # Обновляем logic_unit для корректного анализа ответа пользователя
            if len(action_value) > 1:  # Проверяем наличие сущностей для обновления
                env['entity'].update(action_value[1])
            msg = action_value[0]
            if not value['phrase']:
                env['ask'] = False
            if run_action:  # Если для фразы получены переменные, формируем сообщение с их учетом
                msg %= run_action
            print(msg)
