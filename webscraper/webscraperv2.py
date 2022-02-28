# utilizes YouTube Data API v3

from csv import writer
from apiclient.discovery import build 
from apiclient.errors import HttpError
from oauth2client.tools import argparser
from datetime import date
import pandas as pd
import json
import re
import traceback

# This external file contains secure keys.
# Comment out and replace 'youTubeAPIKey' with 
# your own API key.
from keys import *

apiKey = youTubeAPIKey
youtube = build('youtube','v3', developerKey=apiKey)

# Channel ID of youtube Channel
channelID = youtubeID

############## CHANNEL ##############
channelName     = ""
description     = ""
channelStrt     = ""
channelNameLen  = 0     # channel_title_length: length of channel title
channelViews    = 0     # channel_ViewCount: number of views the channel received
linkCount       = 0     # social_links: number of social links mentioned on the channel page
chanDescLen     = 0     # channel_description_length: length of channel description
channelAge      = 0     # channel_months_old: how old the channel is in months
channelSubCnt   = 0     # channel_subscriberCount: number of subscribers the channel has

channelData=youtube.channels().list(part='snippet, statistics',id=channelID).execute()
for i in channelData['items']:
    channelName     = i['snippet']['title']
    description     = i['snippet']['description']
    channelStrt     = i['snippet']['publishedAt']
    channelViews    = int(i['statistics']['viewCount'])
    channelSubCnt   = int(i['statistics']['subscriberCount'])
print(channelViews)

# Channel title length
channelName = channelName.replace(' ','')
channelNameLen = len(channelName)

# Channel description length
description = description.replace('\n','')
description = description.replace(' ','')
chanDescLen = len(description)

# Channel Age in months
formatTime = channelStrt[:channelStrt.index("T")].split("-")
begin = date(int(formatTime[0]), int(formatTime[1]), int(formatTime[2]))
end = date.today()
channelAge = (end.year - begin.year) * 12 + end.month - begin.month



# Need to figure out how to get links


############## VIDEOS ##############
videoCount      = 0
viewCount       = 0     # viewCount: number of views the video received
totalViewCount  = 0
videoDuration   = 0     #duration: length of the video in seconds
videoList = youtube.playlistItems().list(playlistId=listID, part='snippet')

# iterate over every video
while videoList:
    response = videoList.execute()
    for video in response['items']:
        videoCount += 1
        title = video['snippet']['title']
        vidID = video['snippet']['resourceId']['videoId']
        vidReq = youtube.videos().list(part='statistics, contentDetails', id=vidID).execute()
        
        for stats in vidReq['items']:
            # handle video duration
            videoLength = stats['contentDetails']['duration']
            videoLength = videoLength.replace('PT','').replace('H', ' ').replace('M', ' ').replace('S','')
            
            # convert durations to seconds
            extractLength = videoLength.split(' ')
            seconds = 0
            if len(extractLength) == 2:
                mts = int(extractLength[0]) * 60
                videoDuration = mts + int(extractLength[1])
            elif len(exctractLength) == 3:
                htm = int(extractLength[0]) * 60
                mts = int(extractLength[1]) + htm
                videoDuration = mts + int(extractLength[2])
            viewCount = stats['statistics']['viewCount']
            totalViewCount += int(viewCount)
    videoList = youtube.playlistItems().list_next(videoList, response)
print(totalViewCount)

#         # video category
#         # definition
#         # duration
#         # embeddable
#         # licenced?
#         # viewcount per video
#         # viewcount of channel
#         # number of videos on channel
#         # number of subscribers
#         # video description length
#         # number of tags in description
#         # video title length
#         # number of tags in title
#         # tags applied by publisher to video

#         # video age in months

#         # day uploaded




#         # number of socialmedia links