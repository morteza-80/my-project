import tkinter as tk
from tkinter import ttk
import ttkbootstrap as tb
from googletrans import Translator
from gtts import gTTS
from playsound import playsound
import os

# اطلاعات کاربری
REGISTERED_USERNAME = "morteza"
REGISTERED_PASSWORD = "12345"  # رمز پیش‌فرض

def login():
    username = username_var.get()
    password = password_var.get()
    
    if username == REGISTERED_USERNAME and password == REGISTERED_PASSWORD:
        frame1.pack_forget()
        frame2.pack(fill="both", expand=True)
    else:
        error_label.config(text="نام کاربری یا رمز عبور اشتباه است!", foreground="red")

def translate_text():
    translator = Translator()
    input_text = input_text_var.get("1.0", "end-1c")  # دریافت متن از باکس بالایی
    selected_language = language_var.get()  # زبان انتخابی
    
    if input_text.strip():
        # ترجمه متن
        translated = translator.translate(input_text, src='fa', dest=selected_language)
        output_text_var.delete("1.0", "end")
        output_text_var.insert("1.0", translated.text)
    else:
        output_text_var.delete("1.0", "end")
        output_text_var.insert("1.0", "لطفاً متنی وارد کنید.")

def play_audio():
    input_text = output_text_var.get("1.0", "end-1c")  # دریافت متن از باکس پایین
    selected_language = language_var.get()  # زبان انتخابی
    
    if input_text.strip():
        # تبدیل متن به صدا
        tts = gTTS(text=input_text, lang=selected_language)
        tts.save("translation.mp3")
        playsound("translation.mp3")
        os.remove("translation.mp3")
    else:
        output_text_var.delete("1.0", "end")
        output_text_var.insert("1.0", "لطفاً متنی وارد کنید.")

# ایجاد پنجره اصلی
app = tb.Window(themename="darkly")
app.title("Multi Page Application")
app.geometry("400x500")

# صفحه اول
frame1 = ttk.Frame(app)
frame1.pack(fill="both", expand=True)

# تصویر
photo = tk.PhotoImage(file=r"C:\Users\user\Desktop\german 1\python-logo.png")  # مسیر تصویر خود را جایگزین کنید
photo_label = ttk.Label(frame1, image=photo)
photo_label.pack(pady=10)

# فیلد نام کاربری
username_var = tk.StringVar()
username_entry = ttk.Entry(frame1, textvariable=username_var, font=("Helvetica", 12), width=25)
username_entry.pack(pady=5)
username_entry.insert(0, "نام کاربری")

# فیلد رمز عبور
password_var = tk.StringVar()
password_entry = ttk.Entry(frame1, textvariable=password_var, font=("Helvetica", 12), width=25, show="*")
password_entry.pack(pady=5)
password_entry.insert(0, "رمز عبور")

# دکمه ورود
login_button = ttk.Button(frame1, text="ورود", command=login)
login_button.pack(pady=5)

# برچسب خطا
error_label = ttk.Label(frame1, text="", font=("Helvetica", 10))
error_label.pack()

# صفحه دوم
frame2 = ttk.Frame(app)

# انتخاب زبان مقصد
language_var = tk.StringVar(value="en")
language_label = ttk.Label(frame2, text="انتخاب زبان:")
language_label.pack(pady=5)
language_combobox = ttk.Combobox(frame2, textvariable=language_var, values=["en", "de"], state="readonly")
language_combobox.pack(pady=5)

# باکس ورود متن
input_text_var = tk.Text(frame2, height=5, width=40, font=("Helvetica", 12))
input_text_var.pack(pady=10)
input_text_var.insert("1.0", "سلام دنیا! این یک متن فارسی ساده است.")

# باکس نمایش ترجمه
output_text_var = tk.Text(frame2, height=5, width=40, font=("Helvetica", 12), state="normal")
output_text_var.pack(pady=10)

# دکمه‌های ترجمه، پخش صدا، پاک کردن و خروج
translate_button = ttk.Button(frame2, text="ترجمه", command=translate_text)
translate_button.pack(side="left", padx=10, pady=10)

audio_button = ttk.Button(frame2, text="پخش صدا", command=play_audio)
audio_button.pack(side="left", padx=10, pady=10)

clear_button = ttk.Button(frame2, text="پاک کردن", command=lambda: [input_text_var.delete("1.0", "end"), output_text_var.delete("1.0", "end")])
clear_button.pack(side="left", padx=10, pady=10)

exit_button = ttk.Button(frame2, text="خروج", command=app.quit)
exit_button.pack(side="left", padx=10, pady=10)

# اجرای برنامه
app.mainloop()