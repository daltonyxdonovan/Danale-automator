import pyautogui, time

running = True

while running:
    mouse_pos = pyautogui.position()
    print(mouse_pos)
    time.sleep(1)

    