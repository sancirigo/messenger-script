import pyautogui
import keyboard


def write(img: str, text: str) -> None:
    if (pyautogui.locateOnScreen(img) is not None):
        pyautogui.click(pyautogui.center(pyautogui.locateOnScreen('home.png')))
        pyautogui.typewrite(text + "\n")


def main():
    while True:
        if (keyboard.is_pressed('F10')):
            exit(0)

        write("jolvagy.png", "Igen igen")

        write("hogyvagy.png", "Jol")


if __name__ == "__main__":
    main()
