from tkinter import *
import random
from tkinter import ttk
from bubble_sort import *
from merge_sort import merge_sort
from quick_sort import quick_sort
data_list = []
root = Tk()
root.title("Sorting Algorithm Visualizer")
icon_image = PhotoImage(file="./images/LOGO.png")
root.iconphoto(False, icon_image)
root.geometry("900x600+200+80")
root.config(bg="#082a46")

selected_algorithm = StringVar()


def start_onCick():
    global data_list
    if not data_list:
        return
    if selected_algorithm.get() == "Quick Sort":
        quick_sort(data_list, 0, len(data_list) - 1,
                   draw_list_on_canvas, speed_input.get())
    elif selected_algorithm.get() == "Bubble Sort":
        bubble_sort(data_list, draw_list_on_canvas,
                    float(speed_input.get()))
    elif selected_algorithm.get() == "Merge Sort":
        merge_sort(data_list, draw_list_on_canvas, speed_input.get())
    draw_list_on_canvas(data_list, ['green' for x in range(len(data_list))])


def draw_list_on_canvas(data_list, colors_list):
    """Draws data_list on canvas perfectly without data overflow in canvas"""
    visualizer_canvas.delete("all")
    canvas_height = 450
    canvas_width = 870
    offset = 10
    space_between_rect = 10
    x_width = canvas_width / len(data_list)
    # 400 is multiplyer for to normalize the values so data won't flow out of canvas
    normalized_data = [i / max(data_list) for i in data_list]
    for i, height in enumerate(normalized_data):
        x0 = i*x_width + offset + space_between_rect
        y0 = canvas_height - height * 400

        x1 = (i+1) * x_width
        y1 = canvas_height

        visualizer_canvas.create_rectangle(
            x0, y0, x1, y1, fill=colors_list[i])
        visualizer_canvas.create_text(
            x0 + 2, y0, anchor=SW, text=str(data_list[i]), font=("new roman", 15, "italic bold"), fill="white")
    root.update_idletasks()


def generate_onClick():
    """Generates random array depending upon given constrains"""
    global data_list
    print("Selected Algo: " + selected_algorithm.get())

    min_input_value = int(min_input.get())
    max_input_value = int(max_input.get())
    size_input_value = int(size_input.get())

    # if minimum value is greater than maximum values will be swaped
    if min_input_value > max_input_value:
        min_input_value, max_input_value = max_input_value, min_input_value
    data_list = []
    for j in range(size_input_value):
        data_list.append(random.randrange(min_input_value, max_input_value+1))
    # Draw Data list on canvas
    draw_list_on_canvas(data_list, ['#A90042' for x in range(len(data_list))])


# Algorithm select input Label
algo_input_label = Label(root, text="Algorithm:", bg="#05897A",
                         width=10, fg="black", relief=GROOVE, bd=5)
algo_input_label.place(x=0, y=0)

# Algorithm select input
algo_input = ttk.Combobox(root, width=15, textvariable=selected_algorithm, values=[
                          'Bubble Sort', 'Quick Sort', 'Merge Sort'])
algo_input.place(x=145, y=00)

# Default choice is bubble sort
algo_input.current(0)

# Generate Random numbers button
generate_btn = Button(root, text="Generate", bg="#2DAE9A", relief=SUNKEN, activebackground="#059458",
                      activeforeground="white", bd=5, width=10, command=generate_onClick)
generate_btn.place(x=750, y=60)

# Size input Label
size_input_label = Label(root, text="Size: ", bg="#0E6DA5",
                         width=10, fg="black", height=2, relief=GROOVE, bd=5)
size_input_label.place(x=0, y=60)
# Size input
size_input = Scale(root, from_=5, to=30, resolution=1,
                   orient=HORIZONTAL, width=10, relief=GROOVE, bd=2)
size_input.place(x=120, y=60)

# Minimum input Label
min_input_label = Label(root, text="Min Value: ", bg="#0E6DA5",
                        width=10, fg="black", height=2, relief=GROOVE, bd=5)
min_input_label.place(x=250, y=60)
# Minimum input
min_input = Scale(root, from_=1, to=10, resolution=1,
                  orient=HORIZONTAL, width=10, relief=GROOVE, bd=2)
min_input.place(x=370, y=60)

# Maximum input Label
max_input_label = Label(root, text="Max Value: ", bg="#0E6DA5",
                        width=10, fg="black", height=2, relief=GROOVE, bd=5)
max_input_label.place(x=500, y=60)
# Maximum input
max_input = Scale(root, from_=1, to=100, resolution=1,
                  orient=HORIZONTAL, width=10, relief=GROOVE, bd=2)
max_input.place(x=620, y=60)


# Start button
start_btn = Button(root, text="Start", bg="#C45B09", relief=SUNKEN, activebackground="#059458",
                   activeforeground="white", bd=5, width=10, command=start_onCick)
start_btn.place(x=750, y=0)


# Speed input Label
speed_input_label = Label(root, text="Speed Value: ", bg="#0E6DA5",
                          width=12, fg="black", relief=GROOVE, bd=5)
speed_input_label.place(x=400, y=0)

# Speed input
speed_input = Scale(root, from_=0.2, to=5.0, resolution=0.1,
                    orient=HORIZONTAL, length=200, digits=2, width=10, relief=GROOVE, bd=2)
speed_input.place(x=520, y=0)

visualizer_canvas = Canvas(root, height=450, width=870, bg="black", bd=2)
visualizer_canvas.place(x=10, y=120)
root.mainloop()
