import tkinter as tk
from tkinter import ttk, messagebox
from datetime import date


"""
Objective: Create an app to track users spending with different categories 
"""


class FinanceTracker:

    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.cost = tk.IntVar()
        self.purchase_type_options = ["Groceries",
                                      "Bills", "Travel",
                                      "Fuel", "Clothing",
                                      "Leisure"]

        self.purchase_type = ttk.Combobox(self.frame, values=self.purchase_type_options, state="readonly")
        self.purchase_type.current(0)
        
        self.cost_label = tk.Label(self.frame, text="Amount")
        self.purchase_label = tk.Label(self.frame, text="Type of expense:")
        self.submit_button = tk.Button(self.frame, command=lambda: self.add_expense(self.date_today,
                                                                                    self.purchase_type.get(),
                                                                                    self.cost_entry.get()),
                                                                                    text="Submit")

        self.cost_entry = tk.Entry(self.frame, textvariable=self.cost)
        self.expenses_view = ttk.Treeview(self.frame, show=["headings"])
        self.expenses_view['columns'] = ('Date', 'Purchase Type', 'Cost')
        self.expenses_view.heading('Date', text='Date')
        self.expenses_view.heading('Purchase Type', text='Purchase Type')
        self.expenses_view.heading('Cost', text='Cost')
        self.date_today = date.today()
        self.expenses_view.pack(side="top", expand=0)
        self.purchase_label.pack(side="left")
        self.purchase_type.pack(side="left")
        self.submit_button.pack(side="right")

        self.cost_entry.pack(side="right")
        self.cost_label.pack(side="right")


        self.frame.pack()


    def add_expense(self, date_today, pur_type, cost):
        try:
            if int(self.cost_entry.get()) >= 1:
                    self.expenses_view.insert("", tk.END, values=(date_today, pur_type, cost))

        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number")
                



if __name__ == "__main__":
    root = tk.Tk()
    root.title("Finance Tracker")
    FinanceTracker(root)
    root.mainloop()
