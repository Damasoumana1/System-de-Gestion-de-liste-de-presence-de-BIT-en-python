import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import json

class AttendanceSystem:
    def __init__(self):
        try:
            with open('attendance_data.json', 'r') as file:
                self.attendance_list = json.load(file)
        except FileNotFoundError:
            self.attendance_list = {}

    def add_student(self, student_id, name, classe):
        self.attendance_list[student_id] = {'name': name, 'classe': classe, 'attendance': []}
        self.save_data()

    def mark_attendance(self, student_id, is_present, cours):
        if student_id in self.attendance_list:
            if is_present:
                self.attendance_list[student_id]['attendance'].append({'cours': cours, 'status': 'Present'})
            else:
                self.attendance_list[student_id]['attendance'].append({'cours': cours, 'status': 'Absent'})
            self.save_data()
        else:
            messagebox.showerror("Erreur", "Étudiant non trouvé.")

    def view_attendance_list(self):
        attendance_list = "\n".join([f"ID: {student_id}, Nom: {details['name']}, Classe: {details['classe']}, Présences: {details['attendance']}" for student_id, details in self.attendance_list.items()])
        messagebox.showinfo("Liste des présences", attendance_list)

    def search_student(self, name):
        for student_id, details in self.attendance_list.items():
            if details['name'] == name:
                messagebox.showinfo("Résultat de la recherche", f"ID: {student_id}, Nom: {details['name']}, Classe: {details['classe']}, Présences: {details['attendance']}")
                return
        messagebox.showinfo("Résultat de la recherche", "Étudiant non trouvé.")

    def save_data(self):
        with open('attendance_data.json', 'w') as file:
            json.dump(self.attendance_list, file, indent=4)

