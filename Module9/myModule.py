# 計算幾次方
def pow(x, y):
    return x**y


# 簡單斷句

def segment_sentence(text):
    list_sentences = text.split(' ')
    return list_sentences




# 測試模組

if __name__ == "__main__":

    result = pow(3,5)
    print(result)

    txt = "I will always love you"
    text_result = segment_sentence(txt)

    print(text_result)


