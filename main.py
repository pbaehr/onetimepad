import Tkinter as tk
import ttk
import tkFileDialog

from otp import otp_encode, otp_decode


class App:
    encode_plaintext = None
    encode_ciphertext = None
    encode_key = None
    decode_ciphertext = None
    decode_key = None
    decode_plaintext = None

    def __init__(self, master):
        nb = ttk.Notebook(master, name='encode_decode')
        nb.enable_traversal()
        nb.pack(fill=tk.BOTH, expand=tk.Y, padx=5, pady=5)
        padding = {'padx': 5, 'pady': 5}

        encode_frame = ttk.Frame(nb, name='encode')
        self.load_plaintext = ttk.Button(encode_frame,
                                         command=self.do_load_plaintext,
                                         text='Load plaintext...')
        self.save_ciphertext = ttk.Button(encode_frame, state=tk.DISABLED,
                                          command=self.do_save_ciphertext,
                                          text='Save ciphertext...')
        self.save_key = ttk.Button(encode_frame, state=tk.DISABLED,
                                   command=self.do_save_key,
                                   text='Save key...')
        self.load_plaintext.grid(row=0, column=0, columnspan=2, **padding)
        self.save_ciphertext.grid(row=1, column=0, **padding)
        self.save_key.grid(row=1, column=1, **padding)

        decode_frame = ttk.Frame(nb, name='decode')
        self.load_ciphertext = ttk.Button(decode_frame,
                                          command=self.do_load_ciphertext,
                                          text='Load ciphertext...')
        self.load_key = ttk.Button(decode_frame, command=self.do_load_key,
                                   text='Load key...')
        self.save_plaintext = ttk.Button(decode_frame, state=tk.DISABLED,
                                         command=self.do_save_plaintext,
                                         text='Save plaintext...')
        self.load_ciphertext.grid(row=0, column=0, **padding)
        self.load_key.grid(row=0, column=1, **padding)
        self.save_plaintext.grid(row=1, column=0, columnspan=2, **padding)

        nb.add(encode_frame, text='Encode', underline=0, padding=2)
        nb.add(decode_frame, text='Decode', underline=0, padding=2)
        
    def do_load_plaintext(self):
        plaintext_file = tkFileDialog.askopenfile(mode='rb')
        self.encode_plaintext = plaintext_file.read()
        plaintext_file.close()
        self.encode_ciphertext, self.encode_key = otp_encode(self.encode_plaintext)
        self.save_ciphertext['state'] = tk.NORMAL
        self.save_key['state'] = tk.NORMAL

    def do_save_ciphertext(self):
        ciphertext_file = tkFileDialog.asksaveasfile(mode='wb')
        ciphertext_file.write(self.encode_ciphertext)
        ciphertext_file.close()

    def do_save_key(self):
        key_file = tkFileDialog.asksaveasfile(mode='wb')
        key_file.write(self.encode_key)
        key_file.close()

    def do_load_ciphertext(self):
        ciphertext_file = tkFileDialog.askopenfile(mode='rb')
        self.decode_ciphertext = ciphertext_file.read()
        ciphertext_file.close()
        if self.decode_key:
            self.decode_plaintext = otp_decode(self.decode_ciphertext,
                                               self.decode_key)
            self.save_plaintext['state'] = tk.NORMAL

    def do_load_key(self):
        key_file = tkFileDialog.askopenfile(mode='rb')
        self.decode_key = key_file.read()
        key_file.close()
        if self.decode_ciphertext:
            self.decode_plaintext = otp_decode(self.decode_ciphertext,
                                               self.decode_key)
            self.save_plaintext['state'] = tk.NORMAL

    def do_save_plaintext(self):
        plaintext_file = tkFileDialog.asksaveasfile(mode='wb')
        plaintext_file.write(self.decode_plaintext)
        plaintext_file.close()


if __name__ == '__main__':
    root = tk.Tk()
    root.title('One Time Pad')

    app = App(root)
    root.mainloop()
