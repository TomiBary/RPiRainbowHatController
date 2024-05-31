import rainbowhat as rh
import time


@rh.touch.A.press()
def press_a(channel):
    #get current date in ISO format
    date = time.strftime('%d.%m.', time.gmtime())
    rh.display.print_number_str(date)
    rh.display.show()
    rh.lights.rgb(1, 0, 0)


@rh.touch.B.press()
def press_b(channel):
    #get current time in ISO format
    time_str = time.strftime('%H.%M', time.gmtime())
    rh.display.print_number_str(time_str)
    rh.display.show()
    rh.lights.rgb(0, 1, 0)


@rh.touch.C.press()
def press_c(channel):
    rh.display.print_number_str("    ")
    rh.display.show()
    rh.lights.rgb(0, 0, 1)