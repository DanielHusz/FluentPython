symbols = '$%&*#@'
codes = []
for item in symbols:
    codes.append(ord(item))

print(codes)

codes_listcomps = [ord(i) for i in symbols]
print(codes_listcomps)

x = 'ABC'
# 列表推导式，for 子句中赋值的变量在局部作用域内
codes = [ord(x) for x in x]
print(codes)
print(x)
# 海象运算符：:= 运算符赋值的变量，其作用域限定在函数内，
#           除非目标变量使用 global 或 nonlocal 声明
codes = [last := ord(c) for c in x]
print(last)

# 列表推导式与map和filter比较
beyond_ascii = [ord(i) for i in symbols if ord(i) < 127]
print(beyond_ascii)
beyond_ascii = list(filter(lambda x: x < 127, map(ord, symbols)))
print(beyond_ascii)

# 笛卡尔乘积
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
shirts = [(color, size) for color in colors for size in sizes]
print(shirts)

# 生成器表达式
shirts = ((color, size) for color in colors for size in sizes)
for i in shirts:
    # %和f的区别
    print(f"{i[0]} {i[1]}")
    print("%s %s" % i)  # 元组拆包
