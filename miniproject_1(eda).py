# -*- coding: utf-8 -*-
"""MiniProject_1(EDA).ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1_Jqi7jIxIadRvL95SW9Kzp295IyTrmLX

# **Importing Libraries**
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

"""#**Loading file**"""

# Load the data from CSV file
file_path = 'AlexTheAnalyst_1.csv'
all_video_data = pd.read_csv(file_path)

"""# **Top 10 videos by VIEWS**"""

import seaborn as sns
import matplotlib.pyplot as plt

# Get top 10 videos by views
top10_videos = all_video_data.sort_values(by='Views', ascending=False).head(10)
top10_videos['Views_in_lakhs'] = top10_videos['Views'] / 100000

# Create the bar plot
plt.figure(figsize=(5,5))
top_videos_plot = sns.barplot(x='Views_in_lakhs', y='Videotitles', data=top10_videos, palette='viridis')

# Set the title and labels
top_videos_plot.set_title('Top 10 Videos by Views')
top_videos_plot.set_xlabel('Views (in lakhs)')
top_videos_plot.set_ylabel('VideoTitles')

# Show the plot
plt.show()

"""# **Monthly uploads**"""

# Calculate the number of videos uploaded in each month
videos_per_month = all_video_data.groupby('Month', as_index=False).size()

# Sort the data by month
sort_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
videos_per_month.index = pd.CategoricalIndex(videos_per_month['Month'], categories=sort_order, ordered=True)
videos_per_month = videos_per_month.sort_index()

# Create the bar plot
plt.figure(figsize=(5,5))
monthly_uploads_plot = sns.barplot(x='Month', y='size', data=videos_per_month, palette='cubehelix')

# Set the title and labels
monthly_uploads_plot.set_title('Monthly Video Uploads')
monthly_uploads_plot.set_xlabel('Month')
monthly_uploads_plot.set_ylabel('Number of Videos')

# Show the plot
plt.show()

"""# **Yearly Uploads**"""

# Ensure Published_date is in datetime format
all_video_data['Published_date'] = pd.to_datetime(all_video_data['Published_date'], errors='coerce')

# Drop rows with missing Published_date
all_video_data.dropna(subset=['Published_date'], inplace=True)

# Extract the year from Published_date
all_video_data['Year'] = all_video_data['Published_date'].dt.year

# Calculate the number of videos uploaded each year
videos_per_year = all_video_data.groupby('Year').size().reset_index(name='Count')

# Create the bar plot
plt.figure(figsize=(5,5))
sns.barplot(x='Year', y='Count', data=videos_per_year, palette='Dark2')

# Setting the title and labels
plt.title('Year-wise Uploaded Videos')
plt.xlabel('Year')
plt.ylabel('No. of Videos Uploaded')

# Adjusting the y-axis ticks to show units in multiples of 10
plt.yticks(range(0, int(videos_per_year['Count'].max()) + 10, 10))

# Show the plot
plt.show()

"""# **Relationship between views,comments,likes**"""

# Pair plot to visualize the relationships
sns.pairplot(all_video_data[['Views', 'Likes', 'Comments']])
plt.suptitle('Relationships Between Views, Likes, and Comments', y=1.02)
plt.show()

"""# **Plot Distributions**"""

# Distribution of Views
plt.figure(figsize=(5,5))
sns.histplot(all_video_data['Views'], bins=50, kde=True, color='blue')
plt.title('Distribution of Views')
plt.xlabel('Views')
plt.ylabel('Frequency')
plt.show()

# Distribution of Likes
plt.figure(figsize=(5,5))
sns.histplot(all_video_data['Likes'], bins=50, kde=True, color='green')
plt.title('Distribution of Likes')
plt.xlabel('Likes')
plt.ylabel('Frequency')
plt.show()

# Distribution of Comments
plt.figure(figsize=(5,5))
sns.histplot(all_video_data['Comments'], bins=50, kde=True, color='red')
plt.title('Distribution of Comments')
plt.xlabel('Comments')
plt.ylabel('Frequency')
plt.show()

"""#**Time Series Analysis**"""

# Combine Year and Month columns to create a Published_date column
all_video_data['Published_date'] = pd.to_datetime(all_video_data['Year'].astype(str) + '-' + all_video_data['Month'] + '-01')

# Set the Published_date as the index
all_video_data.set_index('Published_date', inplace=True)

# Plotting time series data
plt.figure(figsize=(8, 5))

# Plot Views over time
plt.plot(all_video_data.resample('M').sum()['Views'], label='Views', color='blue')

# Plot Likes over time
plt.plot(all_video_data.resample('M').sum()['Likes'], label='Likes', color='green')

# Plot Comments over time
plt.plot(all_video_data.resample('M').sum()['Comments'], label='Comments', color='purple')

# Set title and labels
plt.title('Time Series of Views, Likes, and Comments')
plt.xlabel('Date')
plt.ylabel('Count (Views, Likes, Comments)')

# Adding grid for better readability of the scales
plt.grid(True)

# Adding legend
plt.legend()

# Show the plot
plt.show()

"""# **Correlation Analysis**"""

# Calculate correlation matrix
correlation_matrix = all_video_data[['Views', 'Likes', 'Comments']].corr()

print(correlation_matrix)

# Plotting the correlation matrix
plt.figure(figsize=(5,5))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Matrix of Views, Likes, and Comments')
plt.show()

"""# **Scatter Plot**"""

# Scatter plot with regression line for Views vs Likes
plt.figure(figsize=(5,5))
sns.regplot(x='Views', y='Likes', data=all_video_data, scatter_kws={'s':10}, line_kws={'color':'red'})
plt.title('Views vs Likes')
plt.xlabel('Views')
plt.ylabel('Likes')
plt.show()

# Scatter plot with regression line for Views vs Comments
plt.figure(figsize=(5,5))
sns.regplot(x='Views', y='Comments', data=all_video_data, scatter_kws={'s':10}, line_kws={'color':'red'})
plt.title('Views vs Comments')
plt.xlabel('Views')
plt.ylabel('Comments')
plt.show()

# Scatter plot with regression line for Likes vs Comments
plt.figure(figsize=(5,5))
sns.regplot(x='Likes', y='Comments', data=all_video_data, scatter_kws={'s':10}, line_kws={'color':'red'})
plt.title('Likes vs Comments')
plt.xlabel('Likes')
plt.ylabel('Comments')
plt.show()