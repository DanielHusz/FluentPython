"""
内置序列：
1、容器序列：list、tuple、collections.deque
2、扁平序列：str、bytes、array.array


可变序列-Sequence
list、bytearray、array.array、collections.deque
不可变序列-MutableSequence
tuple、str、bytes


"""

from collections import abc

print(issubclass(tuple, abc.Sequence))
print(issubclass(list, abc.MutableSequence))
