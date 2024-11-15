# 終極密碼 讓使用者能夠重複猜數字，直到猜對為止
# 告訴使用者需要輸入的數字範圍 input()
# 超出範圍要顯示「超出範圍請重新輸入」
# 數字太大 要提示「請輸入更小的數字」
# 數字太小 要提示「請輸入更大的數字」
# 使用者猜對要回傳「恭喜中獎」

secret_num = 50
num = -1

while num != secret_num:
    num = (int)(input("請輸入1~100: "))
    
    if num < 0 or num > 100:
        print("超出範圍請重新輸入")

    elif num > secret_num:
        print("數字太大 請輸入更小的數字")
    
    elif num < secret_num:
        print("數字太小 請輸入更大的數字")
    
    else:
        print("恭喜中獎")











