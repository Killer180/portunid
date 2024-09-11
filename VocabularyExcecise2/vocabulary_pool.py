import tkinter as tk
from datetime import datetime
from operator import index
from tkinter import simpledialog, messagebox, filedialog, font
from tkinter.font import Font
import csv
import random



# 初始空的词汇库
vocabulary = {}

# 记录用户选择“不认识”的单词以及学过的单词
unknown_words = []
learned_words = []

# 用户选择的测试数量
test_quantity = 0

current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# 函数：从CSV文件加载词汇库
def load_vocabulary_from_csv(file_path):
    try:
        with open(file_path, mode='r', encoding='utf-8', errors='ignore') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                vocabulary[row['english']] = {
                    'chinese' : row['chinese'],
                    'practice_times' : row['practice_times'],
                    'last_time' : row['last_time']
                }
    except FileNotFoundError:
        messagebox.showerror("错误", "找不到文件，请检查文件路径。")
    except Exception as e:
        messagebox.showerror("错误", f"读取文件时发生错误：{e}")

# 函数：更新词汇池中本次测试过的单词的信息- practice_time +1, 更新该次测试时间在last_time列
def update_vocabulary_to_csv(file_path):
    update_filename = 'learning.csv'
    for word in learned_words:
        if word in vocabulary:
            vocabulary[word]['practice_times'] += 1
            vocabulary[word]['last_time'] = current_time

    with open(update_filename, mode='w', newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile)
        writer.writerows(words)

print(vocabulary)
print(current_time)