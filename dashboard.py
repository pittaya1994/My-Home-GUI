from tkinter import *
from webbrowser import BackgroundBrowser
from PIL import Image, ImageTk
from threading import Thread
import time

GUI = Tk()
GUI.geometry('1000x600')
GUI.title('IoT System Dashboard')
GUI.state('zoomed')

# Canvas กระดานวาดภาพ
canvas = Canvas(GUI, width=1500, height=800)
canvas.place(x=0, y=0)

# ใส่ background
background = ImageTk.PhotoImage(Image.open('Home 3rd fl.jpg'))
canvas.create_image(300,300, anchor=NW, image = background)


#### Door ####
# วาดสี่เหลี่ยม
canvas.create_polygon([405,430,410,430,410,465,405,465], fill='red',outline='black',tags='d1')
# ใส่ข้อความ
canvas.create_text(150,400,text='Door Close',fill='red',font=('Angsana New',30,'bold'),tags='d1')
# ใส่เส้นชี้
canvas.create_line(220,410,400,450,fill='grey',width=3,tags='d1')

door_state = True # สถานะประตู
def DoorOnOff(event):
    global door_state # เปลี่ยนตัวแปรด้านนอกฟังชั่น
    door_state = not door_state # สลับสถานะ
    canvas.delete('d1')
    if door_state == True:
        canvas.create_polygon([405,430,410,430,410,465,405,465], fill='red',outline='black',tags='d1')
        canvas.create_text(150,400,text='Door Close',fill='red',font=('Angsana New',30,'bold'),tags='d1')
        canvas.create_line(220,410,400,450,fill='grey',width=3,tags='d1')
    else:
        canvas.create_polygon([445,460,445,465,410,465,410,460], fill='green',outline='black',tags='d1')
        canvas.create_text(150,400,text='Door Open',fill='green',font=('Angsana New',30,'bold'),tags='d1')
        canvas.create_line(220,410,400,450,fill='grey',width=3,tags='d1')


fan = ImageTk.PhotoImage(Image.open('fan.png')) 
canvas.create_image(200,200,image=fan,tags='img3')

angle = 0

def run_fan(event=None):
	# fan = ImageTk.PhotoImage(resize_image('fan-icon.png',100))
	global angle
	while True:	
		if angle != 0:
			canvas.delete('img3')
			fan = ImageTk.PhotoImage(image = Image.open('fan.png').rotate(angle)) 
			canvas.create_image(200,200,image=fan,tags='img3')
		angle += 20
		if angle >= 360:
			angle = 0
		time.sleep(0.1)

task = Thread(target=run_fan)
task.start()



GUI.bind('<Return>',DoorOnOff)

GUI.mainloop()
