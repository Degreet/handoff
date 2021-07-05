import clipboard

print(clipboard.get())

clipboard.set('123')
print(clipboard.get())


def callback(text):
    print(text)


clipboard.on_change(callback)
