# Data Science Final Project: The Korean Wave 한류
Dataset associated and released as part of the group's data is included in [Korean Music Groups/Singles Data Set](https://www.kaggle.com/datasets/kimjihoo/kpopdb?resource=download&select=kpop_music_videos.csv)
## Attribute Information
### Attribute 1: Debut Data
- Type: String (TEXT)
- Default Value: There are currently no default values as the dates are ranging from when the Koreans Groups got started. Therefore, a default value would hinder our analysis of how long these groups would survive, where the starting and ending date will be variable.
- Range of Values: The range of values would be variable as well due to the fact that every Korean Group has a different starting debut date and end date. However, most of the korean groups are in the 21st century
Simplified analysis of the distribution of values: The distribution of the debut dates range mostly between the years 2000 and 2023.
- Uniqueness: The debut dates are unique as there are unique korean groups within our table 
- Use this value to detect duplicates: We will use this data to demonstrate how long koreans groups have been active for and demonstrate the correlation to the increase of korean music to international media. 
- Use this attribute in analysis/Required Value: This would be considered a required value as it will be used to calculate the amount of time korean groups have been active
- Sensitive: This date isn’t sensitive as it is publicly available to everyone
### Attribute 2: Number of Members
- Type: Integer (REAL)
- Default Value: The default number of members would be 2 as each group must have at least 2 members within the korean group, or else it would be considered a solo artist 
- Range of Values: The range of values would include somewhere between 2-20 for our data set, however there could be even more as the number of members would be dependent on the group.
- Simplified analysis of the distribution of values: The distribution of data is not uniform as most of the groups have a variable number of members. Most groups do have single digit number of members so between 2-9 members.
- Uniqueness: The number of members would not be distinct as many of the groups could have the same number of singers in them.
- Use this value to detect duplicates: We would not use this value to demonstrate duplicates as it would not help in categorizing the data or finding distinct groups
- Use this attribute in analysis/ Required Value: This would not necessarily be a required value, but it would be used to demonstrate the increase in korean groups sizes over time
- Sensitive: This value is not sensitive as it can be found online for anyone to see
### Attribute 3: Korean Name
- Type: String (TEXT)
- Default Value: There are no default values for Korean names as this is the name of the group in Korean and it would be hard to identify the group without the Korean name. 
- Range of Values:The range of values would most likely be within the Korean alphabet, the Hangul, where each character in the name would demonstrate one of the characters. Also numerically the length of the Korean group name would be between [1, inf)
- Simplified analysis of the distribution of groups: The Korean group name is not necessarily distributed and it would be particularly difficult to do so. However, we can say that there are a uniform distinct number of korean group names
- Uniqueness: The group name is unique to each Korean group and our table has no duplicates
- Use this value to detect duplicates: We would use this value to detect duplicates as the Korean name is the most distinct property. Using the translation of the korean  could cause bias in our data
- Use this attribute in analysis/ Required Value: This would be a required value as this attribute will help us distinguish between groups that might have similar translated group names
- Sensitive: This is not a sensitive attribute as it is open for everyone to see and use
### Attribute 4: Active Status
- Type: String (TEXT)
- Default Value: The default values for Active Status are “Yes”, “No” and “Hiatus”. 
- Range of Status:  The range of the status is between 1 to 3 different values. 
- Simplified analysis of the distribution of values: Overall, most Korean groups are seen to be active, while some are on hiatus or no longer active. This would be a skewed distribution where most groups are active 
- Uniqueness: The status itself is not unique as most of the groups will have the same type of status, however the status would be unique to the group itself, given that there are unique groups. 
- Use this value to detect duplicates: We would not use this value to detect duplicates as the value isn’t unique to the 
- Use this attribute in analysis/ Required Value: This is a required value as it will allow us to see if the group must be considered and how we must calculate the number of years that they have been active. 
- Sensitive: This is not sensitive as their status can be found online for everyone to see
### Attribute 5: Video Id
- Type: String (TEXT)
- Default Value: There are no default values for video ID as this is the ID of the video and each video has a unique ID.
- Range of Values: The range of values would include any combination of English characters and symbols that forms a series.
- Simplified analysis of the distribution of values: The video ID is not necessarily distributed and would be particularly hard to discern a distribution. The video IDs are randomized characters and symbols that combine to form an ID.
- Uniqueness: Each video ID is unique and our table has no duplicates.
- Use this value to detect duplicates: We would use this value to detect duplicates as the video ID’s are completely distinct from one another. Having the same video ID but being a different music video would not make sense for the uniqueness of each video in YouTube.
- Use this attribute in analysis/ Required Value: This would not necessarily be a required value but could be used to differentiate from music video to music video.
- Sensitive: This is not a sensitive attribute as it is open for everyone to see
### Attribute 6: Release Date
- Type: String (TEXT)
- Default Value: There are no default values for upload date as the release date is the date for which the song in the music video was released to the general public.
- Range of Values: The range of releases will be represented in year-month-day format. The most recent release is from 2022-05-22 (May 22, 2022) while the oldest was from 1992-03-23 (March 23, 1992). Hence, all videos were released in between or on these dates.
- Simplified analysis of the distribution of values: The distribution of upload dates is not uniform and increases as time passes due to the increased releasing of KPop related songs with music videos on YouTube in more recent years.
- Uniqueness: Each release date is not necessarily unique as there can be multiple songs with music videos on YouTube that were released on the same day
- Use this value to detect duplicates: This value should not be used to detect duplicates as there can be songs with music videos on YouTube that were released on the same day
- Use this attribute in analysis/ Required Value: We would use this value in our analysis to determine the increase in popularity of Kpop through the frequency in which songs were released in a period of time (i.e. 2014-01-01 to 2017-01-01, 2017-01-01 to 2020-01-01, and so on and so forth)
- Sensitive: This is not a sensitive attribute as it is open for everyone to see
### Attribute 7: Views
- Type: String (TEXT)
- Default Value: There is no default value for views as the views of a music video is dependent on the number of people who view that music video on YouTube, which may vary from music video to music video
- Range of Values: The max number of views for a music video in table is 2033130905 while the minimum value of views is 513. Hence, each music video from the table has views in between or at these number of views.
- Simplified analysis of the distribution of values: This distribution of views is not uniform. It is important to note that the view count of music videos generally increase as the release dates pass due to external factors, such as the easier accessibility of viewing these music videos to younger audiences who may be more likely to access  YouTube and contribute to views.
- Uniqueness: The views of each music video is not necessarily unique. However, it is highly improbably that any music video has the exact same number of views as another music video.
- Use this value to detect duplicates: This value can be used to detect duplicates. However, it is not the surefire means to detect duplicates as two or more videos may coincidentally have the same number of views.
- Use this attribute in analysis/ Required Value: This attribute would be used in analysis to help us determine the increase in views for music videos that were released during a period of time 
- Sensitive: Views is not sensitive as it is open to everyone to see

