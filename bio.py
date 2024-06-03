yourName = input("Please enter your name: ")
yourCompany = input("Please enter the company you work for: ")
myName = "Joe Albrecht"
myGoal = "aspiring Jr Software Engineer"

myAttributes = [ "Continual Learner", "Creative", "Disciplined", "Self-Starter", "Gym Enthusiast", "Collaborative" ]
nssInstructors = ["(Coach Steve", "Greg Korte", "Valerie Freeman)"]
nssLessons = ["Working as a remote team", "Problem Solving", "and PLANNING!!(before coding)." ]
technicalSkills = ["JavaScript", "React", "HTML & CSS", "Python", "Django", "SQLite3", "OOP fundamentals", 
                   "Git/GitHub", "ERDs", "Sequence Diagrams", "and Wireframing"]

def welcomeToMyProfile():
    return f"""

Hey {yourName}, it's a pleasure to meet you!

My name is {myName}, and if you couldn't tell by now I am a {myGoal} (starting my job hunt)! 
Over the past 6 months at NSS me and my classmates have been plunged into the dark murky waters of programming. 
We have been tortured by error codes and have had countless BUGs crawling in the code... BUT 
throughout all of the frustration and confusion we have emerged victorious! 

However most importantly the amazing team of instructors{", ".join(nssInstructors)} have taught us many valuable lessons.

Some of those include: {", ".join([i for i in nssLessons])} 

They have also taught us the fundamentals of: {" | ".join(technicalSkills)}. 
{"--" * 5}
My favorite thing about NSS and IMO most valuable part was the sprints we did for group projects. Learning how to code as a team 
was challenging at first (juggling branches, merge conflicts, picking & grading tickets) but we dealt with those  
issues together and we are all better for it. My favorite part about the sprints was when someone on the team had an issue
so we would all come together to solve it or struggle through it together and then reflect on what caused the issue so that
everyone understood it.

With that said, for my job search this is the type of company that i will be looking for.. one that is characterized by 
effective team work, continual learning and mutual support. 

Thank you {yourName} for taking the time to read my bio, I wanted to do something fun with it :)

Sincerely {myName}, {myGoal} at {yourCompany}
"""

print(welcomeToMyProfile())