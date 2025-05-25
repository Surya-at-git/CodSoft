import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os

# File where contacts will be stored
FILE_NAME = "contacts.json"

# Ensure the file exists
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w") as file:
        json.dump([], file)

def load_contacts():
    with open(FILE_NAME, "r") as file:
        return json.load(file)

def save_contacts(contacts):
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)

def add_contact():
    name = entry_name.get()
    phone = entry_phone.get()
    email = entry_email.get()
    address = entry_address.get()

    if not name or not phone:
        messagebox.showwarning("Required Fields", "Name and phone are required.")
        return

    contacts = load_contacts()
    contacts.append({"name": name, "phone": phone, "email": email, "address": address})
    save_contacts(contacts)
    messagebox.showinfo("Success", "Contact added successfully!")
    clear_entries()
    view_contacts()

def view_contacts():
    contacts = load_contacts()
    listbox.delete(0, tk.END)
    for contact in contacts:
        listbox.insert(tk.END, f"{contact['name']} - {contact['phone']}")

def clear_entries():
    entry_name.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_address.delete(0, tk.END)

def search_contact():
    query = simpledialog.askstring("Search", "Enter name or phone number to search:")
    if not query:
        return
    contacts = load_contacts()
    listbox.delete(0, tk.END)
    found = False
    for contact in contacts:
        if query.lower() in contact['name'].lower() or query in contact['phone']:
            listbox.insert(tk.END, f"{contact['name']} - {contact['phone']}")
            found = True
    if not found:
        messagebox.showinfo("Not Found", "No contact matches your search.")

def get_selected_contact():
    try:
        index = listbox.curselection()[0]
        selected_text = listbox.get(index)
        name = selected_text.split(" - ")[0]
        contacts = load_contacts()
        for i, contact in enumerate(contacts):
            if contact['name'] == name:
                return i, contact
    except:
        return None, None
    return None, None

def delete_contact():
    index, contact = get_selected_contact()
    if contact:
        confirm = messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete '{contact['name']}'?")
        if confirm:
            contacts = load_contacts()
            contacts.pop(index)
            save_contacts(contacts)
            messagebox.showinfo("Deleted", "Contact deleted.")
            view_contacts()
    else:
        messagebox.showwarning("Select Contact", "Please select a contact to delete.")

def update_contact():
    index, contact = get_selected_contact()
    if contact:
        new_name = simpledialog.askstring("Update", "Enter new name:", initialvalue=contact['name'])
        new_phone = simpledialog.askstring("Update", "Enter new phone:", initialvalue=contact['phone'])
        new_email = simpledialog.askstring("Update", "Enter new email:", initialvalue=contact['email'])
        new_address = simpledialog.askstring("Update", "Enter new address:", initialvalue=contact['address'])

        if not new_name or not new_phone:
            messagebox.showwarning("Required Fields", "Name and phone cannot be empty.")
            return

        updated_contact = {
            "name": new_name,
            "phone": new_phone,
            "email": new_email,
            "address": new_address
        }

        contacts = load_contacts()
        contacts[index] = updated_contact
        save_contacts(contacts)
        messagebox.showinfo("Updated", "Contact updated successfully!")
        view_contacts()
    else:
        messagebox.showwarning("Select Contact", "Please select a contact to update.")

# GUI setup
root = tk.Tk()
root.title("📒 Contact Book")
root.geometry("600x500")
root.config(bg="#e8f0fe")

# Heading
title = tk.Label(root, text="Contact Book App", font=("Arial", 18, "bold"), bg="#e8f0fe", fg="#333")
title.pack(pady=10)

# Entry form
form_frame = tk.Frame(root, bg="#e8f0fe")
form_frame.pack(pady=5)

tk.Label(form_frame, text="Name:", bg="#e8f0fe").grid(row=0, column=0, sticky="e")
tk.Label(form_frame, text="Phone:", bg="#e8f0fe").grid(row=1, column=0, sticky="e")
tk.Label(form_frame, text="Email:", bg="#e8f0fe").grid(row=2, column=0, sticky="e")
tk.Label(form_frame, text="Address:", bg="#e8f0fe").grid(row=3, column=0, sticky="e")

entry_name = tk.Entry(form_frame, width=30)
entry_phone = tk.Entry(form_frame, width=30)
entry_email = tk.Entry(form_frame, width=30)
entry_address = tk.Entry(form_frame, width=30)

entry_name.grid(row=0, column=1, pady=2)
entry_phone.grid(row=1, column=1, pady=2)
entry_email.grid(row=2, column=1, pady=2)
entry_address.grid(row=3, column=1, pady=2)

tk.Button(root, text="Add Contact", command=add_contact, bg="#4CAF50", fg="white", width=20).pack(pady=5)

listbox = tk.Listbox(root, width=50, height=10)
listbox.pack(pady=10)

btn_frame = tk.Frame(root, bg="#e8f0fe")
btn_frame.pack()

tk.Button(btn_frame, text="View All", command=view_contacts, width=12).grid(row=0, column=0, padx=5, pady=5)
tk.Button(btn_frame, text="Search", command=search_contact, width=12).grid(row=0, column=1, padx=5, pady=5)
tk.Button(btn_frame, text="Update", command=update_contact, width=12).grid(row=0, column=2, padx=5, pady=5)
tk.Button(btn_frame, text="Delete", command=delete_contact, width=12).grid(row=0, column=3, padx=5, pady=5)

view_contacts()

root.mainloop()
