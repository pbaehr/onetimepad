import Tkinter as tk
import ttk


class App:
    def __init__(self, master):
        self.encode_label = tk.Label(master, text='Encode')
        self.load_plaintext = tk.Button(master, padx=10,
                                        text='Load plaintext...')
        self.save_ciphertext = tk.Button(master, padx=10, state=tk.DISABLED,
                                         text='Save ciphertext...')
        self.save_key = tk.Button(master, padx=10, state=tk.DISABLED,
                                  text='Save key...')

        self.decode_label = tk.Label(master, text='Decode')
        self.load_ciphertext = tk.Button(master, padx=10,
                                         text='Load ciphertext...')
        self.load_key = tk.Button(master, padx=10, text='Load key...')
        self.save_plaintext = tk.Button(master, padx=10, state=tk.DISABLED,
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


if __name__ == '__main__':
    root = tk.Tk()
    root.title('One Time Pad')

    app = App(root)
    root.mainloop()
