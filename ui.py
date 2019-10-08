import tkinter as tk
import send
import receive

def main():
    window = tk.Tk()
    window.title('我的sqs服务')
    window.geometry('400x340')
    e = tk.Entry(window, font=('Arial', 9), width=42)
    e.grid(row=1, column=0)
    l1 = tk.Label(text="url:", height=1, width=6)
    l1.grid(row=0, column=0, sticky='w')

    e1 = tk.Entry(window, font=('Arial', 14), width=36)
    e1.grid(row=3, column=0)
    def get_m():
        m = e1.get()  # 获取文本框内容
        url = e.get()
        send.send(m, url)
        print(m)
    b1 = tk.Button(window, text='send', font=('Arial', 12), width=10, height=1,
                  command=get_m)
    b1.grid(row=4, column=0, sticky='w')

    t2 = tk.Text(window, font=('Arial', 14), width=36, height=10)
    t2.grid(row=2, column=0)

    def display_m():
        url = e.get()
        n = receive.receive(url)
        t2.insert('1.0', n)
        print(n)

    b2 = tk.Button(window, text='receive', font=('Arial', 12), width=10, height=1,
                   command=display_m)
    b2.grid(row=4, column=0, sticky='e')
    window.mainloop()

if __name__ == '__main__':
    print('1')
    main()
