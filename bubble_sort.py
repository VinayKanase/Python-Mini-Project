import time


def bubble_sort(data_list, draw_list_on_canvas, time_speed):
    for i in range(len(data_list) - 1):
        for j in range(len(data_list) - 1):
            if data_list[j] > data_list[j+1]:
                # Swapping
                temp = data_list[j]
                data_list[j] = data_list[j+1]
                data_list[j+1] = temp
                draw_list_on_canvas(
                    data_list, ['yellow' if x == j or x == j+1 else "#A90042" for x in range(len(data_list))])
                time.sleep(time_speed)
    draw_list_on_canvas(data_list, ['yellow' for x in range(len(data_list))])
