from tkinter import *
from tkinter import messagebox
import mysql.connector as m
from random import *

email = ""
count = -1
score = 0
question = []

def uiLogin():
    def login():
        global email
        cn = m.connect(host="localhost", user="root", password="alok@2003", database="QuizEngine")
        cursor = cn.cursor()
        if s.get() == "Admin":
            query = "select * from admin where email='{}' and password='{}'".format(t1.get(), t2.get())
            cursor.execute(query)
            record = cursor.fetchone()
            if record is None:
                messagebox.showinfo("Sorry", "Invalid id or password")
            else:
                uiAdminHome()
        else:
            query = "select * from students where email='{}' and password='{}'".format(t1.get(), t2.get())
            cursor.execute(query)
            record = cursor.fetchone()
            if record is None:
                messagebox.showinfo("Sorry", "Invalid id or password")
            else:
                email = t1.get()
                uiStudentHome()

        cn.close()

    def toggle_password():
        if t2.cget('show') == '':
            t2.config(show='*')
            toggle_btn.config(text='Show')
        else:
            t2.config(show='')
            toggle_btn.config(text='Hide')

    frame = Tk()
    frame.geometry("400x400")
    frame.title("Quiz Engine")

    ti1 = Label(frame, text="Email", font=("Arial", 10, "bold"))
    t1 = Entry(frame, width=20, bg="skyblue")
    
    ti2 = Label(frame, text="Password", font=("Arial", 10, "bold"))
    t2 = Entry(frame, width=20, bg="skyblue", show="*")
    toggle_btn = Button(frame, text="Show", width=6, command=toggle_password)
    
    ti3 = Label(frame, text="Role", font=("Arial", 10, "bold"))
    options = ["Student", "Admin"]
    s = StringVar()
    d = OptionMenu(frame, s, *options)
    
    butn1 = Button(frame, text="Login", width=10, bg="blue", command=login)

    ti1.place(x=70, y=20)
    t1.place(x=20, y=40)
    ti2.place(x=70, y=60)
    t2.place(x=20, y=80)
    toggle_btn.place(x=220, y=80)
    ti3.place(x=70, y=100)
    d.place(x=20, y=120)
    butn1.place(x=50, y=170)
    
    frame.mainloop()

    
def uiViewScore():
    frame = Toplevel()
    frame.geometry("400x400")
    frame.title("View Scores")

    score_list = Listbox(frame, width=50, height=20)
    score_list.pack(pady=20)

    try:
        cn = m.connect(host="localhost", user="root", password="alok@2003", database="QuizEngine")
        cursor = cn.cursor()
        query = "SELECT email, score FROM students_scores"
        cursor.execute(query)
        records = cursor.fetchall()
        
        if not records:
            messagebox.showinfo("Info", "No scores found.")
        
        for record in records:
            score_list.insert(END, f"Email: {record[0]} - Score: {record[1]}")

    except m.Error as e:
        messagebox.showerror("Database Error", str(e))

    finally:
        if 'cn' in locals():
            cn.close()

    close_button = Button(frame, text="Close", command=frame.destroy)
    close_button.pack(pady=10)

    frame.mainloop()



def uiAdminHome():
    frame = Tk()
    frame.geometry("400x400")
    b1 = Button(frame, text="Add Student", width=20, bg="skyblue", font=("Arial", 9, "italic"), command=uiAddStudent)
    b2 = Button(frame, text="Add Question", width=20, bg="skyblue", font=("Arial", 9, "italic"), command=uiAddQuestion)
    b3 = Button(frame, text="View Score", width=20, bg="skyblue", font=("Arial", 9, "italic"), command=uiViewScore)
    b1.place(x=20, y=20)
    b2.place(x=20, y=70)
    b3.place(x=20, y=120)
    frame.mainloop()

