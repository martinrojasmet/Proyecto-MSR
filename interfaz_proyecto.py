import customtkinter

from logic import logic

log = logic()

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
    
    def get_selected_destiny(self):
        return self.combobox.get()
    
    def add_new_value(self, value):
        new_values = self.combobox.cget("values")
        new_values.append(value)
        self.combobox.configure(values=new_values)
    
class NewDestinyFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.grid_rowconfigure(1, weight=1)

        self.nombre_label = customtkinter.CTkLabel(self, text="Nombre: ")
        self.nombre_label.grid(row=0, column=0, padx=10)

        self.nombre_input = customtkinter.CTkEntry(self, font=("Arial", 12), height=8)
        self.nombre_input.grid(row=0, column=1, padx=10, columnspan=3)

        self.carrera_label = customtkinter.CTkLabel(self, text="Carrera: ")
        self.carrera_label.grid(row=1, column=0, padx=10)
        self.carrera_minus = customtkinter.CTkButton(self, text="-", font=("Arial", 14), command=self.substract_carrera, width=20, height=5)
        self.carrera_minus.grid(row=1, column=1, padx=10)
        self.carrera = customtkinter.CTkLabel(self, text="15")
        self.carrera.grid(row=1, column=2, padx=10)
        self.carrera_plus = customtkinter.CTkButton(self, text="+", font=("Arial", 14), command=self.add_carrera, width=20, height=5)
        self.carrera_plus.grid(row=1, column=3, padx=10)

        self.calle_label = customtkinter.CTkLabel(self, text="Calle: ")
        self.calle_label.grid(row=2, column=0, padx=10)
        self.calle_minus = customtkinter.CTkButton(self, text="-", font=("Arial", 14), command=self.substract_calle, width=20, height=5)
        self.calle_minus.grid(row=2, column=1, padx=10)
        self.calle = customtkinter.CTkLabel(self, text="55")
        self.calle.grid(row=2, column=2, padx=10)
        self.calle_plus = customtkinter.CTkButton(self, text="+", font=("Arial", 14), command=self.add_calle, width=20, height=5)
        self.calle_plus.grid(row=2, column=3, padx=10)

    def add_carrera(self):
        current = int(self.carrera.cget("text"))
        if (current < 15):
            current += 1
            self.carrera.configure(text=f"{current}")

    def substract_carrera(self):
        current = int(self.carrera.cget("text"))
        if (current > 10):
            current -= 1
            self.carrera.configure(text=f"{current}")

    def add_calle(self):
        current = int(self.calle.cget("text"))
        if (current < 55):
            current += 1
            self.calle.configure(text=f"{current}")

    def substract_calle(self):
        current = int(self.calle.cget("text"))
        if (current > 50):
            current -= 1
            self.calle.configure(text=f"{current}")

    def reset_frame(self):
        self.carrera.configure(text="15")
        self.calle.configure(text="55")
        self.nombre_input.delete(0, 'end')

