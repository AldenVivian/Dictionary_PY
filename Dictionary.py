mydict = {'key1':'val1','key2':'val2'}
print(mydict)
print(mydict['key1'])

pricedict = {'apple':20,'orange':40}
print(pricedict['apple'])

d = {'k1':123,'k2':[0,1,2],'k3':{'insidekey':99}}#Can hold any datatype including another dictionary or list itself

print(d['k2'])
print(d['k2'][1])

print(d['k3'])
print(d['k3']['insidekey'])

sampledict = {'key':['a','b','c']}
sampledict = sampledict['key'][1].upper()
print(sampledict)

newd = {'k1':100,'k2':200}
newd['k3'] = 300# Add a key to the dictionary
print(newd)

print(newd.keys())
print(newd.values())
print(newd.items())
