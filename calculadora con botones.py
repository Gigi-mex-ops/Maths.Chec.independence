
import tkinter as tk


def click(boton) :
   actual = entrada.get()
   entrada.delete(0, tk END)
   entrada.insert(0, actual + str(boton))   
   
   
   
   
def borrar():
   entrada.delete(0, tk.END)
   

def calcular():
   try:
      resultado = eval (entrada.get) 
      entrada.delete(0, tk END)
      entrada.insert(0, str(resultado))
      
   except:
      entrada.delete(0, tk.END)
      entrada.insert(0, "Error")   
      
      
      
ventana = tk.Tk()
ventana.title("calcuadora para ti")


entrada = tk.Entry(Ventana, width=30, font=("Arial",18), borderwidth=5, relief="ridge")          
        
    