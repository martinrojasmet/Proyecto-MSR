import customtkinter

class DropdownList(customtkinter.CTkFrame):
    def __init__(self, master, titulo, destinos):
        super().__init__(master)
        self.grid_columnconfigure(0,weight=1)
        self.destinos = destinos
        self.title = titulo

        self.title = customtkinter.CTkLabel(self, text=self.title)
        self.title.grid(row=0, column=0, padx=10, sticky="w")

        self.combobox = customtkinter.CTkComboBox(self, values=destinos)
        self.combobox.set(destinos[0])
        self.combobox.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

class CanvasPrincipal(customtkinter.CTkCanvas):
    def __init__(self, master):
        super().__init__(master, bg="#414141", highlightthickness=0)
        self.width = 1900
        self.height = 870
        self.nodeList = []
        self.javier_movement = []
        self.andreina_movement = []

        self.startWidth = 100
        self.startHeight = 80

        self.counter = 0

        self.steps1 = 0
        self.steps2 = 0

        self.widthIncrement = 335
        self.heightIncrement = 140

        for i in range(6):
            for j in range(6):    
                if (i != 5):
                    arc1 = self.create_line(self.get_row_position(j), self.get_column_position(i), self.get_row_position(j), self.get_column_position(i+1), width=8)
                if (j != 5):
                    arc2 = self.create_line(self.get_row_position(j), self.get_column_position(i), self.get_row_position(j+1), self.get_column_position(i), width=8)
                node = self.create_aa_circle(self.get_row_position(j), self.get_column_position(i), 40)
                self.nodeList.append(node)
                self.create_text(self.get_row_position(j),  self.get_column_position(i), font=("Arial", 18), text=f"{self.counter}")
                self.counter = self.counter + 1

        self.javier = self.create_aa_circle(self.get_row_position(1), self.get_column_position(1), 30, fill="blue", tags="javier")
        self.andreina = self.create_aa_circle(self.get_row_position(2), self.get_column_position(2), 30, fill="pink")
    
    def get_row_position(self, index):
        return self.startWidth + (index * self.widthIncrement)
    
    def get_column_position(self, index):
        return self.startHeight + (index * self.heightIncrement)
    
    def movement1(self):
        if (len(self.javier_movement) > 1):
            direction, velocity = self.javier_movement[1][0] - self.javier_movement[0][0], self.javier_movement[1][1] - self.javier_movement[0][1]
            if (direction == 6):
                step_rate = 140 / velocity
                self.move(self.javier, 0, step_rate)
                if ((self.steps1 + 1) == velocity):
                    self.steps1 = 0
                    self.javier_movement.pop(0)
                    self.after(1000, self.movement1)
                else:
                    self.steps1 += 1
                    self.after(1000, self.movement1)

            elif (direction == -6):
                step_rate = 140 / velocity
                self.move(self.javier, 0, - step_rate)
                if ((self.steps1 + 1) == velocity):
                    self.steps1 = 0
                    self.javier_movement.pop(0)
                    self.after(1000, self.movement1)
                else:
                    self.steps1 += 1
                    self.after(1000, self.movement1)
            elif (direction == 1):
                step_rate = 335 / velocity
                self.move(self.javier, step_rate, 0)
                if ((self.steps1 + 1) == velocity):
                    self.steps1 = 0
                    self.javier_movement.pop(0)
                    self.after(1000, self.movement1)
                else:
                    self.steps1 += 1
                    self.after(1000, self.movement1)
            elif (direction == -1):
                step_rate = 335 / velocity
                self.move(self.javier, - step_rate, 0)
                if ((self.steps1 + 1) == velocity):
                    self.steps1 = 0
                    self.javier_movement.pop(0)
                    self.after(1000, self.movement1)
                else:
                    self.steps1 += 1
                    self.after(1000, self.movement1)
        else:
            self.after_cancel(self.movement1)

    def movement2(self):
        if (len(self.andreina_movement) > 1):
            direction, velocity = self.andreina_movement[1][0] - self.andreina_movement[0][0], self.andreina_movement[1][1] - self.andreina_movement[0][1]
            if (direction == 6):
                step_rate = 140 / velocity
                self.move(self.andreina, 0, step_rate)
                if ((self.steps2 + 1) == velocity):
                    self.steps2 = 0
                    self.andreina_movement.pop(0)
                    self.after(1000, self.movement2)
                else:
                    self.steps2 += 1
                    self.after(1000, self.movement2)

            elif (direction == -6):
                step_rate = 140 / velocity
                self.move(self.andreina, 0, - step_rate)
                if ((self.steps2 + 1) == velocity):
                    self.steps2 = 0
                    self.andreina_movement.pop(0)
                    self.after(1000, self.movement2)
                else:
                    self.steps2 += 1
                    self.after(1000, self.movement2)
            elif (direction == 1):
                step_rate = 335 / velocity
                self.move(self.andreina, step_rate, 0)
                if ((self.steps2 + 1) == velocity):
                    self.steps2 = 0
                    self.andreina_movement.pop(0)
                    self.after(1000, self.movement2)
                else:
                    self.steps2 += 1
                    self.after(1000, self.movement2)
            elif (direction == -1):
                step_rate = 335 / velocity
                self.move(self.andreina, - step_rate, 0)
                if ((self.steps2 + 1) == velocity):
                    self.steps2 = 0
                    self.andreina_movement.pop(0)
                    self.after(1000, self.movement2)
                else:
                    self.steps2 += 1
                    self.after(1000, self.movement2)
        else:
            self.after_cancel(self.movement2)
            

    def stop_javier(self):
        self.after_cancel(self.movement1)


class PantallaPrincipal(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Proyecto N°1 Javier y Andreina")
        self.geometry("1000x600")
        self.attributes('-fullscreen', True)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure((0,1), weight=1)


        self.exit_button = customtkinter.CTkButton(self, text="Salir", command=self.close_window)
        self.exit_button.grid(row=0, column=2, padx=10, pady=10, sticky="nse")

        self.new_destiny_button = customtkinter.CTkButton(self, text="Añadir destino", command=self.new_destiny_callback)
        self.new_destiny_button.grid(row=0, column=1, padx=10, pady=10, sticky="nse")


        self.canvas_frame = CanvasPrincipal(self)
        self.canvas_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew", columnspan=3)


        self.destinos_frame = DropdownList(self, "Seleccionar destino:", destinos=["Paraguay", "Boleita", "Parque del Este"])
        self.destinos_frame.grid(row=2, column=0, padx=10, pady=10, sticky="sew")


        self.restart_button = customtkinter.CTkButton(self, text="Reiniciar", font=("Arial", 24), command=self.reiniciar_callback)
        self.restart_button.grid(row=2, column=1, padx=10, pady=10, sticky="nse")

        self.start_button = customtkinter.CTkButton(self, text="Empezar", font=("Arial", 24), command=self.empezar_callback)
        self.start_button.grid(row=2, column=2, padx=10, pady=10, sticky="nse")

    def empezar_callback(self):
        # estos son unos caaminos dummy, falta conectar con dijkstra
        camino_javier = [(7,0),(13,7),(19,10),(25,16)]
        camino_andreina = [(14,0),(20,7),(21,16),(27,23),(33,32)]
        self.canvas_frame.andreina_movement = camino_andreina
        self.canvas_frame.javier_movement = camino_javier
        self.canvas_frame.movement2()
        self.canvas_frame.movement1()
        
    
    def reiniciar_callback(self):
        print("TODO")

    def new_destiny_callback(self):
        print("TODO")

    def close_window(self):
        self.destroy()

        

app = PantallaPrincipal()
app.mainloop()