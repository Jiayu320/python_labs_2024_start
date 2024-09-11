# 创建一个包含水果的列表
fruits = ["苹果", "香蕉", "樱桃"]
print(fruits)

# 访问列表中的第一个元素
first_fruit = fruits[0]
print(first_fruit)

# 修改列表中的第二个元素
fruits[1] = "橙子"
print(fruits)

# 添加一个新元素到列表末尾
fruits.append("葡萄")
print(fruits)

# 删除列表中的一个元素
fruits.remove("樱桃")
print(fruits)

# 获取列表的长度
length = len(fruits)
print(length)

# 利用循环实现输出所有列表（可以利用注释实现自动输出代码）
for fruit in fruits:
    print(fruit)

