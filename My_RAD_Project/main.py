from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
import pandas as pd


# Methods
def exit_app():
    if mb.askyesno('Alert', 'Are you sure ?'):
        root.destroy()


# Class
class AppComponents:
    def __init__(self, window):
        # Labels background color
        fg_color = 'white'
        bg_color = 'gray'
        #  Style
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('Treeview', rowheight=30)
        # Canvas
        self.appCanvas = Canvas(window, width=800, height=600, highlightthickness=0)
        self.appCanvas.grid(row=0, column=0)
        # TreeView
        self.appTree = ttk.Treeview(window)
        self.iid = 0
        self.columnsHeader = ("Student", "First Note", "Second Note", "Average", "Status")
        self.get_data()
        self.appTree['columns'] = self.columnsHeader
        self.appTree.column("#0", width=0, stretch='no')
        for col in range(len(self.columnsHeader)):
            self.appTree.heading(col, text=self.columnsHeader[col])
            self.appTree.column(col, width=150)
            if col in range(1, 4):
                self.appTree.column(col, anchor='center')
        self.appTreeScroll = ttk.Scrollbar(window,
                                           orient="vertical",
                                           command=self.appTree.yview)
        self.appTree.configure(yscrollcommand=self.appTreeScroll.set)
        self.appTree.bind("<<TreeviewSelect>>", self.selected_item)

        # Entry box
        self.student = StringVar()
        self.note1 = StringVar()
        self.note2 = StringVar()
        self.boxStudent = Entry(width=24, textvariable=self.student)
        self.boxNote1 = Entry(width=24, justify='center', textvariable=self.note1)
        self.boxNote2 = Entry(width=24, justify='center', textvariable=self.note2)

        # Buttons
        self.btnClearFields = Button(window, text='Clear', width=20, command=self.call_clear_fields)
        self.btnCalcAverage = Button(window, text='Calculate Average', width=20,
                                     command=self.calc_average)
        self.btnAdd = Button(window, text='Add Record', width=20, command=self.add_record)
        self.btnUpdate = Button(window, text='Update Record', width=20, state='disable',
                                command=self.update_record)
        self.btnDelete = Button(window, text='Delete Record', width=20, state='disable',
                                command=self.delete_record)
        self.btnExit = Button(window, text='Exit', width=20, command=exit_app)

        # Labels
        lbl_font1 = 'Helvetica 12 bold'
        lbl_font2 = 'Helvetica 9 italic'
        self.lblAverage = Label(window, width=22, anchor='center', relief='sunken')
        self.lblStatus = Label(window, width=21, anchor='w', relief='sunken')
        self.lblTotalStudents = Label(window, text='Total of Students', font=lbl_font1, fg=fg_color, bg=bg_color)
        self.lblTotalStudentsValue = Label(window, width=15, anchor='center', font=lbl_font1, fg=fg_color, bg=bg_color)
        self.lblCountApproved = Label(window, text='Students Approved', font=lbl_font2, fg=fg_color, bg=bg_color)
        self.lblCountApprovedValue = Label(window, width=20, anchor='center', font=lbl_font2, fg=fg_color, bg=bg_color)
        self.lblCountDisapproved = Label(window, text='Students Disapproved', font=lbl_font2, fg=fg_color, bg=bg_color)
        self.lblCountDisapprovedValue = Label(window, width=20, anchor='center', font=lbl_font2, fg=fg_color, bg=bg_color)
        self.lblCountRecovering = Label(window, text='Students Recovering', font=lbl_font2, fg=fg_color, bg=bg_color)
        self.lblCountRecoveringValue = Label(window, width=20, anchor='center', font=lbl_font2, fg=fg_color, bg=bg_color)

        # Place widgets
        self.appTree.place(x=20, y=20)
        self.appTreeScroll.place(x=775, y=20, height=330)

        self.boxStudent.place(x=20, y=353)
        self.boxNote1.place(x=170, y=353)
        self.boxNote2.place(x=320, y=353)
        self.lblAverage.place(x=470, y=353)
        self.lblStatus.place(x=620, y=353)

        self.btnClearFields.place(x=20, y=385)
        self.btnCalcAverage.place(x=180, y=385)
        self.btnAdd.place(x=20, y=420)
        self.btnUpdate.place(x=180, y=420)
        self.btnDelete.place(x=20, y=455)
        self.btnExit.place(x=180, y=455)

        self.lblTotalStudents.place(x=480, y=400)
        self.lblCountApproved.place(x=480, y=435)
        self.lblCountRecovering.place(x=480, y=470)
        self.lblCountDisapproved.place(x=480, y=505)
        #
        self.lblTotalStudentsValue.place(x=620, y=400)
        self.lblCountApprovedValue.place(x=620, y=435)
        self.lblCountRecoveringValue.place(x=620, y=470)
        self.lblCountDisapprovedValue.place(x=620, y=505)

        self.appCanvas.create_line(480, 425, 710, 425, fill=fg_color)
        self.appCanvas.create_line(480, 460, 710, 460, fill=fg_color)
        self.appCanvas.create_line(480, 500, 710, 500, fill=fg_color)
        self.appCanvas.configure(bg=bg_color)

        self.show_statistics()

    # Functions
    def get_data(self):
        try:
            dataframe = pd.read_excel('datasource.xlsx', engine='openpyxl')
            last_row = dataframe.shape[0]

            if last_row > 0:
                for row in range(last_row):
                    df_values = list(dataframe.values[row])
                    self.appTree.insert('', 'end', iid=self.iid, values=df_values)
                    self.iid = self.iid + 1

        except ValueError:
            self.columnsHeader = ("", "", "", "", "")
            mb.showerror('Alert', 'Error on trying to load Data Base')

    def selected_item(self, event):
        if self.btnAdd['state'] == 'normal':
            self.btnAdd['state'] = 'disable'
            self.btnUpdate['state'] = 'normal'
            self.btnDelete['state'] = 'normal'

        selected = self.appTree.focus()
        values = self.appTree.item(selected, 'values')
        self.student.set(values[0])
        self.note1.set(values[1])
        self.note2.set(values[2])
        self.lblAverage['text'] = values[3]
        self.lblStatus['text'] = values[4]

    def show_statistics(self):
        count_student = len(self.appTree.get_children())
        # count_student = self.iid
        self.lblTotalStudentsValue['text'] = ''
        self.lblCountApprovedValue['text'] = ''
        self.lblCountDisapprovedValue['text'] = ''
        self.lblCountRecoveringValue['text'] = ''
        status = []
        if count_student > 0:
            for item in self.appTree.get_children():
                status.append(self.appTree.item(item)['values'][4])

                count_approved = status.count('Approved')
                count_disapproved = status.count('Disapproved')
                count_recovering = status.count('Recovering')

                self.lblTotalStudentsValue['text'] = count_student
                self.lblCountApprovedValue['text'] = format(count_approved / count_student, '.0%')
                self.lblCountDisapprovedValue['text'] = format(count_disapproved / count_student, '.0%')
                self.lblCountRecoveringValue['text'] = format(count_recovering / count_student, '.0%')

    def clean_fields(self):
        try:
            if self.btnUpdate['state'] == 'normal':
                self.btnUpdate['state'] = 'disable'
                self.btnDelete['state'] = 'disable'
                self.btnAdd['state'] = 'normal'

            self.boxStudent.delete(0, 'end')
            self.boxNote1.delete(0, 'end')
            self.boxNote2.delete(0, 'end')
            self.lblAverage['text'] = ''
            self.lblStatus['text'] = ''
            self.boxStudent.focus_set()
            self.show_statistics()

        except ValueError:
            mb.showerror('Error', 'Error when trying to clean fields')

    def call_clear_fields(self):
        if mb.askyesno('Alert', 'Clear all input fields'):
            self.clean_fields()

    def calc_average(self):
        if self.boxStudent.get() and self.boxNote1.get() and self.boxNote2.get():
            try:
                note1 = float(self.boxNote1.get())
                note2 = float(self.boxNote2.get())
                average = (note1 + note2)/2
                self.lblAverage['text'] = average
                if average >= 7:
                    self.lblStatus['text'] = 'Approved'
                elif average >= 5:
                    self.lblStatus['text'] = 'Recovering'
                else:
                    self.lblStatus['text'] = 'Disapproved'
            except ValueError:
                mb.showinfo('Data type error', 'Please, enter only valid data')

    def get_fields(self):
        student = self.boxStudent.get()
        note1 = float(self.boxNote1.get())
        note2 = float(self.boxNote2.get())
        average = float(self.lblAverage['text'])
        status = self.lblStatus['text']
        return student, note1, note2, average, status

    def write_to_workbook(self):
        # overwriting workbook
        try:
            source = 'datasource.xlsx'
            data = []
            for line in self.appTree.get_children():
                content = []
                for value in self.appTree.item(line)['values']:
                    content.append(value)
                data.append(content)
            df = pd.DataFrame(data=data, columns=self.columnsHeader)
            spreadsheet = pd.ExcelWriter(source)
            df.to_excel(spreadsheet, 'data', index=False)
            spreadsheet.save()
        except ValueError:
            mb.showerror('Error', 'Data base error')

    def add_record(self):
        student, note1, note2, average, status = self.get_fields()
        if not average == '':
            try:
                self.appTree.insert('', 'end', iid=self.iid,
                                    values=(student, note1, note2, average, status))
                self.appTree.see(self.iid)
                self.iid = self.iid + 1
                self.write_to_workbook()
            except ValueError:
                mb.showerror('Error', 'Error when trying to save data')
            finally:
                self.clean_fields()

    def update_record(self):
        student, note1, note2, average, status = self.get_fields()
        temp_average = (note1 + note2)/2
        if temp_average != average:
            mb.showinfo('', 'Please, calculate average')
        else:
            if mb.askyesno('Alert', f"Update data from {student}"):
                if not average == '':
                    try:
                        selected = self.appTree.focus()
                        self.appTree.item(selected, values=(student, note1, note2, average, status))
                        self.write_to_workbook()
                    except ValueError:
                        mb.showerror('Error', 'Error when trying to update data')
                    finally:
                        self.clean_fields()

    def delete_record(self):
        student = self.boxStudent.get()
        if mb.askyesno('Alert', f'Delete all data from {student}'):
            try:
                selected = self.appTree.focus()
                self.appTree.delete(selected)
                self.iid = self.iid - 1
                self.write_to_workbook()
            except ValueError:
                mb.showerror('Error', 'Error when trying to delete')
            finally:
                self.clean_fields()


# Main Screen
root = Tk()
root.title('My first RAD Application Sample')
root.geometry("800x600+400+200")
root.resizable(False, False)
AppComponents(root)
root.mainloop()
