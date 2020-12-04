import ctypes
MessageBox = ctypes.windll.user32.MessageBoxW
MessageBox(None, 'Big fish game', 'Window title', 0)