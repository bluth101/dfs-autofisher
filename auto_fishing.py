import win32
import win32api
import win32con
import time

def get_pixel_colour(i_x, i_y):
	import win32gui
	i_desktop_window_id = win32gui.GetDesktopWindow()
	i_desktop_window_dc = win32gui.GetWindowDC(i_desktop_window_id)
	long_colour = win32gui.GetPixel(i_desktop_window_dc, i_x, i_y)
	i_colour = int(long_colour)
	return (i_colour & 0xff), ((i_colour >> 8) & 0xff), ((i_colour >> 16) & 0xff)

def left_click(x, y):
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y)
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y)

def main():
	print("Starting auto fisher..")

	while True:
		mousex, mousey = win32api.GetCursorPos()
		red, green, blue = get_pixel_colour(mousex, mousey)

		print(red, green, blue)
		# Fish button detected!
		if red < 50 and green > 100 and blue < 50:
			print("Fish detected!")
			left_click(mousex, mousey)
			time.sleep(2)
			left_click(mousex, mousey)

		#print("update")
		time.sleep(3)

if __name__ == "__main__": main()