class CanvasPrincipal(customtkinter.CTkCanvas):
    def __init__(self, master):
        super().__init__(master, bg="#414141", highlightthickness=0)
        self.width = 1900
        self.height = 870
        self.nodeList = []
        self.javier_movement = []
        self.andreina_movement = []

        self.startWidth = 110
        self.startHeight = 50

        self.counter = 0

        self.stopped = True
        self.done = False

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
                node = self.create_aa_circle(self.get_row_position(j), self.get_column_position(i), 40, tags=f"{self.counter}")
                self.nodeList.append(node)
                self.create_text(self.get_row_position(j),  self.get_column_position(i), font=("Arial", 18), text=f"{self.counter}")
                self.counter = self.counter + 1

        self.javier = self.create_aa_circle(self.get_row_position(1), self.get_column_position(1), 30, fill="blue", tags="javier")
        self.andreina = self.create_aa_circle(self.get_row_position(2), self.get_column_position(3), 30, fill="pink", tags="andreina")
    
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
                    self.after(500, self.movement1)
                else:
                    self.steps1 += 1
                    self.after(500, self.movement1)

            elif (direction == -6):
                step_rate = 140 / velocity
                self.move(self.javier, 0, - step_rate)
                if ((self.steps1 + 1) == velocity):
                    self.steps1 = 0
                    self.javier_movement.pop(0)
                    self.after(500, self.movement1)
                else:
                    self.steps1 += 1
                    self.after(500, self.movement1)
            elif (direction == 1):
                step_rate = 335 / velocity
                self.move(self.javier, step_rate, 0)
                if ((self.steps1 + 1) == velocity):
                    self.steps1 = 0
                    self.javier_movement.pop(0)
                    self.after(500, self.movement1)
                else:
                    self.steps1 += 1
                    self.after(500, self.movement1)
            elif (direction == -1):
                step_rate = 335 / velocity
                self.move(self.javier, - step_rate, 0)
                if ((self.steps1 + 1) == velocity):
                    self.steps1 = 0
                    self.javier_movement.pop(0)
                    self.after(500, self.movement1)
                else:
                    self.steps1 += 1
                    self.after(500, self.movement1)
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
                    self.after(500, self.movement2)
                else:
                    self.steps2 += 1
                    self.after(500, self.movement2)

            elif (direction == -6):
                step_rate = 140 / velocity
                self.move(self.andreina, 0, - step_rate)
                if ((self.steps2 + 1) == velocity):
                    self.steps2 = 0
                    self.andreina_movement.pop(0)
                    self.after(500, self.movement2)
                else:
                    self.steps2 += 1
                    self.after(500, self.movement2)
            elif (direction == 1):
                step_rate = 335 / velocity
                self.move(self.andreina, step_rate, 0)
                if ((self.steps2 + 1) == velocity):
                    self.steps2 = 0
                    self.andreina_movement.pop(0)
                    self.after(500, self.movement2)
                else:
                    self.steps2 += 1
                    self.after(500, self.movement2)
            elif (direction == -1):
                step_rate = 335 / velocity
                self.move(self.andreina, - step_rate, 0)
                if ((self.steps2 + 1) == velocity):
                    self.steps2 = 0
                    self.andreina_movement.pop(0)
                    self.after(500, self.movement2)
                else:
                    self.steps2 += 1
                    self.after(500, self.movement2)
        else:
            self.stopped = True
            self.done = True
            self.itemconfigure(self.nodeList[self.andreina_movement[0][0]], fill="white")
            self.after_cancel(self.movement2)
    
    def reset_ui(self):
        if (self.stopped):
            self.delete("javier")
            self.delete("andreina")
            self.javier = self.create_aa_circle(self.get_row_position(1), self.get_column_position(1), 30, fill="blue", tags="javier")
            self.andreina = self.create_aa_circle(self.get_row_position(2), self.get_column_position(3), 30, fill="pink", tags="andreina")

