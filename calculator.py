import tkinter as tk

def on_click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result.set(eval(entry.get()))
        except Exception:
            result.set("Error")
    elif text == "C":
        result.set("")
    else:
        result.set(result.get() + text)

root = tk.Tk()
root.title("Calculator")

result = tk.StringVar()
entry = tk.Entry(root, textvar=result, font="Arial 20", justify="right")
entry.grid(row=0, column=0, columnspan=4)

buttons = ["7", "8", "9", "/",
           "4", "5", "6", "*",
           "1", "2", "3", "-",
           "C", "0", "=", "+"]

for i, btn in enumerate(buttons):
    b = tk.Button(root, text=btn, font="Arial 20", height=2, width=5)
    b.grid(row=i//4+1, column=i%4)
    b.bind("<Button-1>", on_click)

root.mainloop()