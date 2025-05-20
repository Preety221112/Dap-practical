import matplotlib.pyplot as plt # type: ignore
import pandas as pd

df = pd.read_csv('student_habits_performance.csv')

plt.figure(figsize=(10, 6))
plt.hist(df['exam_score'], bins=20, color='skyblue', edgecolor='black')
plt.title('Distribution of Exam Scores')
plt.xlabel('Exam Score')
plt.ylabel('Number of Students')
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()

plt.figure(figsize=(10, 6))
plt.scatter(df['study_hours_per_day'], df['exam_score'], alpha=0.6, color='green')
plt.title('Study Hours per Day vs. Exam Score')
plt.xlabel('Study Hours per Day')
plt.ylabel('Exam Score')
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()

gender_scores = df.groupby('gender')['exam_score'].mean()

plt.figure(figsize=(8, 5))
gender_scores.plot(kind='bar', color=['pink', 'lightblue', 'lightgreen'])
plt.title('Average Exam Score by Gender')
plt.xlabel('Gender')
plt.ylabel('Average Exam Score')
plt.xticks(rotation=0)
plt.grid(True, axis='y', linestyle='--', alpha=0.7)
plt.show()

diet_scores = df.groupby('diet_quality')['exam_score'].mean()

plt.figure(figsize=(8, 5))
diet_scores.plot(kind='bar', color=['red', 'yellow', 'green'])
plt.title('Average Exam Score by Diet Quality')
plt.xlabel('Diet Quality')
plt.ylabel('Average Exam Score')
plt.xticks(rotation=0)
plt.grid(True, axis='y', linestyle='--', alpha=0.7)
plt.show()