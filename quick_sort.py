import time


def partition(data_list, head, tail, draw_list_on_canvas, time_speed):
    border = head
    pivot = data_list[tail]

    draw_list_on_canvas(data_list, get_colors_list(
        len(data_list), head, tail, border, border))
    time.sleep(time_speed)

    for j in range(head, tail):
        if data_list[j] < pivot:
            draw_list_on_canvas(data_list, get_colors_list(
                len(data_list), head, tail, border, j, True))
            time.sleep(time_speed)
            data_list[border], data_list[j] = data_list[j], data_list[border]
            border += 1

        draw_list_on_canvas(data_list, get_colors_list(
            len(data_list), head, tail, border, j))
        time.sleep(time_speed)

    draw_list_on_canvas(data_list, get_colors_list(
        len(data_list), head, tail, border, tail, True))
    time.sleep(time_speed)
    data_list[border], data_list[tail] = data_list[tail], data_list[border]
    return border


def quick_sort(data_list, head, tail, draw_list_on_canvas, time_speed):
    if head < tail:
        partition_index = partition(
            data_list, head, tail, draw_list_on_canvas, time_speed)
        # Left partition
        quick_sort(data_list, head, partition_index-1,
                   draw_list_on_canvas, time_speed)
        # Right partition
        quick_sort(data_list, partition_index+1, tail,
                   draw_list_on_canvas, time_speed)


def get_colors_list(data_list_length, head, tail, border, current_index, is_swapping=False):
    color_array = []

    for i in range(data_list_length):
        # Color when nothing is perform
        if i >= head and i <= tail:
            color_array.append("gray")
        else:
            color_array.append("white")

        if i == tail:
            color_array[i] = "orange"
        elif i == border:
            color_array[i] = "red"
        elif i == current_index:
            color_array[i] = "yellow"

        if is_swapping:
            if i == border or i == current_index:
                color_array[i] = "green"
    return color_array
