import pandas as pd
import numpy as np
import matplotlib.pyplot as plt # type: ignore

# 1. Load the data
df = pd.read_csv('student_habits_performance.csv')

## 2. Correlation Analysis
numeric_cols = df.select_dtypes(include=[np.number]).columns
corr_matrix = df[numeric_cols].corr()

# Plot correlation matrix
plt.figure(figsize=(12, 10))
plt.imshow(corr_matrix, cmap='coolwarm', interpolation='nearest')
plt.colorbar()
plt.xticks(range(len(corr_matrix.columns)), corr_matrix.columns, rotation=90)
plt.yticks(range(len(corr_matrix.columns)), corr_matrix.columns)
plt.title('Correlation Matrix of Student Data')
plt.show()

# Top correlations with exam score
exam_corr = corr_matrix['exam_score'].sort_values(ascending=False)

## 3. Key Visualizations

# Study Hours vs Exam Score
plt.figure(figsize=(10, 6))
for gender in df['gender'].unique():
    subset = df[df['gender'] == gender]
    plt.scatter(subset['study_hours_per_day'], subset['exam_score'], 
                alpha=0.6, label=gender)
plt.title('Study Hours vs Exam Score')
plt.xlabel('Study Hours per Day')
plt.ylabel('Exam Score')
plt.legend()
plt.grid(True)
plt.show()

# Sleep Hours vs Exam Score (boxplot)
sleep_bins = [0, 5, 7, 9, 12]
sleep_labels = ['0-5', '5-7', '7-9', '9+']
df['sleep_range'] = pd.cut(df['sleep_hours'], bins=sleep_bins, labels=sleep_labels)

plt.figure(figsize=(10, 6))
data_to_plot = [df[df['sleep_range'] == r]['exam_score'] for r in sleep_labels]
plt.boxplot(data_to_plot, labels=sleep_labels)
plt.title('Sleep Hours vs Exam Score')
plt.xlabel('Sleep Hours Range')
plt.ylabel('Exam Score')
plt.grid(True)
plt.show()

# Entertainment Hours vs Exam Score
df['entertainment_hours'] = df['social_media_hours'] + df['netflix_hours']
plt.figure(figsize=(10, 6))
for gender in df['gender'].unique():
    subset = df[df['gender'] == gender]
    plt.scatter(subset['entertainment_hours'], subset['exam_score'], 
                alpha=0.6, label=gender)
plt.title('Entertainment Hours vs Exam Score')
plt.xlabel('Daily Entertainment Hours (Social Media + Netflix)')
plt.ylabel('Exam Score')
plt.legend()
plt.grid(True)
plt.show()

# Attendance vs Exam Score
plt.figure(figsize=(10, 6))
plt.scatter(df['attendance_percentage'], df['exam_score'], alpha=0.6)
plt.title('Attendance Percentage vs Exam Score')
plt.xlabel('Attendance Percentage')
plt.ylabel('Exam Score')
plt.grid(True)

# Add regression line
z = np.polyfit(df['attendance_percentage'], df['exam_score'], 1)
p = np.poly1d(z)
plt.plot(df['attendance_percentage'], p(df['attendance_percentage']), "r--")
plt.show()

# Parental Education vs Exam Score
plt.figure(figsize=(10, 6))
order = ['None', 'High School', 'Bachelor', 'Master']
data_to_plot = [df[df['parental_education_level'] == l]['exam_score'] for l in order]
plt.boxplot(data_to_plot, labels=order)
plt.title('Parental Education Level vs Exam Score')
plt.xlabel('Parental Education Level')
plt.ylabel('Exam Score')
plt.grid(True)
plt.show()

# Mental Health vs Exam Score
plt.figure(figsize=(10, 6))
data_to_plot = [df[df['mental_health_rating'] == r]['exam_score'] 
               for r in sorted(df['mental_health_rating'].unique())]
plt.boxplot(data_to_plot, labels=sorted(df['mental_health_rating'].unique()))
plt.title('Mental Health Rating vs Exam Score')
plt.xlabel('Mental Health Rating (1-10)')
plt.ylabel('Exam Score')
plt.grid(True)
plt.show()

