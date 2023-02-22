# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

from gettext import find


scorer_1 = 'Ruud Gullit'
scorer_2 = 'Marco van Basten'

goal_0 = 32
goal_1 = 54

scorers = scorer_1 + " " +  str(goal_0)+ ", " + scorer_2 + " " + str(goal_1)

report = f"{scorer_1} scored in the {str(goal_0)}nd minute\n{scorer_2} scored in the {str(goal_1)}th minute"

print(scorers)
print(report)

player = 'Rinat Dasayev'

first_name = player[:(player.find(" "))]

print(first_name)

last_name_len = len(player[(player.find(" ")+1):])

print(last_name_len)

name_short = first_name[0] + "." + player[(player.find(" ")):]

print(name_short)

chant = ((first_name+ "! ")*len(first_name)).strip()

good_chant = chant[-1] != " "

print(good_chant)