import fbchat
from fbchat.models import *
import getpass

def main():
    client = fbchat.Client("sancirigo@gmail.com", getpass.getpass())
    tsalad = "1281138335305176"

    client.send(Message(text="Igen igen"), thread_id = tsalad, thread_type = ThreadType.GROUP)
    client.logout()


main()