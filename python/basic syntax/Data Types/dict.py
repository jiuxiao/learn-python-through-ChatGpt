# A dictionary in Python is an unordered collection of key-value pairs.
# Each key-value pair in a dictionary is separated by a colon(:),
# and the key and value are separated by a comma(,).
# Dictionaries are mutable, meaning that you can add, remove, and modify key-value pairs.
# In Python, dictionaries are defined using curly braces {}.

# len() - Returns the number of key-value pairs in a dictionary.

my_dict = {"key1": "value1", "key2": "value2", "key3": "value3"}
print(len(my_dict))  # Output: 3

# keys() - Returns a list of all the keys in a dictionary.
my_dict = {"key1": "value1", "key2": "value2", "key3": "value3"}
print(my_dict.keys())  # Output: dict_keys(['key1', 'key2', 'key3'])

# values() - Returns a list of all the values in a dictionary.
my_dict = {"key1": "value1", "key2": "value2", "key3": "value3"}
print(my_dict.values())  # Output: dict_values(['value1', 'value2', 'value3'])

# items() - Returns a list of tuples, where each tuple contains a key-value pair in the dictionary.
my_dict = {"key1": "value1", "key2": "value2", "key3": "value3"}
print(my_dict.items())  # Output: dict_items([('key1', 'value1'), ('key2', 'value2'), ('key3', 'value3')])

# get(key[, default]) - Returns the value associated with a given key.
# If the key is not found in the dictionary, it returns the default value (if provided), or None.

my_dict = {"key1": "value1", "key2": "value2", "key3": "value3"}
print(my_dict.get("key2"))  # Output: value2
print(my_dict.get("key4", "default_value"))  # Output: default_value

# pop(key[, default]) - Removes the key-value pair associated with the given key from the dictionary, and returns the
# value. If the key is not found in the dictionary, it returns the default value (if provided), or raises a KeyError.

my_dict = {"key1": "value1", "key2": "value2", "key3": "value3"}
print(my_dict.pop("key2"))  # Output: value2
print(my_dict.pop("key4", "default_value"))  # Output: default_value

# update(other_dict) - Adds the key-value pairs from another dictionary other_dict to the current dictionary.

my_dict = {"key1": "value1", "key2": "value2", "key3": "value3"}
other_dict = {"key4": "value4", "key5": "value5"}
my_dict.update(other_dict)
print(my_dict)  # Output: {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4', 'key5': 'value5'}









