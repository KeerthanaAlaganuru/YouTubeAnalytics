
# YouTube Dashboard Project

## Overview

This project is a comprehensive YouTube Analytics Dashboard created using Google Looker Studio (formerly Google Data Studio). It provides insights into key YouTube performance metrics by visualizing data exported from the YouTube API. The dashboard enables users to track metrics such as views, watch time, subscriber growth, and engagement rates, offering valuable insights into channel performance.

## Key Features

1. **Data Extraction**: 
   - Used YouTube API to extract important metrics like views, watch time, likes, dislikes, comments, and subscriber count.
   - The data was downloaded for further visualization.

2. **Data Visualization**:
   - The extracted data was imported into Google Looker Studio to create interactive and visually appealing charts and graphs.
   - Visuals include line charts for tracking trends over time, bar charts for comparison, and pie charts for engagement metrics distribution.

3. **Metrics Tracked**:
   - **Views**: Track the total number of video views.
   - **Subscriber Growth**: Analyze daily/weekly/monthly subscriber changes.
   - **Engagement**: Visualize likes, dislikes, comments, and shares.
   - **Top Performing Videos**: Identify the videos generating the most views and engagement.

4. **Dynamic Filters**:
   - Filters were implemented in Looker Studio to allow users to view data by different time periods (daily, weekly, monthly).
   - Data can also be filtered by video or playlists, allowing for specific video performance analysis.

5. **Responsive and Interactive**:
   - The dashboard is designed to be interactive, with features like tooltips and clickable elements to drill down into specific video metrics.
   - Responsive design ensures it looks good on different screen sizes.

## Steps to Develop the Dashboard

1. **YouTube API Data Collection**:
   - Authenticate with the YouTube Data API.
   - Download relevant metrics such as views, watch time, subscriber count, and engagement data.

2. **Data Preparation**:
   - Format the downloaded data into a CSV/Google Sheets file for compatibility with Looker Studio.
   - Clean and organize the data for better visualization (removing unnecessary columns, adding calculated fields like engagement rate).

3. **Create Looker Studio Report**:
   - Open Google Looker Studio.
   - Import the cleaned data file from Google Sheets or CSV into the dashboard.
   - Build visuals for each key metric (views, subscribers, engagement, etc.).
   
## Technologies Used

- **YouTube API**: For extracting video and channel analytics.
- **Google Looker Studio**: For creating and sharing the dashboard.
- **Google Sheets/CSV**: For organizing and formatting the data.