class AttendanceSystemGUI:
    def __init__(self, attendance_system):
        self.attendance_system = attendance_system
        self.root = tk.Tk()
        self.root.title("Systeme de gestion de liste de Présences de Bit")
        self.root.geometry("800x600")
        self.root.resizable(False, False)
        self.root.configure(bg="#F5F5F5")
        
        # Charger l'image en arrière-plan avec PIL
        # image = Image.open("téléchar bit.jpeg")
        # self.background_image = ImageTk.PhotoImage(image)
        # self.new_size = (800, 600)

        # Créer un Label avec l'image en arrière-plan
        # self.background_label = tk.Label(self.root,image=self.background_image)
        # self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Conserver une référence à l'image pour éviter qu'elle ne soit supprimée par le ramasse-miettes
        # self.background_label.image = self.background_image

        self.create_widgets()
        self.root.mainloop()

    def create_widgets(self):
        # Widgets pour ajouter un étudiant
        self.student_id_label = tk.Label(self.root, text="ID de l'étudiant:")
        self.student_id_label.configure(fg="#333333")
        self.student_id_entry = tk.Entry(self.root, width=30)
        self.student_id_entry.configure(bg="#FFFFFF", fg="#000000")

        self.name_label = tk.Label(self.root, text="Nom de l'étudiant:")
        self.name_label.configure(fg="#333333")
        self.name_entry = tk.Entry(self.root, width=30)
        self.name_entry.configure(bg="#FFFFFF", fg="#000000")

        self.classe_label = tk.Label(self.root, text="Classe de l'étudiant:")
        self.classe_label.configure(fg="#333333")
        self.classe_entry = tk.Entry(self.root, width=30)
        self.classe_entry.configure(bg="#FFFFFF", fg="#000000")

        self.add_student_button = tk.Button(self.root, text="Ajouter un étudiant", command=self.add_student)
        self.add_student_button.configure(bg="#ADD8E6", fg="#000000")
        
        #Bouton en survole
        self.add_student_button.bind("<Enter>", lambda e: self.add_student_button.configure(bg="#0000CD"))
        self.add_student_button.bind("<Leave>", lambda e: self.add_student_button.configure(bg="#ADD8E6"))


        # Widgets pour marquer la présence
        self.mark_attendance_label = tk.Label(self.root, text="ID de l'étudiant:")
        self.mark_attendance_label.configure(fg="#333333")
        self.mark_attendance_entry = tk.Entry(self.root, width=30)
        self.mark_attendance_entry.configure(bg="#FFFFFF", fg="#000000")

        self.cours_label = tk.Label(self.root, text="Nom du cours:")
        self.cours_label.configure(fg="#333333")
        self.cours_entry = tk.Entry(self.root, width=30)
        self.cours_entry.configure(bg="#FFFFFF", fg="#000000")

        self.mark_attendance_button = tk.Button(self.root, text="Marquer la présence", command=self.mark_attendance)
        self.mark_attendance_button.configure(bg="#ADD8E6", fg="#000000")
        
        
         
        #Bouton en survole
        self.mark_attendance_button.bind("<Enter>", lambda e: self.mark_attendance_button.configure(bg="#0000CD"))
        self.mark_attendance_button.bind("<Leave>", lambda e: self.mark_attendance_button.configure(bg="#ADD8E6"))


        # Widgets pour voir la liste des présences
        self.view_attendance_list_button = tk.Button(self.root, text="Voir la liste des présences", command=self.view_attendance_list)
        self.view_attendance_list_button.configure(bg="#ADD8E6", fg="#000000")
        
         #Bouton de survole
        self.view_attendance_list_button.bind("<Enter>", lambda e: self.view_attendance_list_button.configure(bg="#0000CD"))
        self.view_attendance_list_button.bind("<Leave>", lambda e: self.view_attendance_list_button.configure(bg="#ADD8E6"))


        # Widgets pour rechercher un étudiant
        self.search_student_label = tk.Label(self.root, text="Nom de l'étudiant:")
        self.search_student_label.configure(fg="#333333")
        self.search_student_entry = tk.Entry(self.root, width=30)
        self.search_student_entry.configure(bg="#FFFFFF", fg="#000000")

        self.search_student_button = tk.Button(self.root, text="Rechercher un étudiant", command=self.search_student)
        self.search_student_button.configure(bg="#ADD8E6", fg="#000000")
        
        
        #Bouton de survole
        self.search_student_button.bind("<Enter>", lambda e: self.search_student_button.configure(bg="#0000CD"))
        self.search_student_button.bind("<Leave>", lambda e: self.search_student_button.configure(bg="#ADD8E6"))


        # Placement des widgets
        self.student_id_label.grid(row=0, column=0, padx=10, pady=10)
        self.student_id_entry.grid(row=0, column=1, padx=10, pady=10)
        self.name_label.grid(row=1, column=0, padx=10, pady=10)
        self.name_entry.grid(row=1, column=1, padx=10, pady=10)
        self.classe_label.grid(row=2, column=0, padx=10, pady=10)
        self.classe_entry.grid(row=2, column=1, padx=10, pady=10)
        self.add_student_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        self.mark_attendance_label.grid(row=4, column=0, padx=10, pady=10)
        self.mark_attendance_entry.grid(row=4, column=1, padx=10, pady=10)
        self.cours_label.grid(row=5, column=0, padx=10, pady=10)
        self.cours_entry.grid(row=5, column=1, padx=10, pady=10)
        self.mark_attendance_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

        self.view_attendance_list_button.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

        self.search_student_label.grid(row=8, column=0, padx=10, pady=10)
        self.search_student_entry.grid(row=8, column=1, padx=10, pady=10)
        self.search_student_button.grid(row=9, column=0, columnspan=2, padx=10, pady=10)
        
        
        
        # Ajout du bouton "Exit"
        self.exit_button = tk.Button(self.root, text="Exit", command=self.root.destroy)
        self.exit_button.configure(bg="#ADD8E6", fg="#000000")
        #Bouton de survole
        self.exit_button.bind("<Enter>", lambda e: self.exit_button.configure(bg="#0000CD"))
        self.exit_button.bind("<Leave>", lambda e: self.exit_button.configure(bg="#ADD8E6"))

        #Espacement
        self.exit_button.grid(row=12, column=0, columnspan=2)


        # Lancement de la boucle principale
        self.root.mainloop()

    def add_student(self):
        student_id = self.student_id_entry.get()
        name = self.name_entry.get()
        classe = self.classe_entry.get()
        self.attendance_system.add_student(student_id, name, classe)
        messagebox.showinfo("Succès", "Étudiant ajouté avec succès.")

    def mark_attendance(self):
        student_id = self.mark_attendance_entry.get()
        is_present = messagebox.askyesno("Présence", "L'étudiant est-il présent ?")
        cours = self.cours_entry.get()
        self.attendance_system.mark_attendance(student_id, is_present, cours)
        messagebox.showinfo("Succès", "Présence marquée avec succès.")

    def view_attendance_list(self):
        self.attendance_system.view_attendance_list()

    def search_student(self):
        name = self.search_student_entry.get()
        self.attendance_system.search_student(name)

if __name__ == "__main__":
    attendance_system = AttendanceSystem()
    gui = AttendanceSystemGUI(attendance_system)
