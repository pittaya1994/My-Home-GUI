from tkinter import *
import socket
import threading

def runserver():
    #####################
    serverip = '192.168.0.149'
    port = 9000
    #####################

    buffsize = 4096

    while True:
            server = socket.socket()
            server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
            server.bind((serverip,port))
            server.listen(1)
            print('waiting micropython...')

            client, addr = server.accept()
            print('connected from:', addr)

            data = client.recv(buffsize).decode('utf-8')
            print('Data from MicroPython: ',data)
            # data = 'LED1:ON' / 'LED1:OFF'
            data_split = data.split(':')

            if float(data_split[1]) > 30:
                img = PhotoImage(file='level3.png')
                ICON.configure(image=img)
                ICON.image = img
                v_status.set('{} อุณหภูมิร้อนเกินไป {}'.format(data_split[0],data_split[1]))
            elif float(data_split[1]) > 28.5:
                img = PhotoImage(file='level2.png')
                ICON.configure(image=img)
                ICON.image = img
                v_status.set('{} อุณหภูมิ {}'.format(data_split[0],data_split[1]))
            elif float(data_split[1]) > 27:
                img = PhotoImage(file='level1.png')
                ICON.configure(image=img)
                ICON.image = img
                v_status.set('{} อุณหภูมิเย็นเกินไป {}'.format(data_split[0],data_split[1]))

            '''
            if data_split[1] == 'ON':
                v_status.set('{} สถานะ {}'.format(data_split[0],data_split[1]))
                L2.configure(fg='green')
            else:
                v_status.set('{} สถานะ {}'.format(data_split[0],data_split[1]))
                L2.configure(fg='red')
            '''    
            client.send('received your messages.'.encode('utf-8'))
            client.close()




GUI = Tk()
GUI.geometry('600x600')
GUI.title('โปรแกรมติดตามสถานะ IoT by Koh')

FONT = ('Angsana New',30)

# ข้อความแสดง - ไม่เปลี่ยนแปลง
L1 = Label(GUI,text='สถานะ LED จาก MicroPython',font=FONT)
L1.pack()

# ข้อความแสดง - มีเปลี่ยนแปลง
v_status = StringVar() #ตัวแปรเก็บค่าสถานะ
v_status.set('<<< No Status >>>')
L2 = Label(GUI, textvariable=v_status, font=FONT)
L2.configure(fg='red')
L2.pack()

img = PhotoImage(file='level1.png')
ICON = Label(GUI,image=img)
ICON.pack()


########RUNSERVER########
task = threading.Thread(target=runserver)
task.start()
#########################
GUI.mainloop()