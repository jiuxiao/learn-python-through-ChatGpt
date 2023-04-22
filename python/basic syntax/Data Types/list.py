# list 存储一系列的值，可以不同的类型
#新建

my_list = [1, 2, 3, 4, 5]

my_list = ["apple", "banana", "cherry"]
#建立空的list，添加元素
my_list = []
my_list.append(1)
my_list.append(2)
my_list.append(3)


# append(x): Adds an element to the end of the list.
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits)  # ['apple', 'banana', 'cherry', 'orange']

#extend(iterable): Adds all the elements of an iterable (list, tuple, string etc.) to the end of the list.
fruits = ["apple", "banana", "cherry"]
more_fruits = ["orange", "mango", "grape"]
fruits.extend(more_fruits)
print(fruits)  # ['apple', 'banana', 'cherry', 'orange', 'mango', 'grape']

#insert(i, x): Inserts an element at a specific position in the list.
fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "orange")
print(fruits)  # ['apple', 'orange', 'banana', 'cherry']

#remove(x): Removes the first occurrence of the specified element from the list.
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")
print(fruits)  # ['apple', 'cherry']

#pop([i]): Removes and returns the element at the specified position. If no index is specified, removes and returns the last element.
fruits = ["apple", "banana", "cherry"]
banana = fruits.pop(1)
print(fruits)  # ['apple', 'cherry']
print(banana)  # 'banana'

#clear(): Removes all the elements from the list.
fruits = ["apple", "banana", "cherry"]
fruits.clear()
print(fruits)  # []

#index(x[, start[, end]]): Returns the index of the first occurrence of the specified element in the list. If the element is not found, raises a ValueError.
fruits = ["apple", "banana", "cherry"]
banana_index = fruits.index("banana")
print(banana_index)  # 1

#count(x): Returns the number of times the specified element appears in the list.
fruits = ["apple", "banana", "cherry", "banana"]
banana_count = fruits.count("banana")
print(banana_count)  # 2

#sort(key=None, reverse=False): Sorts the elements of the list in ascending order. If reverse is True, sorts the elements in descending order.
fruits = ["banana", "cherry", "apple"]
fruits.sort()
print(fruits)  # ['apple', 'banana', 'cherry']

fruits = ["banana", "cherry", "apple"]
fruits.sort(reverse=True)
print(fruits)  # ['cherry', 'banana', 'apple']

#reverse(): Reverses the order of the elements in the list.
fruits = ["apple", "banana", "cherry"]
fruits.reverse()
print(fruits)  # ['cherry', 'banana', 'apple']











