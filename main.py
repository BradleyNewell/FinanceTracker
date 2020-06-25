import tkinter as tk
from tkinter import ttk, messagebox
from datetime import date



class FinanceTracker:

    def __init__(self, master):

        # GUI Setup

        self.master = master
        self.frame = tk.Frame(self.master)
        self.cost = tk.IntVar()

        # Configuration for the combobox widget

        self.purchase_type_options = ["Groceries",
                                      "Bills", "Travel",
                                      "Fuel", "Clothing",
                                      "Leisure"]

        self.purchase_type = ttk.Combobox(self.frame, values=self.purchase_type_options, state="readonly")
        self.purchase_type.current(0)
        
        # Input field to obtain the cost of an entry

        self.cost_label = tk.Label(self.frame, text="Amount")
        self.purchase_label = tk.Label(self.frame, text="Type of expense:")

        # Button to add a new entry to the tree

        self.submit_button = tk.Button(self.frame, command=lambda: self.add_expense(self.date_today,
                                                                                    self.purchase_type.get(),
                                                                                    self.cost_entry.get()),
                                                                                    text="Submit")

        self.cost_entry = tk.Entry(self.frame, textvariable=self.cost)

        # Configuring Treeview for user input

        self.expenses_view = ttk.Treeview(self.frame, show=["headings"])
        self.expenses_view['columns'] = ('Date', 'Purchase Type', 'Cost')
        self.expenses_view.heading('Date', text='Date')
        self.expenses_view.heading('Purchase Type', text='Purchase Type')
        self.expenses_view.heading('Cost', text='Cost')
        self.show_previous()

        # Creating date object to accompany user input in the tree

        self.date_today = date.today()

        # Packing elements to frame and setting locations

        self.expenses_view.pack(side="top", expand=0)
        self.purchase_label.pack(side="left")
        self.purchase_type.pack(side="left")
        self.submit_button.pack(side="right")
        self.cost_entry.pack(side="right")
        self.cost_label.pack(side="right")
        self.frame.pack()

    """Reads CSV file for existing entries, formats the data to be displayed in the Tree,
       if no CSV file is found a new one is created."""
    def show_previous(self):
        try:
            file = open("user_finances.csv")
            data = [row for row in reader(file)]
            for entry in data:
                self.expenses_view.insert("", tk.END, values=(entry))
        except FileNotFoundError:
            open("user_finances.csv", "a+")
            self.show_previous()

    
    """ Add and format new entries to the tree, checks user input, writes entries to CSV """

    def add_expense(self, date_today, pur_type, cost):
        try:
            if int(self.cost_entry.get()) >= 1:
                    self.expenses_view.insert("", tk.END, values=(date_today, pur_type, cost))
                    formatted_values = [date_today, pur_type, cost]
                    with open('user_finances.csv', 'a', newline='') as write_to:
                        csv_writer = writer(write_to)
                        csv_writer.writerow(formatted_values)

        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number")
                



if __name__ == "__main__":

    root = tk.Tk()
    root.title("Finance Tracker")
    FinanceTracker(root)
    root.mainloop()