def uiAddStudent():
    def saveStudent():
        cn = m.connect(host="localhost", user="root", password="alok@2003", database="QuizEngine")
        cursor = cn.cursor()
        query = "insert into students values('{}', '{}', '{}')".format(t3.get(), t4.get(), t5.get())
        cursor.execute(query)
        cn.commit()
        cn.close()
        messagebox.showinfo("Success", "Data Saved")

    frame = Tk()
    frame.geometry("400x400")
    frame.title("Add Student")
    ti3 = Label(frame, text="Email", font=("Arial", 10, "bold"))
    t3 = Entry(frame, width=20, bg="skyblue")
    ti4 = Label(frame, text="Password", font=("Arial", 10, "bold"))
    t4 = Entry(frame, width=20, bg="skyblue")
    ti5 = Label(frame, text="Name", font=("Arial", 10, "bold"))
    t5 = Entry(frame, width=20, bg="skyblue")
    butn2 = Button(frame, text="Save", width=10, bg="blue", command=saveStudent)
    ti3.place(x=70, y=20)
    t3.place(x=20, y=40)
    ti4.place(x=70, y=60)
    t4.place(x=20, y=80)
    ti5.place(x=70, y=100)
    t5.place(x=20, y=120)
    butn2.place(x=50, y=155)
    frame.mainloop()

def uiAddQuestion():
    def saveQuestion():
        cn = m.connect(host="localhost", user="root", password="alok@2003", database="QuizEngine")
        cursor = cn.cursor()
        query = "insert into questions(question, op1, op2, op3, op4, ca) values('{}', '{}', '{}', '{}', '{}', '{}')".format(t6.get(), t7.get(), t8.get(), t9.get(), t10.get(), t11.get())
        cursor.execute(query)
        cn.commit()
        cn.close()
        messagebox.showinfo("Success", "Data Saved")

    frame = Tk()
    frame.geometry("400x400")
    frame.title("Add Questions")
    ti6 = Label(frame, text="Write Your Question", font=("Arial", 10, "bold"))
    t6 = Entry(frame, width=40, bg="skyblue")
    ti7 = Label(frame, text="Write Options", font=("Arial", 10, "bold"))
    t7 = Entry(frame, width=30, bg="skyblue")
    t8 = Entry(frame, width=30, bg="skyblue")
    t9 = Entry(frame, width=30, bg="skyblue")
    t10 = Entry(frame, width=30, bg="skyblue")
    t11 = Entry(frame, width=30, bg="skyblue")
    butn3 = Button(frame, text="Save", width=10, bg="blue", command=saveQuestion)
    ti6.place(x=10, y=20)
    t6.place(x=10, y=40)
    ti7.place(x=10, y=60)
    t7.place(x=10, y=80)
    t8.place(x=10, y=105)
    t9.place(x=10, y=125)
    t10.place(x=10, y=145)
    t11.place(x=10, y=170)
    butn3.place(x=50, y=195)
    frame.mainloop()

def uiStudentHome():
    global question
    cn = m.connect(host="localhost", user="root", password="alok@2003", database="QuizEngine")
    cursor = cn.cursor()
    query = "select * from questions"
    cursor.execute(query)
    questions = cursor.fetchall()
    cn.close()
    
    s = StringVar()

    def nextQuestion():
        global question
        global score
        global count
        if count != -1:
            ua = s.get()
            ca = question[6]
            if ua == ca:
                score += 1

        if count == len(questions) - 1:
            messagebox.showinfo("Result", "Your result is " + str(score))
        else:
            count += 1
            if count < len(questions):
                question = questions[count]
                l13.config(text=question[1])
                rd1.config(text=question[2], value=question[2])
                rd2.config(text=question[3], value=question[3])
                rd3.config(text=question[4], value=question[4])
                rd4.config(text=question[5], value=question[5])

    frame = Toplevel()
    frame.geometry("400x400")
    frame.title("Questions")
    l13 = Label(frame, text="", width=25, bg="skyblue")
    rd1 = Radiobutton(frame, text="Option A", variable=s, value="A")
    rd2 = Radiobutton(frame, text="Option B", variable=s, value="B")
    rd3 = Radiobutton(frame, text="Option C", variable=s, value="C")
    rd4 = Radiobutton(frame, text="Option D", variable=s, value="D")
    butn6 = Button(frame, text="Next", width=10, bg="crimson", command=nextQuestion)
    
    l13.place(x=20, y=10)
    rd1.place(x=20, y=40)
    rd2.place(x=20, y=60)
    rd3.place(x=20, y=80)
    rd4.place(x=20, y=100)
    butn6.place(x=50, y=150)
    
    nextQuestion()
    frame.mainloop()

# Call the login UI to start the application
uiLogin()
