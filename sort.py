#創一個函示用來交換arr裡的兩個數字
def swap(arr, a, b):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp
    return arr
#快速排序函式
def Quicksort(arr, start, end):
    #終止條件: 當arr長度小於0
    if end <= start:
        return
    #設定一個基準點
    pivot = arr[start]
    #設定左右邊的箭頭
    left = start
    right = end
    #在左右兩邊的箭頭碰到之前
    while left != right:
        #如果右邊箭頭指的數字大於基準點就繼續往左邊找，直到找到一個比基準點還要小的數字才停
        while arr[right] >= pivot and left != right:
            right -= 1
        #如果左邊箭頭指的數字小於基準點就繼續往左邊找，直到找到一個比基準點還要大的數字才停
        while arr[left] <= pivot and left != right:
            left += 1
        #如果兩個箭頭指的點不是同一個點就把兩個數字互換
        if left != right:
            #印出是哪兩個數字互換，還有現在處理到哪一層遞迴
            print('----------swap %s and %s from portion %s----------' %(arr[start], arr[right], arr[start: end+1]))
            #互換數字
            arr = swap(arr, left, right)
            #印換完數字後的結果
            print(arr)
    #如果兩個箭頭指的數字和基準點不一樣的時候就把兩個數字互換
    if start != right:
        #印出是哪兩個數字互換，還有現在處理到哪一層遞迴
        print('----------swap %s and %s from portion %s----------' %(arr[start], arr[right], arr[start: end+1]))
        #互換數字
        arr = swap(arr, start, right)
        #印換完數字後的結果
        print(arr)
    
    #下一層遞迴
    Quicksort(arr, start, left-1)
    Quicksort(arr, left+1, end)

    
#開始跑程式
arr = [33, 67, 8, 13, 54, 119, 3, 84, 25, 41]

Quicksort(arr, 0, len(arr)-1)

print(arr)
        
            