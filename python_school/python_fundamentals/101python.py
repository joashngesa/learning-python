team="""
    raya
    saliba
    bukayo
"""
name='rasik'
age=34
print("my name is {} and i am {} old ".format(name,age))
target=100000
installments=12
id='son'
print(f'My aim is to save ${target:,.2f} in my time in Canada, saving ${target/installments:,.2f} every year')

#if statements

number=34

if number < 0:
    print(f"{number} is negative")
elif number == 0:
    print(f"{number} is equaL zero")
else :
    print(f"{number} is positive")

maganji=100
kukatinga="ndakas" if maganji >= 100 else "piga shuksha"
print(kukatinga)

#list in python
mbogi = [2,16,28,14,29,[12,10,7],"baraka","wenger"]
print(mbogi)
mbogi.append("arteta")
print(mbogi)
mbogi.extend([8])
print(mbogi)
mbogi.remove("baraka")

print(len(mbogi),mbogi)

#set in python_unique,no_order

members = {2,4,5,7,8,10,28,4,5,6,7,8,34,45,45,45656,7}
members.add(29)
members.remove(45656)
print(members)

#combining sets
membersb = {3,4,5,6,7,8,9,34,435,56,67,78}
print(members | membersb)
#intersection;common elements
members & membersb
#difference(a but not b)
members - membersb
#symmetric difference(in either but not both)
members ^ membersb

#for loops through sets and lists
legends=["wenger","diaby","ozil","ramsey","cazorla"]
for legend in legends:
    print(legend)

#loop through dictionaries 
ma_ovete={"best":"wenger",
          "favourite":"ramsey",
          "all_time":"henry",
          "promising":"bukayo"}
for ovetes in ma_ovete:
    print(ovetes)
    
for keys in ma_ovete:
    print(keys)

for values in ma_ovete:
        print(values)

for key in ma_ovete:
     print(f"key:{"key"} values:{ma_ovete[key]}")

ma_ovete.update({"like":"norgard","best_player":"rice"})
print(ma_ovete)

for ovete in ma_ovete.keys():
     print(ovete)
for ovetee in ma_ovete.values():
     print(ovetee)
for xyz, values in ma_ovete.items():
     print(xyz, values)
for values in ma_ovete:
     print(ma_ovete[values])

#for loops for nested dictionary
teams={
     "arsenal":
       {"manager":"arteta",
        "captain":"odegard",
        "favourite":"saliba"},
        "crystal_palace":
        {"manager":"viera",
         "captain":"crux",
         "favourite":"sanders"}}

for club,data in teams.items():
     print("club",club)
     
     for key,values in data.items():
        print(" ",key,":",values)

#freestyle
sales = {
    "Jan": {"revenue": 12000, "orders": 300},
    "Feb": {"revenue": 15000, "orders": 350},
    "Mar": {"revenue": 11000, "orders": 280}
}
#calculate the total revenue
total_revenue = 0
for month, metrics in sales.items():
     total_revenue += metrics["revenue"]

print(total_revenue)
     
#find sum
purchases=(23,33,45,56,55,66,64,44,455,55)
totals=0

for buy in purchases:
     totals += buy
print(totals)
#waiting for something
user_input=()
while user_input!="quit":
     user_input=input("type quit to exit.")
#processing untill empty
tasks=[1,2,3,4,5]
while tasks:
     task=tasks.pop()
     print(task)
else :
    print("finish off")



























