import tkinter as tk
from tkinter import messagebox

def convert_and_display(input_field, output_field, conversion_func):
    try:
        value = input_field.get()
        result = conversion_func(value)
        output_field.delete(0, tk.END)
        output_field.insert(tk.END, str(result))
    except ValueError as e:
        messagebox.showerror("输入错误", f"输入错误：{e}")

def decimal_to_binary(decimal_str):
    return bin(int(decimal_str))[2:]

def binary_to_decimal(binary_str):
    return int(binary_str, 2)

def char_to_ascii(char_str):
    return ord(char_str)

def ascii_to_char(ascii_str):
    return chr(int(ascii_str))

# 创建主窗口
root = tk.Tk()
root.title("编码解码辅助工具")
root.geometry("600x300")

# 创建标签和输入框
widgets = {}
for i, (label_text, command, conversion_func) in enumerate([
    ("十进制数:", "十进制转二进制", decimal_to_binary),
    ("二进制数:", "二进制转十进制", binary_to_decimal),
    ("字符:", "字符转十进制数", char_to_ascii),
    ("十进制数:", "十进制数转字符", ascii_to_char)
]):
    label = tk.Label(root, text=label_text)
    entry = tk.Entry(root)
    result = tk.Entry(root)
    
    button = tk.Button(root, text=command, command=lambda e=entry, r=result, c=conversion_func: convert_and_display(e, r, c))
    
    label.grid(row=i, column=0, padx=10, pady=5)
    entry.grid(row=i, column=1, padx=10, pady=5)
    result.grid(row=i, column=3, padx=10, pady=5)
    button.grid(row=i, column=2, padx=10, pady=5)

widgets['entry'] = [entry, result]
widgets['label'] = [label, button]

# 运行主循环
root.mainloop()