class ShowPaths(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.javier_path_label = customtkinter.CTkLabel(self, text="Camino Javier: ")
        self.javier_path_label.grid(row=0, column=0, padx=10, pady=5)

        self.javier_path = customtkinter.CTkLabel(self, text="[]")
        self.javier_path.grid(row=0, column=1, padx=10, pady=5)

        self.andreina_path_label = customtkinter.CTkLabel(self, text="Camino Andreina: ")
        self.andreina_path_label.grid(row=1, column=0, padx=10, pady=5)

        self.andreina_path = customtkinter.CTkLabel(self, text="[]")
        self.andreina_path.grid(row=1, column=1, padx=10, pady=5)

class PantallaPrincipal(customtkinter.CTk):

    diccionario = {
        "Discoteca The Darkness": 10,
        "Bar La Pasión": 31,
        "Cervecería Mi Rolita": 33,
        "Café Sensación": 35
    }

    def __init__(self):
        super().__init__()

        self.title("Proyecto N°1 Javier y Andreina")
        self.geometry("1000x600")
        self.attributes('-fullscreen', True)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure((0,1), weight=1)

        self.show_paths_frame = ShowPaths(self)
        self.show_paths_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsw")

        self.new_destiny_input = NewDestinyFrame(self)
        self.new_destiny_input.grid(row=0, column=1, padx=10, pady=10, sticky="nse")

        self.new_destiny_button = customtkinter.CTkButton(self, text="Añadir destino", font=("Arial", 24), command=self.new_destiny_callback)
        self.new_destiny_button.grid(row=0, column=2, padx=10, pady=10, sticky="nse", rowspan=2)

        self.exit_button = customtkinter.CTkButton(self, text="Salir", font=("Arial", 24), command=self.close_window)
        self.exit_button.grid(row=0, column=3, padx=10, pady=10, sticky="nse", rowspan=2)

        self.canvas_frame = CanvasPrincipal(self)
        self.canvas_frame.grid(row=2, column=0, padx=10, pady=10, sticky="nsew", columnspan=4)

        destinies_list = []
        for item in log.places_to_visit:
            destinies_list.append(item["name"])

        self.destinos_frame = DropdownList(self, "Seleccionar destino:", destinos=destinies_list)
        self.destinos_frame.grid(row=3, column=0, padx=10, pady=10, sticky="sew")


        self.restart_button = customtkinter.CTkButton(self, text="Reiniciar", font=("Arial", 24), command=self.reiniciar_callback)
        self.restart_button.grid(row=3, column=2, padx=10, pady=10, sticky="nse")

        self.start_button = customtkinter.CTkButton(self, text="Empezar", font=("Arial", 24), command=self.empezar_callback)
        self.start_button.grid(row=3, column=3, padx=10, pady=10, sticky="nse")

    def empezar_callback(self):

        if (self.canvas_frame.stopped and not self.canvas_frame.done):

            self.canvas_frame.stopped = False
            
            destino = self.destinos_frame.get_selected_destiny()
            nodo = self.diccionario[destino]
            nodo_ui = self.canvas_frame.nodeList[nodo]
            self.canvas_frame.itemconfigure(nodo_ui, fill="yellow")

            log.get_shortest_path(nodo)

            self.show_paths_frame.javier_path.configure(text=log.result_path_javier)
            self.show_paths_frame.andreina_path.configure(text=log.result_path_andreina)

            self.canvas_frame.andreina_movement = log.result_path_andreina
            self.canvas_frame.javier_movement = log.result_path_javier

            if (log.result_path_javier[0][1] != 0):
                javier_delay = log.result_path_javier[0][1] * 500
                self.after(javier_delay, self.canvas_frame.movement1)
                self.canvas_frame.movement2()
            elif (log.result_path_andreina[0][1] != 0):
                andreina_delay = log.result_path_andreina[0][1] * 500
                self.canvas_frame.movement1()
                self.after(andreina_delay, self.canvas_frame.movement2)
            else:
                self.canvas_frame.movement2()
                self.canvas_frame.movement1()
    
    def reiniciar_callback(self):
        if (self.canvas_frame.done):
            log.reset_values()
            self.show_paths_frame.javier_path.configure(text="[]")
            self.show_paths_frame.andreina_path.configure(text="[]")
            self.canvas_frame.done = False
            self.canvas_frame.reset_ui()

    def new_destiny_callback(self):
        if (self.canvas_frame.stopped):
            nombre = self.new_destiny_input.nombre_input.get()
            carrera = int(self.new_destiny_input.carrera.cget("text"))
            calle = int(self.new_destiny_input.calle.cget("text"))

            if (nombre != ""):
                destino = log.add_place_to_visit(name=nombre, carrera=carrera, calle=calle)
                destino_ya_existe = False
                for item in self.diccionario:
                    if (self.diccionario[item] == destino["node"]):
                        destino_ya_existe = True
                    else:
                        pass
                if (not destino_ya_existe):
                    log.places_to_visit.append(destino)
                    self.diccionario[nombre] = destino["node"]
                    self.destinos_frame.add_new_value(nombre)
                    self.new_destiny_input.reset_frame()


    def close_window(self):
        self.destroy()

        

app = PantallaPrincipal()
app.mainloop()