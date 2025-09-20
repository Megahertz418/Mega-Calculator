from tkinter import *
import re, os, sys

# برای دسترسی به فایل‌ها داخل پکیج onefile
def resource_path(rel_path: str) -> str:
    base = getattr(sys, "_MEIPASS", os.path.abspath("."))
    return os.path.join(base, rel_path)

window = Tk()
window.title("MegaCalculator")
window.configure(bg="black")
window.resizable(False, False)

# --- آیکون پنجره (اول .ico، اگر نبود PNG) ---
try:
    ico_path = resource_path(os.path.join("assets", "Calculator.ico"))
    if os.path.exists(ico_path):
        window.iconbitmap(ico_path)             # بهترین حالت ویندوز
    else:
        png_path = resource_path(os.path.join("assets", "Calculator.png"))
        if os.path.exists(png_path):
            window.iconphoto(True, PhotoImage(file=png_path))  # fallback
except Exception:
    pass

def click(num):
    display.insert(END, num)

def do_equal():
    expr = display.get()
    # فقط ارقام و عملگرهای مجاز
    if not re.fullmatch(r"[0-9+\-*/(). ]*", expr):
        display.delete(0, END); display.insert(END, "Err"); return
    try:
        result = eval(expr)
    except Exception:
        result = "Err"
    display.delete(0, END)
    display.insert(END, result)

def do_clear():
    display.delete(0, END)

def do_backspace():
    e = display.get()
    if e:
        display.delete(len(e)-1, END)

display = Entry(window, bg="black", fg="white", bd=10, font=("DOSIS Semi Bold", 27), justify="left")
display.grid(row=0, column=0, columnspan=4)

btn0 = Button(window, text="0", bg="black", fg="white", activebackground="lightblue", font=("DOSIS Semi Bold", 35), command=lambda: click("0"))
btn1 = Button(window, text="1", bg="black", fg="white", activebackground="lightblue", font=("DOSIS Semi Bold", 35), command=lambda: click("1"))
btn2 = Button(window, text="2", bg="black", fg="white", activebackground="lightblue", font=("DOSIS Semi Bold", 35), command=lambda: click("2"))
btn3 = Button(window, text="3", bg="black", fg="white", activebackground="lightblue", font=("DOSIS Semi Bold", 35), command=lambda: click("3"))
btn4 = Button(window, text="4", bg="black", fg="white", activebackground="lightblue", font=("DOSIS Semi Bold", 35), command=lambda: click("4"))
btn5 = Button(window, text="5", bg="black", fg="white", activebackground="lightblue", font=("DOSIS Semi Bold", 35), command=lambda: click("5"))
btn6 = Button(window, text="6", bg="black", fg="white", activebackground="lightblue", font=("DOSIS Semi Bold", 35), command=lambda: click("6"))
btn7 = Button(window, text="7", bg="black", fg="white", activebackground="lightblue", font=("DOSIS Semi Bold", 35), command=lambda: click("7"))
btn8 = Button(window, text="8", bg="black", fg="white", activebackground="lightblue", font=("DOSIS Semi Bold", 35), command=lambda: click("8"))
btn9 = Button(window, text="9", bg="black", fg="white", activebackground="lightblue", font=("DOSIS Semi Bold", 35), command=lambda: click("9"))

btnPlus  = Button(window, text="+", bg="black", fg="orange", activebackground="orange", font=("DOSIS Semi Bold", 35), command=lambda: click("+"))
btnMinus = Button(window, text="-", bg="black", fg="orange", activebackground="orange", font=("DOSIS Semi Bold", 35), command=lambda: click("-"))
btnMul   = Button(window, text="×", bg="black", fg="orange", activebackground="orange", font=("DOSIS Semi Bold", 35), command=lambda: click("*"))
btnDiv   = Button(window, text="÷", bg="black", fg="orange", activebackground="orange", font=("DOSIS Semi Bold", 35), command=lambda: click("/"))
btnDot   = Button(window, text=".", bg="black", fg="orange", activebackground="orange", font=("DOSIS Semi Bold", 35), command=lambda: click("."))

btnEqual = Button(window, text="=", bg="black", fg="lightgreen", activebackground="lightgreen", font=("DOSIS Semi Bold", 35), command=do_equal)
btnClear = Button(window, text="C", bg="black", fg="yellow", activebackground="yellow", font=("DOSIS Semi Bold", 35), command=do_clear)
btnBack  = Button(window, text="\u232b", bg="black", fg="red", activebackground="red", font=("DOSIS Semi Bold", 20), command=do_backspace)

# همان چیدمان قبلی
btn0.grid(row=5, column=1, sticky="news")
btn1.grid(row=4, column=0, sticky="news")
btn2.grid(row=4, column=1, sticky="news")
btn3.grid(row=4, column=2, sticky="news")
btn4.grid(row=3, column=0, sticky="news")
btn5.grid(row=3, column=1, sticky="news")
btn6.grid(row=3, column=2, sticky="news")
btn7.grid(row=2, column=0, sticky="news")
btn8.grid(row=2, column=1, sticky="news")
btn9.grid(row=2, column=2, sticky="news")

btnPlus.grid(row=2, column=3, rowspan=2, sticky="news")
btnMinus.grid(row=1, column=2, sticky="news")
btnMul.grid(row=1, column=1, sticky="news")
btnDiv.grid(row=1, column=0, sticky="news")
btnDot.grid(row=5, column=2, sticky="news")

btnEqual.grid(row=4, column=3, rowspan=2, sticky="news")
btnClear.grid(row=5, column=0, sticky="news")
btnBack.grid(row=1, column=3, sticky="news")

window.mainloop()