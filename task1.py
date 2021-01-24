from sys import argv

produckt_per_hour, rate_per_hour, award = argv[1:]
var_wage = (int(produckt_per_hour) * int(rate_per_hour)) + int(award)
print(var_wage)
