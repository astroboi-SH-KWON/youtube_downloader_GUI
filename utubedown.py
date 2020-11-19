from tkinter import *
from tkinter import messagebox
from pytube import YouTube
import os

############### st to set env ################
window = None
url_label = None
url_input = None
res_text = None

############### en to set env ################


def setupGUI():
    global window
    global url_label
    global url_input
    global res_text

    window = Tk()
    window.title('Utube DownLoader by pytube 4.0')

    url_label = Label(window, text='YouTube url', font='Courier 10 bold', relief=RAISED)
    url_label.grid(row=0, column=0, padx=5, pady=5)
    url_input = Entry(window, font='Terminal 10', width=50)
    url_input.grid(row=0, column=1, padx=3, pady=3)

    download_btn = Button(window, text='down\nload', font='Courier 20 bold', command=click_dn_btn, height=10)
    download_btn.grid(rowspan=1, column=2, padx=3, pady=3)

    reset_btn = Button(window, text='reset', font='Courier 10 bold', bg='yellow', fg='red', command=reset)
    reset_btn.grid(row=2, column=2, padx=3, pady=3)

    res_text = Text(window, font='Terminal 10', relief=RAISED, width=60, height=30)
    res_text.grid(row=1, columnspan=2, padx=5, pady=5)


def clear_Text(res_txt):
    if res_txt.get('1.0', END) != '':
        res_txt.delete('1.0', END)


def valid_input(url):
    if url == '':
        messagebox.showerror('error', 'check url')
        return False
    else:
        return True

def reset():
    global url_input
    global res_text

    url_input.delete(0, 'end')
    clear_Text(res_text)

def click_dn_btn():
    global res_text
    clear_Text(res_text)
    res_text.insert(CURRENT, 'checking url...\n\n')
    download_youtube()

def download_youtube():
    global url_input
    global res_text

    url = url_input.get().replace(' ', '')

    if valid_input(url):
        try:
            youTube_vid = YouTube(url)
            res_text.insert(CURRENT, 'title : ' + youTube_vid.title + '\n')
            my_vid = youTube_vid.streams.get_highest_resolution()
            res_text.insert(CURRENT, 'make output folder\n')
            os.makedirs('./output/', exist_ok=True)
            res_text.insert(CURRENT, 'downloading...\n')
            my_vid.download('./output/')
            res_text.insert(CURRENT, 'DONE.\n\n')
            res_text.insert(CURRENT, 'youtube clip path\n ' + os.getcwd() + '\\output\n\n')

        except Exception as err:
            res_text.insert(CURRENT, 'error : \n' + str(err) + '\n')


if __name__ == '__main__':
    setupGUI()
    window.mainloop()