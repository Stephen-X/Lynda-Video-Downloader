#!/usr/bin/env python3
"""
A convenient wrapper program of yt-dlp (youtube-dl fork) for downloading and organizing
course videos and subtitles from Lynda.com.

Ref: https://github.com/yt-dlp/yt-dlp#embedding-yt-dlp
"""

# I heard that people don't upgrade their Python packages often...
import sys
import subprocess
# Call pip through the current Python executable to avoid installing packages
# to the wrong Python distribution
subprocess.call([sys.executable, '-m', 'pip', 'install', '-U', 'yt-dlp'])
# subprocess.call(['mamba', 'update', 'yt-dlp'])

from yt_dlp import YoutubeDL

# -- Set up parameters --------------------------------------------

# If your Lynda account uses organization login, then you should supply cookies
# instead of username and password to yt-dlp.
# Set this to `True` to use cookies to authenticate, `False` to use username+password,
# `None` to disable login.
USE_COOKIES = None
# Name of the browser to load cookies from. Supported browsers:
# https://github.com/yt-dlp/yt-dlp#filesystem-options
# Format: A tuple containing (1) the name of the browser, (2) the profile name/path
# from where cookies are loaded, (3) the name of the keyring, and
# (4) the container name, e.g. ('chrome', ) or ('vivaldi', 'default', 'BASICTEXT')
# or ('firefox', 'default', None, 'Meta')
COOKIES_CONFIG = ('brave', )
# Set the following two up if USE_COOKIES is False
USERNAME = 'your_username'
PASSWORD = 'your_password'
# Location to your URL list file
URLFILE = 'urls.txt'
# Would you like to download subtitles as well? (All available languages will
# be downloaded)
DOWN_SUB = True

# ----------------------------------------------------------------

# Parameters passed to youtube-dl
# For complete list of available options, check out the comments (search for
# 'Available options') in ydl's source code:
# https://github.com/yt-dlp/yt-dlp/blob/master/yt_dlp/YoutubeDL.py
ydl_opts = {
    # -- For video downloads ----------------------------------------------
    # More options: https://github.com/yt-dlp/yt-dlp#format-selection

    # The following means "download `bestvideo` and `bestaudio` separately and
    # mux them together into a single file giving the best overall quality
    # available; if not available, fall back to `best` and download the best
    # available quality served as a single file".

    'format': 'bestvideo*+bestaudio/best',

    'merge_output_format': 'mp4/mkv',

    # The following simply download the best available quality served as a
    # single file. Note that this may not download the best available quality
    # in websites such as YouTube, since they separate video and audio tracks
    # for videos with resolution higher than 720p.

    # 'format': 'best',

    # -- For audio downloads ---------------------------------------------

    # The following will first download audio track with the best possible
    # quality, then convert to mp3 with a bit rate of 192 kbps.
    # Look here for a complete list of available postprocessors (remember to
    # first remove the last 'PP' from the postprocessor names):
    # https://github.com/yt-dlp/yt-dlp/blob/master/yt_dlp/postprocessor/__init__.py
    # and check out the constructor of the source code of selected
    # postprocessors for available options.

    # 'format': 'bestaudio/best',
    # 'postprocessors': [{
    #     'key': 'FFmpegExtractAudio',
    #     'preferredcodec': 'mp3',
    #     'preferredquality': '192'  # bit rate
    # }],

    # -- Set up how the downloaded files are renamed and organized --------------
    # Ref: https://github.com/yt-dlp/yt-dlp#output-template

    # Template for video playlists

    'outtmpl': '%(playlist)s/%(playlist_index)s- %(title)s.%(ext)s',

    # Template for single video urls

    # 'outtmpl': '%(title)s - %(uploader)s.%(ext)s',

    # -- Subtitle download settings ---------------------------------------

    'writesubtitles': DOWN_SUB,
    # 'subtitleslangs': ['en'],
    'allsubtitles': True,
    'subtitlesformat': 'ass/srt/best',

    # ---------------------------------------------------------------------

    # youtube-dl can log identifiers of all downloaded videos so that only new
    # videos from a playlist is downloaded; comment this out if you don't need
    # this feature and don't like the log file to be generated in program's
    # root directory.

    'download_archive': 'download_history.log',

    # Number of fragments of a dash/hlsnative video that should be
    # downloaded concurrently.

    'concurrent_fragment_downloads': 5
}
if USE_COOKIES:
    ydl_opts['cookiesfrombrowser'] = COOKIES_CONFIG
elif USE_COOKIES is not None:
    ydl_opts.update({
        'username': USERNAME,
        'password': PASSWORD
    })

# URLs of the Lynda courses to be downloaded
urls = None
with open(URLFILE, mode='r') as f:
    urls = [line.strip() for line in f]

if urls:
    with YoutubeDL(ydl_opts) as ydl:
        # This is equivalent to the following command line executed once for
        # each URL:
        # yt-dlp --cookies cookies.txt --all-subs --write-sub --sub-format "srt" -f "best" -o "Lynda.com- %(playlist)s/%(chapter)s/%(playlist_index)s- %(title)s.%(ext)s" "YOUR_URL"
        ydl.download(urls)
else:
    print('Please check whether the location of urls.txt is correct and the file is not empty.')
