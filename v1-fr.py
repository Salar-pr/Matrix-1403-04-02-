import random#فراخانی کردن کتاب خانه رندوم 
row = 3
column = 3
a = 1
b = 9


#تعریف تابع برای ساخت جدول
def jadval(row,column,a,b):
    my_list=list(random.randint(a,b)for _ in range(row*column))

#جدا سازی ان به مقدار ستون
    for i in range(0, len(my_list),row):
        print(my_list[i:i+row],"\t"*2)