### Attribute 8: Percent English
- Type: Integer (WHOLE)
- Default Value: The default value would not exist here as each percentage would technically be a whole number representing the percentage of english that is within each korean youtube video 
- Range of Values: The range of values are between 0 and 100 where each value is a percentage
- Simplified analysis of the distribution of values: The distribution is definitely random but mostly between 25 and 75 showing most Korean videos are 25 to 75 percent english. But this can be skewed due to auto generated subtitles.
- Uniqueness: This value is not necessarily unique as the values could be duplicated, however each percentage is unique to the youtube video
- Use this value to detect duplicates: This value won’t be used to detect duplicates as the value is a form of analyzing how much English is in kpop songs. 
- Use this attribute in analysis/ Required Value: This attribute would be considered a required value as the attribute must be used to show how korean songs have been affected by international and global languages such as English
- Sensitive: Percent English is not a sensitive attribute as it can be readily calculated by any viewer by obtaining the ratio of English to total lyrics in a music video.


## Tech Report
Please go to the following link: [Tech Report](https://docs.google.com/document/d/1n0Uyh-afpeXoUiwQXFHr9mCIjvav0BKANuEJmDL_F6E/edit)


## Analysis 
Please go to the following link: [Analysis](https://docs.google.com/document/d/1NzBToV-roybttZNnF0SVukqds4UL_k80Y_n4zNMnkc4/edit)

## Final Submission

Please use the following links:

[Poster](https://docs.google.com/presentation/d/1nv1bRshLrFRDuUkz5q6DyijGgzJlpGK_8ifehgT3uS0/edit)

[Abstract and Socio-historical context and Impact Report](https://docs.google.com/document/d/1LIVgVsMGTto6fNg1a2rTZVQleEgKZZ9svXxBfq0W1bc)

[Recorded presentation](https://drive.google.com/file/d/1shfXoQHp2nV3M-CBwHFymPcNEegUZmJO/view?usp=sharing)
