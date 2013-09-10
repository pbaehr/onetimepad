import Tkinter as tk
import ttk
import tkFileDialog

from otp import otp_encode, otp_decode


class App:
    plaintext = None
    ciphertext = None
    key = None

    def __init__(self, master):
        self.encode_label = tk.Label(master, text='Encode')
        self.load_plaintext = tk.Button(master, padx=10,
                                        command=self.do_load_plaintext,
                                        text='Load plaintext...')
        self.save_ciphertext = tk.Button(master, padx=10, state=tk.DISABLED,
                                         command=self.do_save_ciphertext,
                                         text='Save ciphertext...')
        self.save_key = tk.Button(master, padx=10, state=tk.DISABLED,
                                  command=self.do_save_key,
                                  text='Save key...')

        self.decode_label = tk.Label(master, text='Decode')
        self.load_ciphertext = tk.Button(master, padx=10,
                                         command=self.do_load_ciphertext,
                                         text='Load ciphertext...')
        self.load_key = tk.Button(master, padx=10, command=self.do_load_key,
                                  text='Load key...')
        self.save_plaintext = tk.Button(master, padx=10, state=tk.DISABLED,
                                        command=self.do_save_plaintext,
                                        text='Save plaintext...')
        self.divider = ttk.Separator(master)

        self.encode_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
        self.divider.grid(row=0, column=2, rowspan=3, sticky='ns')
        self.decode_label.grid(row=0, column=3, columnspan=2, padx=5, pady=5)
        self.load_plaintext.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
        self.load_ciphertext.grid(row=1, column=3, padx=5, pady=5)
        self.load_key.grid(row=1, column=4, padx=5, pady=5)
        self.save_ciphertext.grid(row=2, column=0, padx=5, pady=5)
        self.save_key.grid(row=2, column=1, padx=5, pady=5)
        self.save_plaintext.grid(row=2, column=3, columnspan=2, padx=5, pady=5)

    def do_load_plaintext(self):
        plaintext_file = tkFileDialog.askopenfile(mode='rb')
        self.plaintext = plaintext_file.read()
        plaintext_file.close()
        self.ciphertext, self.key = otp_encode(self.plaintext)
        self.save_ciphertext['state'] = tk.NORMAL
        self.save_key['state'] = tk.NORMAL

    def do_save_ciphertext(self):
        ciphertext_file = tkFileDialog.asksaveasfile(mode='wb')
        ciphertext_file.write(self.ciphertext)
        ciphertext_file.close()

    def do_save_key(self):
        key_file = tkFileDialog.asksaveasfile(mode='wb')
        key_file.write(self.key)
        key_file.close()

    def do_load_ciphertext(self):
        ciphertext_file = tkFileDialog.askopenfile(mode='rb')
        self.ciphertext = ciphertext_file.read()
        ciphertext_file.close()
        if self.key:
            self.plaintext = otp_decode(self.ciphertext, self.key)
            self.save_plaintext['state'] = tk.NORMAL

    def do_load_key(self):
        key_file = tkFileDialog.askopenfile(mode='rb')
        self.key = key_file.read()
        key_file.close()
        if self.ciphertext:
            self.plaintext = otp_decode(self.ciphertext, self.key)
            self.save_plaintext['state'] = tk.NORMAL

    def do_save_plaintext(self):
        plaintext_file = tkFileDialog.asksaveasfile(mode='wb')
        plaintext_file.write(self.plaintext)
        plaintext_file.close()


if __name__ == '__main__':
    root = tk.Tk()
    root.title('One Time Pad')

    app = App(root)
    root.mainloop()
