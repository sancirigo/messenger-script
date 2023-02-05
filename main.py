import pyautogui
import keyboard


def write(img: str, text: str) -> None:
    if (pyautogui.locateOnScreen(img) is not None):
        print(img)
        try:
            pyautogui.click(pyautogui.center(pyautogui.locateOnScreen('home.png')))
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
