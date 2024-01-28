import tkinter as tk


root = tk.Tk()
root.geometry("400x400")
root.resizable(False, False)



label = tk.Label(root, text="ExcuseGeneratorPy", font=('Arial', 18))
label.pack()

button = tk.Button(root, text="Generate Excuse", font=('Arial', 18))
button.pack(side=tk.BOTTOM, pady =(20,20))

root.mainloop()
