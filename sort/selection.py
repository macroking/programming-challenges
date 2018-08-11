def selection_sort(data_list):
    cnt = len(data_list)
    for x in range(0, cnt):
        min_idx = x
        for y in range(x+1, cnt):
            if data_list[y] < data_list[min_idx]:
                min_idx = y
        data_list[x], data_list[min_idx] = data_list[min_idx], data_list[x]
        print  data_list


if __name__ == '__main__':
    data_list = [3,44,38,5,47,15,36,26,27,2,46,4,1,19,50,48]
    selection_sort(data_list)
    print(data_list)