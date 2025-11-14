# working with sets
from pyscript import display

monarchs = {'Jade', 'Leiane', 'Ashley','Julia'}
math = {'Jade', 'Lia', 'Manuel', 'Martina'}

all_students = monarchs | math
display(all_students, target='output')
both_clubs = monarchs & math
display(both_clubs, target='output')
only_monarchs = monarchs - math
display(only_monarchs, target='output')
only_math = math - monarchs
display(only_math, target='output')
exactly_one = monarchs ^ math
display(exactly_one, target='output')