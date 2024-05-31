StudentName=['James','Jenny','Joanna','Jimmy','Jake','Jone']
StudentMark=[[50,68,79],
             [67,49,78],
             [30,40,40],
             [45,60,50],
             [60,79,89],
             [90,86,84]]

ClassSize = 6#len(StudentName)
SubjectNo = 3#len(StudentMark[0])

AverageMark=0
DistinctionCount=0
MeritCount=0
PassCount=0
FailCount=0

for row in range(0,ClassSize): #for all students in class
    TotalMark=0#set total mark to 0 for all students
    for col in range(0,SubjectNo):
        TotalMark=TotalMark+StudentMark[row][col]
    AverageMark=round(TotalMark/SubjectNo)
    if AverageMark>=70:
        grade="Distinction"
        DistinctionCount+=1
    elif AverageMark>=55:
        grade="Merit"
        MeritCount+=1
    elif AverageMark>=40:
        grade="Pass"
        PassCount+=1
    else:
        grade="Fail"
        FailCount+=1
    print(f"Name:{StudentName[row]}, Combined Total Mark:{TotalMark}, Average Mark:{AverageMark}")

#for displaying how many students got distinction, merit, pass or fail
print(f"Number of Distinctions:{DistinctionCount}")
print(f"Number of Merit:{MeritCount}")
print(f"Number of Pass:{PassCount}")
print(f"Number of Fail Count:{FailCount}")