student1="Preethi R U"
student2="Nayana M S"
student3="Punja"
student4="Raakshasi"

student_names=["Preethi R U","Nayana M S","Punja","Raakshasi"];

print(student_names)

print(student_names[1])

print(student_names[0])

student_names[0]="Preethuu"
print(student_names)

student_names.append("pree")
print(f" added pree :{student_names}")

student_names.remove("pree")
print(f" remove pree :{student_names}")

student_names.remove("Preethuu")
print(f" remove Preethuu :{student_names}")

student_names.insert(1,"NP")
print(student_names)

student_names.insert(2,"Nayuu")
print(student_names)

student_names.insert(3,"Gowrii")
print(student_names)

student_names.insert(4,"tejuu")
print(student_names)


student_names.insert(5,"shrikuu")
print(student_names)


student_names.pop(1)
print(student_names)

student_names.pop(0)
print(student_names)

print(f" Length of list:{len(student_names)}")

print(student_names.reverse())
print(student_names)
