import time


def merge_sort(data_list, draw_list_on_canvas, time_speed):
    merge_sort_algorithm(data_list, 0, len(data_list) - 1,
                         draw_list_on_canvas, time_speed)


def merge_sort_algorithm(data_list, left, right, draw_list_on_canvas, time_speed):
    if left < right:
        middle = (left + right) // 2
        merge_sort_algorithm(data_list, left, middle,
                             draw_list_on_canvas, time_speed)
        merge_sort_algorithm(data_list, middle + 1, right,
                             draw_list_on_canvas, time_speed)
        merge(data_list, left, middle, right, draw_list_on_canvas, time_speed)


def merge(data_list, left, middle, right, draw_list_on_canvas, time_speed):
    draw_list_on_canvas(data_list, color_array(
        len(data_list), left, middle, right))
    time.sleep(time_speed)
    left_list = data_list[left:middle+1]
    right_list = data_list[middle+1:right+1]
    left_index = right_index = 0
    data_list_index = left
    while left_index < len(left_list) and right_index < len(right_list):
        if left_list[left_index] <= right_list[right_index]:
            data_list[data_list_index] = left_list[left_index]
            left_index += 1
            data_list_index += 1
        else:
            data_list[data_list_index] = right_list[right_index]
            right_index += 1
            data_list_index += 1
    while left_index < len(left_list):
        data_list[data_list_index] = left_list[left_index]
        left_index += 1
        data_list_index += 1
    while right_index < len(right_list):
        data_list[data_list_index] = right_list[right_index]
        right_index += 1
        data_list_index += 1
    draw_list_on_canvas(data_list, [
                        'green' if x >= left and x <= right else "white" for x in range(len(data_list))])
    time.sleep(time_speed)


def color_array(length, left, middle, right):
    color_array_ = []
    for i in range(length):
        if i >= left and i <= right:
            if i >= left and i <= middle:
                color_array_.append("yellow")
            else:
                color_array_.append("orange")
        else:
            color_array_.append("white")

    return color_array_
