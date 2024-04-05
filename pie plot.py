import pandas as pd
import matplotlib.pyplot as plt

# Reading the dataset
df = pd.read_csv("better-training-for-safer-foods-april-2016-to-march-2017.csv")

# Getting the top 10 most common courses
top_10_courses = df['CourseName'].value_counts().nlargest(10)

# Plotting
plt.figure(figsize=(8, 8))
plt.pie(top_10_courses, labels=top_10_courses.index, autopct='%1.1f%%', startangle=140)
plt.title('Top 10 Training Courses')
plt.axis('equal')
plt.tight_layout()
plt.show()
