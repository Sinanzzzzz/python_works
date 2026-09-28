# 2. Given a list l = [1,1,2,3,3,4]
# Remove duplicates without using set()
# (Order should be preserved)

l = [1,1,2,3,3,4]
new = []            # New empty list create aakum,then athil oro values add aakum
for i in l:         # repeat vanno ennu check aakum ,repeat illel add aakum
    if i not in new:
        new.append(i)
print(new)
        