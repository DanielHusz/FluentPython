# 序列和可迭代对象拆包

# 并行赋值
ab = (1, 2)
a, b = ab
print(a, b)
# 变量交换
a, b = b, a
print(a, b)

# 使用*获取余下的项
a, b, *rest = range(5)
print(a, b, rest)

# 并行赋值

a, *body, c, d = range(6)
print(a, body, c, d)


# 函数调用拆包可以多次调用*

def fun(a, b, c, d, *rest):
    return a, b, c, d, rest


print(fun(*[1, 2], 3, *range(7)))

# 嵌套拆包

metro_areas = [
    ('Tokyo', 'JP', 36.933, (25.1223, 139.23432)),
    ('Mexico City', 'MX', 20.142, (19.2433242, -99.234243))
]


def main():
    for name, _, _, (lat, lon) in metro_areas:
        if lon <= 0:
            print(f"{name} {lat} {lon}")


if __name__ == '__main__':
    main()
