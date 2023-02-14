import pyautogui
import keyboard


def write(img: str, text: str) -> None:
    if (pyautogui.locateOnScreen(img, confidence=0.9) is not None):
        print(img)
        try:
            pyautogui.click(pyautogui.center(pyautogui.locateOnScreen('home.png', confidence=0.95)))
            pyautogui.typewrite(text + "\n")
        except:
            print("Can't find home")


def main():
    while True:
        if (keyboard.is_pressed('F10')):
            exit(0)

        write("jolvagy.png", "Igen igen")

        write("hogyvagy.png", "Jol")


if __name__ == "__main__":
    main()
