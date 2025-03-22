# import 自己建立的模組
import myModule


if __name__ == "__main__":
# 計算幾次方
    result = myModule.pow(3,5)
    print(result)

    # 簡單斷句
    txt = "I will always love you"
    text_result = myModule.segment_sentence(txt)

    print(text_result)




