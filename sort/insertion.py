def insertion_sort(data_list):
    cnt = len(data_list)
    for i in range(1, cnt-1):
        j = i-1
        nxt_element = data_list[i]
        while(( data_list[j] > nxt_element) and (j >= 0)):
                data_list[j+1] = data_list[j]
                j -= 1
        data_list[j+1] = nxt_element
        print
    return data_list

if __name__ == '__main__':
    data_list = [19,2,31,45,30,11,121,27]
    insertion_sort(data_list)
    print(data_list)