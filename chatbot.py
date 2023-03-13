import random

print("What is your name?")
name = input()

messages = [
    [["hello", "hello friend", "sup", "hi"], "hello friend", "sup", "hi"], 
    [["by", "good by", "byby"], "good by", "byby"]
    ]

def caculate_percentages(data):
        grade = 0
        grades = []
        split_responses = []
        for lists in messages:
             for messagedata in lists[0]:
                  split_responses.extend(messagedata.split())
             
             #determines grade
             for words in split_responses:
                  if words in data:
                       grade = grade + 1

             #determines percent
             grades.append(grade / len(split_responses))
             split_responses = []
             grade = 0
        return grades

def determine_response(input):
    words = input.split()
    the_grades = caculate_percentages(words)
    highest_value = max(the_grades)
    highest_index = the_grades.index(highest_value)
    correct_choice = messages[highest_index]
    return random.choice(correct_choice[1:])
    
    
    

while True:
     print(determine_response(input("You: ").lower()))