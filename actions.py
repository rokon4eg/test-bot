import logic


def hello(script, *args, **kwargs):
    # msg = script['hello_logic']['action']['hello'][0]
    # print(msg % (kwargs['fio'], kwargs['company_name']))
    return kwargs['fio'], kwargs['company_name']
    pass


def hello_null(script, *args, **kwargs):
    pass


def hangup_null(script, *args, **kwargs):
    pass


def recommend_main(script, *args, **kwargs):
    # confirm=true
    pass


def hangup_wrong_time(script, *args, **kwargs):
    # confirm=false
    pass


def hello_repeat(script, *args, **kwargs):
    return kwargs['company_name']


def recommend_null(script, *args, **kwargs):
    pass


def recommend_default(script, *args, **kwargs):
    pass


def hangup_negative(script, *args, **kwargs):
    pass


def hangup_positive(script, *args, **kwargs):
    pass


def recommend_score_negative(script, *args, **kwargs):
    pass


def recommend_score_neutral(script, *args, **kwargs):
    pass


def recommend_score_positive(script, *args, **kwargs):
    pass


def recommend_repeat(script, *args, **kwargs):
    pass


def recommend_repeat_2(script, *args, **kwargs):
    pass


def forward(script, *args, **kwargs):
    pass


def hangup_action(script, *args, **kwargs):
    print('HANGUP ACTION!')
    logic.env['do'] = False


def bridge_action(script, *args, **kwargs):
    print('BRIDGE ACTION')
    logic.env['do'] = False
