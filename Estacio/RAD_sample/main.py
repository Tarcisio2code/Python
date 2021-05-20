import tkinter as tk
from tkinter import ttk
import pandas as pd
# install lib openpyxl for xlsx files

class ComponentsRAD:
    def __init__(self, window):
        self.lblName = tk.Label(window, text='Students Name:')
        self.lblFirstGrade = tk.Label(window, text='Grade 1:')
        self.lblSecondGrade = tk.Label(window, text='Grade 2:')
        self.txtName = tk.Entry(bd=3)
        self.txtFirstGrade = tk.Entry()
        self.txtSecondGrade = tk.Entry()
        self.btnCalcAverage = tk.Button(window, text='Calculate Average', command=self.fAverageCalculator)

        self.ColumnsData = ("Student", "First Grade", "Second Grade", "Average", "Status")
        self.treeStudents = ttk.Treeview(window, columns=self.ColumnsData, selectmode='browse')

        self.vScrollbar = ttk.Scrollbar(window, orient='vertical', command=self.treeStudents.yview)
        self.vScrollbar.pack(side='right', fill='x')
        self.treeStudents.configure(yscrollcommand=self.vScrollbar.set)

        self.treeStudents.heading("Student", text="Student")
        self.treeStudents.heading("First Grade", text="First Grade")
        self.treeStudents.heading("Second Grade", text="Second Grade")
        self.treeStudents.heading("Average", text="Average")
        self.treeStudents.heading("Status", text="Status")

        self.treeStudents.column("#0", minwidth=0, width=0)
        self.treeStudents.column("Student", minwidth=0, width=200)
        self.treeStudents.column("First Grade", anchor='center', minwidth=0, width=90)
        self.treeStudents.column("Second Grade", anchor='center', minwidth=0, width=90)
        self.treeStudents.column("Average", anchor='center', minwidth=0, width=90)
        self.treeStudents.column("Status", minwidth=0, width=200)

        self.lblName.place(x=100, y=50)
        self.txtName.place(x=200, y=50)

        self.lblFirstGrade.place(x=100, y=100)
        self.txtFirstGrade.place(x=200, y=100)

        self.lblSecondGrade.place(x=100, y=150)
        self.txtSecondGrade.place(x=200, y=150)

        self.btnCalcAverage.place(x=100, y=200)

        self.treeStudents.place(x=100, y=250)
        self.vScrollbar.place(x=780, y=250, height=225)

        self.id = 0
        self.iid = 0
        self.fLoadStartData()

    #
    def fLoadStartData(self):
        try:
            source = 'datasource.xlsx'
            data = pd.read_excel(source, engine='openpyxl')
            lastrow = len(data['Student'])
            for row in range(lastrow):
                name = data['Student'][row]
                firstgrade = str(data['First Grade'][row])
                secondgrade = str(data['Second Grade'][row])
                average = str(data['Average'][row])
                status = data['Status'][row]
                self.treeStudents.insert('', 'end',
                                         iid=self.iid,
                                         values=(name,
                                                 firstgrade,
                                                 secondgrade,
                                                 average,
                                                 status))
                self.iid = self.iid + 1
                self.id = self.id + 1
        except:
            print('No data to load')

    def fAverageCalculator(self):
        try:
            name = self.txtName.get()
            firstgrade = float(self.txtFirstGrade.get())
            secondgrade = float(self.txtSecondGrade.get())
            average, status = self.fStatusCheck(firstgrade, secondgrade)
            self.treeStudents.insert('', 'end',
                                     iid=self.iid,
                                     values=(name,
                                             str(firstgrade),
                                             str(secondgrade),
                                             str(average),
                                             status))
            self.iid = self.iid + 1
            self.id = self.id + 1
            self.fDataSave()
        except ValueError:
            print('Entre com valores válidos')
        finally:
            self.txtName.delete(0, 'end')
            self.txtFirstGrade.delete(0, 'end')
            self.txtSecondGrade.delete(0, 'end')

    #
    def fDataSave(self):
        try:
            source = 'datasource.xlsx'
            data = []

            for line in self.treeStudents.get_children():
                content = []
                for value in self.treeStudents.item(line)['values']:
                    content.append(value)
                data.append(content)
            df = pd.DataFrame(data=data, columns=self.ColumnsData)

            spreadsheet = pd.ExcelWriter(source)
            df.to_excel(spreadsheet, 'data', index=False)

            spreadsheet.save()
        except:
            print('Error to data save')

    def fStatusCheck(self, firstgrade, secondgrade):
        average = (firstgrade + secondgrade) / 2
        if average >= 7:
            status = 'Approved'
        elif average >= 5:
            status = 'Recovering'
        else:
            status = 'Disapproved'
        return average, status


# Main process
window = tk.Tk()
components = ComponentsRAD(window)
window.title('Wellcome to RAD')
window.geometry("820x600+400+200")
window.mainloop()
