import re
from EventSystem.event import Event


def start_utility_in_window(window_id, util_name):
    # ('starting new util', window_id, util_name)
    Event(util_name, window_id + ":add_util")


def choose_cmd_action(cmd):
    if cmd['main_cmd'] == 'startutil':
        util_name = cmd['second_cmd']
        window_id = cmd['params']['w']
        start_utility_in_window(window_id, util_name)
    elif cmd['main_cmd'] == 'ch_city':
        window_id = cmd['params']['w']
        Event(cmd['second_cmd'], window_id + ":" + "ch_city")
    elif cmd['main_cmd'] == 'split':
        Event(cmd['params'], 'splitEvent')


def parse_command(inpcmd: str):
    main_block = re.search(r'[^-]+\s', inpcmd).group(0)
    commands = main_block.split()

    p_command = dict()
    p_command['main_cmd'] = commands[0]
    if len(commands) > 1:
        p_command['second_cmd'] = commands[1]
    p_command['params'] = dict()

    s_params = inpcmd[len(main_block):]
    if len(s_params) > 1:
        s_params = s_params[1:]

        spl_params = re.split(r' -', s_params)

        for sp in spl_params:
            name, val = sp.split()
            p_command['params'][name] = val
        
    return p_command


# cmd = parse_command('startutil utility_thread -w 3 -name utility_thread -px qwerty')
# choose_cmd_action(cmd)
