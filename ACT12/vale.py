from tkinter import*
from tkinter import messagebox

class Validacion:
    
    def __init__ (self, correoE, contraE, corr, contra):
        self.correoE = correoE 
        self.contraE = contraE
        self.corr = corr
        self.contra = contra
    
    def validar(self):
        
        if (self.correoE == self.corr and self.contraE == self.contra):
            messagebox.showinfo("Correcto","Se ha iniciado sesion correctamente")
        elif self.corr == "" or self.contra == "":
            messagebox.showerror("Error","Uno o más campos están vacios")
        else:
            messagebox.showerror("Error","Usuario o contraseña incorrectos")