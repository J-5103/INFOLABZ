import numpy as np

from W3DAY1.W3D1 import average, result

students_data = np.array([
 [101, 'Aarav', 10, 88.0, 92.0, 85.0],
 [102, 'Diya', 11, 76.0, 85.5, 78.0],
 [103, 'Vihaan', 12, 90.0, 88.0, 93.5],
 [104, 'Ananya', 10, 72.0, 80.0, 70.0],
 [105, 'Ishaan', 11, 95.0, 90.5, 92.0],
 [106, 'Kiara', 12, 60.0, 75.0, 65.0],
 [107, 'Aditya', 11, 89.0, 91.0, 84.0],
 [108, 'Riya', 10, 78.0, 88.5, 77.0],
 [109, 'Aryan', 12, 92.0, 95.5, 94.0],
 [110, 'Sneha', 10, 85.0, 89.0, 82.0],
 [111, 'Manav', 11, 82.0, 87.0, 88.0],
 [112, 'Tanya', 12, 75.0, 78.0, 80.5],
 [113, 'Aditi', 11, 88.5, 92.0, 90.0],
 [114, 'Raj', 10, 82.0, 86.0, 79.0],
 [115, 'Siddharth', 12, 91.0, 89.5, 93.0],
 [116, 'Nisha', 10, 79.0, 85.0, 81.0],
 [117, 'Kabir', 11, 85.5, 88.0, 87.0],
 [118, 'Meera', 12, 92.0, 94.0, 91.0],
 [119, 'Harsh', 10, 74.0, 77.0, 72.0],
 [120, 'Pooja', 11, 90.0, 91.5, 89.0]
],dtype=object)

# student_id=students_data['Student ID']
# name = students_data["Name"]
# grade_level=students_data["Grade Level"]
# maths_score=students_data["Math Score"]
# science_score=students_data["'Science Score"]
# english_score=students_data["English Score"]

#1.1) Extract the scores for each subject

print(f"\nmaths`s score:{students_data[:,3]},\nscience`s score:{students_data[:,4]},\nenglish`s score:{students_data[:,5]}")

#1.2) Calculate the average, maximum, and minimum scores for Math, Science, and English.
maths_score=np.array(students_data[:,3],dtype=float)
print(maths_score)

avg_maths=np.mean(maths_score)
print("average of maths score:",avg_maths)

max_maths=np.argmax(maths_score)
print(f"maximum of maths score:{max_maths}")

min_maths=np.min(maths_score)
print(f"minimum of maths score:{min_maths}\n")

science_score=np.array(students_data[:,4],dtype=float)
print(science_score)
avg_science=np.mean(science_score)
print("average of science score:",avg_science)

max_science=np.max(science_score)
print(f"maximum of science score:{max_science}")

min_science=np.min(science_score)
print(f"minimum of science score:{min_science}\n")

english_score=np.array(students_data[:,5],dtype=float)
print(english_score)
avg_english=np.mean(english_score)
print("average of english score:",avg_english)

max_english=np.max(english_score)
print(f"maximum of engish score:{max_english}")

min_english=np.min(english_score)
print(f"minimum of english score:{min_english}\n")

#1.3.) Identify the student with the highest average score across all subjects.

average_score= (maths_score + science_score +english_score)/3
highest_avg=np.argmax(average_score)
student_nm=students_data[highest_avg,1]
print(f"highest average score across all subject:{student_nm}")

#2.1) Calculate the average scores for each subject by grade level.


#2.2). Determine which grade level has the highest average Math score
student_name=students_data[:,1]
print(student_name)
grade_level=students_data[:,2]
print(grade_level)
highest_maths_score=np.max(maths_score)
index3=np.where(maths_score==highest_maths_score)
print("this student has highest average maths score: student name:",student_name[index3],",grade level:",grade_level[index3])


#3.1)Select all students with an average score greater than 85.

index4=np.where(average_score>85)
print("student has average score greater 85:",student_name[index4])

#3.2)Find students who scored below 70 in any subject.

index=np.where((maths_score<70) | (science_score<70) | (english_score<70))
print("this student has scored below 70 in any subject:",student_name[index])

#3.3)Identify students in grade 12 with a Science score above 85.

index2=np.where((grade_level==12) & (science_score>85))
print("student grade 12 with science score above 85:",student_name[index2])

#4.1)Compute the overall average score for each student.
print("overall average score for each student:",average_score)

#5.1)Add a new column to the dataset indicating the overall average score for each student.
new_col=np.array(average_score)
result=np.column_stack((students_data,new_col))

print(result)

#5.2)Sort the dataset by average score in descending order.

sorted_data=result[result[:,-1].argsort()[::-1]]
print(sorted_data)

# Students with an average score above 90 receive a "Gold" scholarship.
index5=np.where(average_score>90)
print(f"{student_name[index5]} has Gold scholarship.")

#Students with an average score between 80 and 90 receive a "Silver" scholarship.

index6 = np.where((average_score>80) & (average_score<90))
print(f"{student_name[index6]} has Silver scholarship")

#Students with an average score below 80 receive no scholarship
index7 = np.where(average_score<80)
print(f"{student_name[index7]} has no scholarship")

#Assign the appropriate scholarship category to each student and add it as a new column to the dataset.

scholarship_category=np.full(average_score.shape,"No Scholarship")
scholarship_category[average_score>90]="Gold Scholarship"
scholarship_category[(average_score>80) & (average_score<90)]="Silver Scholarship"

dataset=np.column_stack((result,scholarship_category))
print(dataset)


#Count the number of students eligible for each scholarship category
scholarship=dataset[:,7]
print(scholarship)
index8=np.where(scholarship=="No Scholarship")
print(len(index8))

index9=np.where(scholarship=="Gold Scholarship")
print(index9)















