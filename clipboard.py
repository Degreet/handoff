import pyperclip
import thread


def on_change_checker(callback):
    temp_cb = pyperclip.paste()

    while True:
        new_cb = pyperclip.paste()
        if temp_cb != new_cb:
            callback(new_cb)


def on_change(callback):
    thread.start_new_thread(on_change_checker, callback)


def get():
    return pyperclip.paste()


def set(value):
    return pyperclip.copy(value)
