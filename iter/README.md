# 可迭代对象、迭代器、生成器

- 容器 container
- 可迭代对象 iterable
- 迭代器 iterator
- 生成器 generator



## 容器
> 容器中的元素可以逐个地迭代获取，可以用in, not in关键字判断元素是否包含在容器中。

> str/ list/ tupe/ dict/ set都是容器对象

```
以字符串为示例
>>> s = '12345'
>>> '12' in s
>>> '126' in s
>>> for x in s:print(x)
```


## 可迭代对象
> 凡是可以返回一个迭代器的对象都可称之为可迭代对象.

> str/ list/ tuple/

```
>>> s = '123'
>>> s_iter = iter(s)
>>> s_iter
<str_iterator at 0x7f830c826f60>
>>> next(s_iter)
1
>>> next(s_iter)
2
>>> next(s_iter)
3
>>> next(s_iter)
---------------------------------------------------------------------------
StopIteration                             Traceback (most recent call last)
<ipython-input-45-9c75d6e5ae59> in <module>()
----> 1 next(s_iter)

StopIteration:
```