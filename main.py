import pyautogui
import keyboard


def write(text: str) -> None:
    pyautogui.click(pyautogui.center(pyautogui.locateOnScreen('home.png')))
    pyautogui.typewrite(text + "\n")


def main():
    while True:
        if (keyboard.is_pressed('F10')):
            exit(0)

        if (pyautogui.locateOnScreen("jolvagy.png") is not None):
            write("Igen igen")

        if (pyautogui.locateOnScreen("hogyvagy.png") is not None):
            write("Jol")


if __name__ == "__main__":
    main()
