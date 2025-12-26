dict1=dict()
dict1["name"]=['Alan']
dict1["family"]=['Abdolghaderi']
dict1["phone"]=['09149822453']
dict1["name"].append('jamal')
dict1["family"].append('Azizbeigi')
dict1["phone"].append('9149822453')
for i in range(len(dict1['name'])):
    print("Name is:  ", dict1['name'][i],
          "Family is: ", dict1['family'][i],
          "Phone is:  ", dict1['phone'][i])

