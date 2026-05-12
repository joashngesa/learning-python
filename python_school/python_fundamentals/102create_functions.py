#we roll out
name = "Rasik"
age = 25
country = "Canada"
dream_job = "Data Engineer"
yearly_savings_goals = 12000
favorite_number = 28

print("==== IDENTITY CARD ====")
print("Name:", name)
print("Age:", age)
print("Country:", country)
print("Dream Job:", dream_job)
print("yearly_savings_goals:", yearly_savings_goals)
print("favorite_number:",favorite_number)

#Savings tracker
target_amount = 7000
current_savings = 200
monthly_savings = 800

remaining = target_amount - current_savings
plan = remaining / 8

print("savings target amount:",target_amount)
print("current savings:", current_savings)
print("remaining amount:",remaining)
print("monthly saving plan:",plan)

#String builder game

name = "rasik"
skill = "python"
goal = "data engineer"

print(f"The child of God leaving here is called {name}. I see him practicing {skill}"\
      f" on a daily. I pray that he makes his dream of becoming a {goal}")
print(f"jina ni {name}"\
      f" i want to be a guru in {skill}"\
      ". in Jesus name, i will make my contribution top the society by being th best "\
      f"{goal} i can be")
print(f"{name} is an aspiring {goal}, the guy really likes {skill}")

#Fuction powered greeting machine
topic = ("python 101")
def greetings(feeling,trait):
    print(f"welcome to python,knowing you, you will {feeling} it")
    print(f"today we shall cover {topic} lesson")
    print(f"keep going, you need to be {trait}.")

greetings("love","disciplined")

purpose = "seek"
def daily_goal(start,day_mantra,finish):
    print(f"the first thing i do in the morning is to {start}.")
    print(f"The rest of the day i will always endeavour to {day_mantra}.")
    print(f"Every day ends in {finish}, respect papa")
    
daily_goal("give thanks","be my best","thanksgiving")

def goodbye(feeling):
    print(f"i donth think i am a fun of goodbyes, i {feeling} goodbyes")

goodbye("hate")

#Minishop receipt

item1 = "exercise book"
price1 = 50
tax1 = 0.05 * price1
item2 = "pencil"
price2 = 10
tax2 = 0.05 * price2
item3 = "tution fee"
price3 = 30000
tax3 = 0.05 * price3
total = price1 + tax1 + price2 + tax2 + price3 + tax3
def receipt():

    print(" ====receipt ====")
    print(item1,":",price1 + tax1)
    print(item2,":",price2 + tax2)
    print(item3,":",price3 + tax3)
    print("total:",total)

receipt()

#Daily report generator

def daily_report(name,topic,hours_spent):
    print(f"Name: {name}")
    print(f"Topic: {topic}")
    print(f"Hours_spent: {hours_spent}")

daily_report("rasik","functions",8)
daily_report("rasik","linux_navigation",12)

#Fortune message game

name = "og_zorin"
fortune = "python excellent"

def motivation():
    print(name + " if you maintain this consistency, you will become " + fortune )

motivation()

#drill exercises
#drill one
identity = "son of God"
purpose = "servant of God"
id_number = 1
humility = 100
state_analysis = 5.5

print("identity:",identity) 
print("purpose:",purpose)
print("id_number:",id_number)
print("humility:",humility)
print("state_analysis:",state_analysis)

#drill two
cost = 7090
product_price = 42000
discount = 3000
future_discount = 0.07

def breakdown():
    print("sales:",product_price - discount)
    print("profit:",(product_price - discount) - cost)
    print("future_discount amount:",(product_price - discount) * future_discount)
   
breakdown()

#drill three
goal = "linux,python,sql fluency:"
means = "consistent practices, sticking to blue print and careful listening to master chief"

print(goal + means )

#drill four
first_name = "joash"
orgin = "kenya"
aspiration = "data engineer"
specialization = "supply chain"

def intro():
    print("My name is " + first_name)
    print("I come from " + orgin)
    print("i am an aspiring " + aspiration)
    print("specialization is in " + specialization)

intro()

#drill five

target1 = "master sql, create schemas,databases,data warehouses"
target2 = "master python foundations and develop capacity to use it effeciently"
target3 = "learn, unserstand,maximize linux"

def mission():
    print(target1)
    print(target2)
    print(target3)

mission()

#drill six

def fact_to_remember():
    print("practice makes permanent")

fact_to_remember()

#personal_profile

profile_name = "rasik"
working_name = "og_zorin"
learning_strategy = "be thorough, consistent, patient, stick to the vision"
mantra = "today i will do what they wont, tomorow i will do what they cant"
financial_goal = "save, record, analyze, learn and understand money"

def personal_profile():
    print("profile_name:",profile_name)
    print("working_name:",working_name)
    print("learning_strategy:",learning_strategy)
    print("mantra:",mantra)
    print("financial_goal:",financial_goal)

personal_profile()

#motivation

strength ="Jesus"
beloved = "family"
end_goal = "become a skilled data engineer in supply chain"
watch_out = "rush to finish, nor should you be too eager to start getting money, focuss on providing the solution, remuneration will follow you"

def motivation():
    print("My strength comes from " + strength)
    print("i do it with my " + beloved + " in my heart")
    print("the goal is to " + end_goal)
    print("be careful not to " + watch_out)

motivation()

#Student dashboard

def student_dashboard(name,nationality,language,course,domain):
    print("name:",name)
    print("nationality:",nationality)
    print("language:",language)
    print("course:",course)
    print("domain:",domain)

student_dashboard("joash_d","kenyan","kiswahili","linux","data_engineering")
student_dashboard("rasik","kenyan","english","data engineering","supply chain")