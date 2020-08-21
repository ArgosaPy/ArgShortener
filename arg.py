import pyshorteners
import time
import sys
import keyboard

class Parent:
    s = pyshorteners.Shortener(api_key='YOUR ADFLY API KEY', user_id='YOUR ADFLY USER ID', domain='adf.ly', group_id=12, type='int')
    b = pyshorteners.Shortener(api_key='YOUR BITLY API KEY')
    def prnt(self):
        print("1-Adf.ly \n2-Bit.ly\n")
        while True:
            if keyboard.is_pressed('1'):
                print("\n\nPlease Write Your Link\n")
                a = input()
                short = self.s.adfly.short(a)
                print("Your Link is: \n" + short)
                break
            elif keyboard.is_pressed('2\n'):

                break
                i = input()
                print("\n\nPlease Write Your Link\n")
                shorti = self.b.bitly.short(i)
                print("Your Link is: \n" + shorti)
                break

object1 = Parent()
object1.prnt()
