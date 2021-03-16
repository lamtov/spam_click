from tkinter import *
from tkinter import filedialog as fd
import os
import logging
cur_dir= os.getcwd()
folder_dataset = cur_dir+ '/dataset/'
from tkinter import messagebox
import time
from threading import Lock
from concurrent.futures import ThreadPoolExecutor
from bot_auto_jerkncum import Bot
class MyWindow:
    def __init__(self, win):
        self.folder_dataset= cur_dir+ '/dataset/'
        self.lb_folder_dataset = Label(win, text='Folder output (default: ' + self.folder_dataset + ')', bg="black", fg="white",font=("Arial", 10))
        self.bt_folder_dataset = Button(text='Select folder dataset', bg="gray", fg="blue",
                                        command=self.callback_folder_dataset)
        self.lb_folder_dataset.place(x=100, y=120)
        self.bt_folder_dataset.place(x=800, y=120)
        self.number_thread=1
        self.lb_number_thread = Label(win, text='number threads: ')
        self.et_number_thread = Entry(win, bd=2, foreground="red")
        self.et_number_thread.insert(END, str(self.number_thread))
        self.lb_number_thread.place(x=130, y=230)
        self.et_number_thread.place(x=305, y=230)

        self.b1 = Button(win, text='START', bg="green", fg="white", command=self.start)
        self.b2 = Button(win, text='STOP', bg="red", fg="white", command=self.stop)
        self.b1.place(x=370, y=310)
        self.b2.place(x=440, y=310)

        self.lock_1 = Lock()
        self.list_proxy=[]
        self.list_link=[]
        self.point_proxy=0
        self.point_link=0

        self.running=False

    def start(selfs):
        selfs.running=True
        # executorx = ThreadPoolExecutor(7)
        # executorx.submit()

        selfs.run()

    def stop(self):
        self.running= False

    def run(self):

        self.number_thread=str(self.et_number_thread.get())
        self.folder_dataset = str(self.folder_dataset)
        file_list_proxy= self.folder_dataset+'/proxy.txt'
        file_list_link = self.folder_dataset + '/link.txt'
        open_file_list_proxy = open(file_list_proxy, encoding="utf8")
        self.list_proxy = open_file_list_proxy.readlines()
        open_file_list_link = open(file_list_link, encoding="utf8")
        self.list_link = open_file_list_link.readlines()
        self.list_proxy=[proxy.replace('\n', '').replace(' ','') for proxy in self.list_proxy ]
        self.list_link = [link.replace('\n', '').replace(' ','') for link in self.list_link]

        for i in range(0,int(self.number_thread)):
            print(i,self.number_thread)
            executor = ThreadPoolExecutor(1)
            executor.submit(self.run_in_thread)


    def get_link_and_proxy(self):
        self.lock_1.acquire()
        try:
            self.point_proxy += 1
            if self.point_proxy == len(self.list_proxy):
                self.point_proxy = 0

            self.point_link += 1
            if self.point_link == len(self.list_link):
                self.point_link = 0

            return self.list_proxy[self.point_proxy], self.list_link[self.point_link]
        except Exception as e:
            logging.debug(str(e))
            self.isDone = True
            self.lock_1.release()
        finally:
            print("final")
            self.lock_1.release()
        return None

    def run_in_thread(self):
        try:
            while(True):
                # print("abc")
                # time.sleep(1)
                proxy, link=self.get_link_and_proxy()
                print(proxy,link)
                bot=Bot(proxy,link)
                bot.spam()
        except Exception as e:
            logging.debug(str(e))
            logging.debug("ERROR run_in_thread")

    # def run(self):
    #     executor = ThreadPoolExecutor(1)
    #     executor.submit(self.run_in_thread())



    def callback_folder_dataset(self):
        try:
            self.folder_dataset = fd.askdirectory()
            self.lb_folder_dataset.configure(text=str('Output: ' + self.folder_dataset ))
        except Exception as e:
            logging.debug(str(e))
            logging.debug("ERROR callback_folder_output")


window = Tk()

mywin = MyWindow(window)

window.title('SPAM ADS')
window.geometry("1300x600+10+10")
window.mainloop()
