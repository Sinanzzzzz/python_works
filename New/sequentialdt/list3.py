# 3. Given a list:
# l = [['arun', 23, 30000],
#     ['amal', 25, 50000],
#     ['anu', 27, 40000]]
# 1.Find the maximum salary
# 2.Find the minimum age

l = [['arun', 23, 30000],['amal', 25, 50000],['anu', 27, 40000]]

max_salary = max([i[2] for i in l])
print("Maximum salary:",max_salary)

min_age = min([i[1] for i in l])
print("Minimum age:",min_age)