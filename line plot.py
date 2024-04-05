import pandas as pd
import matplotlib.pyplot as plt

# Reading the dataset
df = pd.read_csv("better-training-for-safer-foods-april-2016-to-march-2017.csv")

# Converting DateFrom and DateTo columns to datetime
df['DateFrom'] = pd.to_datetime(df['DateFrom'])
df['DateTo'] = pd.to_datetime(df['DateTo'])

# Group by DateFrom and count the number of attendees
attendance_data = df.groupby('DateFrom')['Attendees'].sum().reset_index()

# Plotting the line plot (Time-series) 
plt.figure(figsize=(10, 6))
plt.plot(attendance_data['DateFrom'], attendance_data['Attendees'], marker='o')
plt.title('Attendance Over Time')
plt.xlabel('Date')
plt.ylabel('Total Attendees')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
