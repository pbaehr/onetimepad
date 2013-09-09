import Tkinter as tk


class App:
    def __init__(self, master):
        tk.Button(master, text='Load plaintext file...').grid(row=0, column=0, columnspan=2)
        tk.Button(master, text='Load key file...').grid(row=1, column=0)
        tk.Button(master, text='Load ciphertext file...').grid(row=1, column=1)
        

if __name__ == '__main__':
    root = tk.Tk()
    root.title('One Time Pad')

    app = App(root)
    root.mainloop()
