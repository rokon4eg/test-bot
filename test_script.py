from actions import *

TEST_ACTIONS = {'hello_null': hello_null,
                'hello': hello,
                'hello_repeat': hello_repeat,
                'recommend_main': recommend_main,
                'recommend_repeat': recommend_repeat,
                'recommend_repeat_2': recommend_repeat_2,
                'recommend_score_negative': recommend_score_negative,
                'recommend_score_neutral': recommend_score_neutral,
                'recommend_score_positive': recommend_score_positive,
                'recommend_null': recommend_null,
                'recommend_default': recommend_default,
                'hangup_positive': hangup_positive,
                'hangup_negative': hangup_negative,
                'hangup_wrong_time': hangup_wrong_time,
                'hangup_null': hangup_null,
                'forward': forward,
                'hangup_action': hangup_action,
                'bridge_action': bridge_action
                }

TEST_SCRIPT = {
    'hello_logic': {
        'action': {
            'hello': [
                '%s, добрый день! Вас беспокоит компания %s, мы проводим опрос удовлетворенности нашими услугами. '
                'Подскажите, вам удобно сейчас говорить?'],
            'hello_repeat': ['Это компания %s  Подскажите, вам удобно сейчас говорить?'],
            'hello_null': ['Извините, вас не слышно.Вы могли бы повторить', {'repeat': True}]},
        'phrase': {
            'NULL': ['hello_null, hangup_null'],
            'DEFAULT': ['recommend_main'],
            'да': ['recommend_main', {'confirm': True}],
            'нет': ['hangup_wrong_time', {'confirm': False}],
            'занят': ['hangup_wrong_time', {'wrong_time': True}],
            'еще раз': ['hello_repeat', {'repeat': True}]
        }
    },
    'main_logic': {
        'action': {
            'recommend_main': ['Скажите, а готовы ли вы рекомендовать нашу компанию своим друзьям? '
                               'Оцените, пожалуйста, по шкале от «0» до «10», где «0» - не буду рекомендовать, '
                               '«10» - обязательно порекомендую.', {'repeat': False}],
            'recommend_repeat': ['Как бы вы оценили возможность порекомендовать нашу компанию своим знакомым '
                                 'по шкале от 0 до 10, где 0 - точно не порекомендую, 10 - обязательно порекомендую.'],
            'recommend_repeat_2': ['Ну если бы вас попросили порекомендовать нашу компанию друзьям или знакомым, '
                                   'вы бы стали это делать? Если «да» - то оценка «10», если точно нет – «0».'],
            'recommend_score_negative': ['Ну а от 0 до 10 как бы вы оценили бы: 0, 5 или может 7 ?'],
            'recommend_score_neutral': ['Ну а от 0 до 10 как бы вы оценили ?'],
            'recommend_score_positive': ['Хорошо,  а по 10-ти бальной шкале как бы вы оценили 8-9 или может 10  ?'],
            'recommend_null': ['Извините вас свосем не слышно,  повторите пожалуйста ?', {'repeat': True}],
            'recommend_default': ['повторите пожалуйста ', {'repeat': True}]
        },
        'phrase': {
            'NULL': ['recommend_null, hangup_null'],
            'DEFAULT': ['recommend_default, hangup_null'],
            tuple(str(_) for _ in range(9)): ['hangup_negative', {'recommendation_score': '%d'}],
            ('9', '10'): ['hangup_positive', {'recommendation_score': '%d'}],
            'нет': ['recommend_score_negative', {'recommendation': 'negative'}],
            'возможно': ['recommend_score_neutral', {'recommendation': 'neutral'}],
            'да': ['recommend_score_positive', {'recommendation': 'positive'}],
            'еще раз': ['recommend_repeat', {'repeat': True}],
            'не знаю': ['recommend_repeat_2', {'recommendation': 'dont_know'}],
            'занят': ['hangup_wrong_time', {'wrong_time': True}],
            'вопрос': ['forward', {'question': True}],
        }
    },
    'hangup_logic': {
        'action': {
            'hangup_positive': ['Отлично!  Большое спасибо за уделенное время! Всего вам доброго!',
                                {'tag': 'высокая оценка'}],
            'hangup_negative': ['Я вас понял. В любом случае большое спасибо за уделенное время!  Всего вам доброго.',
                                {'tag': 'низкая оценка'}],
            'hangup_wrong_time': ['Извините пожалуйста за беспокойство. Всего вам доброго',
                                  {'tag': 'нет времени для разговора'}],
            'hangup_null': ['Вас все равно не слышно, будет лучше если я перезвоню. Всего вам доброго',
                            {'tag': 'проблемы с распознаванием'}]},
        'phrase': {},
        'other_action': 'hangup_action'
    },
    'forward_logic': {
        'action': {
            'forward': ['Чтобы разобраться в вашем вопросе, я переключу звонок на моих коллег. '
                        'Пожалуйста оставайтесь на линии.',
                        {'tag': 'перевод на оператора'}]
        },
        'phrase': {},
        'other_action': 'bridge_action'
    }
}
