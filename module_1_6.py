my_dict = {'Masha': 1997, 'Anton': 2000, 'Miakish': 2022, 'Lyumpsik': 2020}
print(my_dict)
print(my_dict['Anton'])
print(my_dict.get('Oleg'))
my_dict['Vasilii'] = 1986
my_dict['Sofia'] = 2005
a = my_dict.pop('Lyumpsik')
print(a)
print(my_dict)


my_set = {5, 48, 'Love', 1.3, 1, 1, 5, 'Love'}
print(my_set)
my_set.add('Star')
my_set.add(False)
my_set.remove(1.3)
print(my_set)

