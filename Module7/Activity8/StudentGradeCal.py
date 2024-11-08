#list of test score of a sutdent
scores = [80,79,60,70,90]
#Calculating average score
average_scores = sum(scores)/len(scores)
#updating the grades
print(f"Initial average score :: {average_scores}")
if average_scores%10 >= 5:
    average_scores +=5
    
 #setting grade of a student 
if average_scores >= 90:
    grade = "A"
elif average_scores >= 80:
    grade = "B"
elif average_scores >= 70:
    grade = "C"
elif average_scores >= 60:
    grade = "D"
elif average_scores >= 50:
    grade = "E"
else:
    grade = "F"
print(f"Final average score :: {average_scores}")
print(f"Final grade :: {grade}")

#check if specific score exists in a list
checkScore = 84

if checkScore in scores:
    print(f"{checkScore} is available in the score list.")
else:
    print(f"{checkScore} is not available in the score list.")

#compare objects using identity operator 
scores_copy = scores
if scores is scores_copy:
    print("The scores and scores_copy are same objects.")
else:
    print("The scores and scores_copy are not same objects.")

#Bitwise opration on the scores
and_bitwise = scores[0] & scores[3]
print(f"and_bitwise operation on two elements of scores :: {and_bitwise}")