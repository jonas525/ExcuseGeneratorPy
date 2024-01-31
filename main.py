import tkinter as tk
import mysql.connector
import random

# Function to generate an excuse
def generate_excuse():
    random_excuse = random.choice(excuses)[0]
    print("Excuse: ", random_excuse, )
    label_result.config(text=random_excuse, font=('Arial', 13))
   
# Database connection
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="Excuse"
)

cursor = connection.cursor()

# Fetch excuses from the database
cursor.execute("SELECT excuse_description FROM excuse_text")
excuses = cursor.fetchall()

#GUI setup
root = tk.Tk()
root.geometry("650x420")
root.resizable(False, False)
root.title("ExcuseGeneratorPy")

# Label for the title
label = tk.Label(root, text="Excuse Generator", font=('Arial', 18))
label.pack()

# Label to display the generated excuse
label_result = tk.Label(root, text="")
label_result.pack(pady=150)

#Button to generate excuses
button = tk.Button(root, text="Generate Excuse", font=('Arial', 20), command=generate_excuse)
button.pack(side=tk.BOTTOM, pady =(20,10))

#SQL database connection close
connection.close()

# Run the main event loop
root.mainloop()