N = int(input())


for i in range(1, N+1):
    str_num = str(i)
    three_six_nine = ''
    for st in str_num:
        if st in ['3', '6', '9']:
            three_six_nine += '-'
    if three_six_nine != '':
        print(three_six_nine, end=' ')
    else:
        print(i, end=' ')
