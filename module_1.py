grades = [[2,4,5,2,4],[2,4,5,3,4],[4,3,3,4,5,4],[4,3,4,2,5,4,3,4,5,3]]
students = {'Petrov','Vasilev','Averin','Kurochkin','Verin'}
print(grades)
print(students)
students_l = list(students)
students_l.sort()
avg_b = []
ind = 0
for j in grades:
    b = len(grades[ind])
    count = 0
    for i in grades[ind]:
        count+=i
    avg_b.append(count/b)
    ind = ind + 1
Student_avg_b = {}
ind_n=0
for i in avg_b:
    Student_avg_b.update({str(students_l[ind_n]):i})
    ind_n=ind_n+1
print(Student_avg_b)

