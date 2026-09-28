# Filter the color whose length is greater than 5
# Filter the color containing letter 'n'

colors=['red','green','blue','yellow','orange']

print(list(filter(lambda x:len(x)>5,colors)))
print(list(filter(lambda x:'n' in x,colors)))