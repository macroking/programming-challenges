def bubblesort(data_list):
    data_list_len = len(data_list)
    for i in range(data_list_len-1, 0, -1):
        for j in range(i):
            if data_list[j] < data_list[j+1]:
                data_list[j], data_list[j+1] = data_list[j+1], data_list[j]
    return data_list

if __name__ =='__main__':
    data_list = [100,124,3904,13493,123] #[19,2,31,45,6,11,121,27]
    data_list = bubblesort(data_list)
    print(data_list)