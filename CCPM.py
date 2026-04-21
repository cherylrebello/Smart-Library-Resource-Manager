from tkinter import *
from tkinter import messagebox

# ---------------- DATA (NO DATABASE) ----------------
books = [
    {"title": "Python Basics", "author": "John Smith", "topic": "Programming", "total": 5, "available": 5},
    {"title": "Data Structures", "author": "Amit", "topic": "DSA", "total": 6, "available": 6},
    {"title": "Algorithms", "author": "CLRS", "topic": "DSA", "total": 5, "available": 5},
    {"title": "Machine Learning", "author": "Tom", "topic": "AI", "total": 4, "available": 4},
    {"title": "Computer Networks", "author": "Tanenbaum", "topic": "Networking", "total": 3, "available": 3},
    {"title": "Operating Systems", "author": "Galvin", "topic": "OS", "total": 4, "available": 4},
    {"title": "DBMS", "author": "Korth", "topic": "Database", "total": 6, "available": 6},
    {"title": "Cyber Security", "author": "Stallings", "topic": "Security", "total": 5, "available": 5},
    {"title": "Cloud Computing", "author": "Buyya", "topic": "Cloud", "total": 5, "available": 5},
    {"title": "Java Programming", "author": "Herbert", "topic": "Programming", "total": 6, "available": 6}
]

# ---------------- APP ----------------
root = Tk()
root.title("Library Resource Manager")
root.geometry("900x550")
root.configure(bg="#1e1e2f")

# ---------------- FUNCTIONS ----------------
def show_books(filter_text=""):
    listbox.delete(0, END)

    found = False

    for book in books:
        if filter_text.lower() in book["topic"].lower():
            listbox.insert(
                END,
                f"{book['title']} | {book['author']} | {book['topic']} | Total:{book['total']} | Available:{book['available']}"
            )
            found = True

    if not found:
        listbox.insert(END, "No books found")

def book_selected():
    try:
        selected = listbox.get(listbox.curselection())

        if selected == "No books found":
            return

        title = selected.split("|")[0].strip()

        for book in books:
            if book["title"] == title:
                if book["available"] > 0:
                    book["available"] -= 1
                    messagebox.showinfo("Success", "Book Booked!")
                else:
                    messagebox.showerror("Error", "No copies left!")
                break

        show_books()

    except:
        messagebox.showerror("Error", "Please select a book!")

def search():
    show_books(search_e.get())

# ---------------- UI ----------------
Label(root, text="📚 Library Resource Manager",
      font=("Arial", 18, "bold"),
      bg="#1e1e2f", fg="white").pack(pady=10)

search_e = Entry(root, width=30)
search_e.pack()

Button(root, text="🔍 Search by Topic",
       command=search,
       bg="#2196F3", fg="white").pack(pady=5)

listbox = Listbox(root,
                  width=120,
                  height=18,
                  bg="#f0f0f0",
                  fg="black",
                  font=("Arial", 10))
listbox.pack(pady=10)

Button(root, text="📖 Show All",
       command=lambda: show_books(""),
       bg="#4CAF50", fg="white", width=20).pack(pady=5)

Button(root, text="✅ Book Selected",
       command=book_selected,
       bg="#FF9800", fg="white", width=20).pack(pady=5)

# Initial load
show_books("")

root.mainloop()