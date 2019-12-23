# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 18:55:46 2019

@author: raghav.aggiwal
"""

import youtube_dl

#this code download videos with thumbnail image
#tries to download in best quality
#set download_video variable to False if you only want video info

def download_video_with_info(yt_url, download_folder, download_video = True):
  #output template
  outtmpl = download_folder + '\\' + '%(title)s.%(ext)s'

  ydl_opts = {
      'format': 'best',
      'outtmpl': outtmpl,
      'writethumbnail' : True,
      'embedthumbnail' : True
  }

  ydl = youtube_dl.YoutubeDL(ydl_opts)

  print("Trying to Download: ", yt_url)
 
  try:
    info = ydl.extract_info(yt_url, download = download_video)
    
    print("Downloaded : ", info['title'], "\n")
    
  except Exception as e:
    print('Error in Download : ', str(e), "\n")
    return False
    
  return info



if __name__ == "__main__":
  download_folder = r'D:\My Folder'
  yt_url = "https://www.youtube.com/watch?v=c_6jv5X-2h4"
  
  info = download_video_with_info(yt_url = yt_url,
                        download_folder = download_folder,
                        download_video = False)
  

  if info:
    print(info["title"], "\n", info["description"])
  
    