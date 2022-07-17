dictionary = {
                'a':1, 
                'b':2, 
                'c':3, 
                'd':2,
                'e':3, 
                'f':2,
            }
print("initial_dictionary", str(dictionary))

rev_dict = {}
  
for key, value in dictionary.items():
    rev_dict.setdefault(value, set()).add(key)
      
result = [key for key, values in rev_dict.items() if len(values) > 1]
print("duplicate values", str(result))