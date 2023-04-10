import json

wit = open('sample-date.json')
a = json.load(wit)

# jsondata = open('sample-date.json', 'r')
# a = json.loads(jsondata)

print('Interface Status')
print('=' * 80)

names = ['DN', 'Description', 'Speed', 'MTU']
form = "{:>47}  {:<15}  {:<10}  {:<6}"
print(form.format(*names))
print('-' * 47 + '  ' + '-' * 15 + '  ' + '-' * 10 + '  ' + '-' * 6)

for i in a['imdata']:
    print(form.format(i['l1PhysIf']['attributes']['dn'], i['l1PhysIf']['attributes']['descr'], i['l1PhysIf']['attributes']['speed'], i['l1PhysIf']['attributes']['mtu']))