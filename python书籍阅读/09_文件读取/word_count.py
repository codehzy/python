def count_words(filename):
    """计算一个文件大致包含多少个单词"""
    try:
        with open(filename) as f_object:
            contents = f_object.read()
    except FileNotFoundError:
        msg = 'Sorry, the file ' + filename + 'does not exist.'
        print(msg)
    else:
        # 计算文件大致包含多少个单词
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words.")


filename = 'book.txt'
count_words(filename)

# 使用pass可以失败时一声不吭