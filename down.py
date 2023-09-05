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

# -- Configurations --------------------------------------------

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
COOKIES_CONFIG = ('brave')

# Set the following two up if USE_COOKIES is False
USERNAME = 'your_username'
PASSWORD = 'your_password'

# Location to your URL list file
URLS_FILE = 'urls.txt'

# Output directories
# All outputs will be placed in ./out/ (the home dir), with temporary files placed
# in ./out/temp/ (the temp dir).
OUT_DIRS = {
    'home': 'out',
    'temp': 'temp'
}

# Whether to download only audio or video+audio
AUDIO_ONLY = False

# Whether to download and embed subtitles into media containers
# (All available languages will be downloaded)
# Note that only the following container formats support subtitle embedding:
# mp4, mov, m4a, webm, mkv, mka files. For the rest embedding will be skipped.
EMBED_SUB = True

# Whether to download and embed metadata into media containers
EMBED_META = True

# Whether to download and embed thumbnails into media containers
EMBED_THUMBNAIL = True

# yt-dlp can log identifiers of all downloaded videos so that only new
# videos from a playlist is downloaded; set it to `None` if you don't need
# this feature and don't like the log file to be generated in program's
# root directory.
DOWN_HISTORY_FILE = 'download_history.log'

# ----------------------------------------------------------------

# Parameters passed to youtube-dl
# For complete list of available options, check out the comments (search for
# 'Available options') in ydl's source code:
# https://github.com/yt-dlp/yt-dlp/blob/master/yt_dlp/YoutubeDL.py

ydl_opts = {
    'paths': OUT_DIRS,

    # -- Set up how the downloaded files are renamed and organized --------------
    # Ref: https://github.com/yt-dlp/yt-dlp#output-template

    # Template for video playlists

    'outtmpl': '%(playlist)s/%(playlist_index)s- %(title)s.%(ext)s',

    # Template for single video urls

    # 'outtmpl': '%(title)s - %(uploader)s.%(ext)s',

    # -- Subtitle download settings ---------------------------------------

    'writesubtitles': EMBED_SUB,
    # 'subtitleslangs': ['en'],
    'allsubtitles': True,
    'subtitlesformat': 'ass/srt/best',

    # -- Post-processor settings ------------------------------------------
    # A complete list of available post-processors and their configs can be found in:
    # https://github.com/yt-dlp/yt-dlp/blob/69dbfe01c47cd078682a87f179f5846e2679e927/yt_dlp/__init__.py#L592
    # (Switch to the `master` branch to see options for the latest version)

    'postprocessors': [],

    # ---------------------------------------------------------------------

    'writethumbnail': EMBED_THUMBNAIL,

    'download_archive': DOWN_HISTORY_FILE,

    # Number of fragments of a dash/hlsnative video that should be
    # downloaded concurrently.
    'concurrent_fragment_downloads': 5
}

# ===== Authentication =====

if USE_COOKIES:
    ydl_opts['cookiesfrombrowser'] = COOKIES_CONFIG
elif USE_COOKIES is not None:
    ydl_opts.update({
        'username': USERNAME,
        'password': PASSWORD
    })

if not AUDIO_ONLY:
    # ===== Video download =====

    # The following means "download `bestvideo` and `bestaudio` separately and
    # mux them together into a single file giving the best overall quality
    # available; if not available, fall back to `best` and download the best
    # available quality served as a single file".
    # More options: https://github.com/yt-dlp/yt-dlp#format-selection

    ydl_opts['format'] = 'bestvideo*+bestaudio/best'

    # -----------------

    # The following simply download the best available quality served as a
    # single file. Note that this may not download the best available quality
    # in websites such as YouTube, since they separate video and audio tracks
    # for videos with resolution higher than 720p.
    #
    # You can further adjust the definition of `best` by tuning the sorting format:
    # https://github.com/yt-dlp/yt-dlp#sorting-formats

    # ydl_opts['format'] = 'best'
    ## ... but with the smallest video size available
    # ydl_opts['format_sort'] = ('+size', '+br')

    ####################

    # Containers that may be used when merging formats.
    # Ignored if no merge is required.
    # Ref: https://github.com/yt-dlp/yt-dlp#video-format-options
    ydl_opts['merge_output_format'] = 'mp4/mkv'

    if EMBED_SUB:
        ydl_opts['postprocessors'].append(
            # Converts downloaded subtitles to another format, e.g. vtt -> srt.
            # All supported formats: https://github.com/yt-dlp/yt-dlp#post-processing-options
            {
                'key': 'FFmpegSubtitlesConvertor',
                'format': 'srt'
            })

else:
    # ===== Audio download =====
    # The following will first download audio track with the best possible
    # quality, then convert to mp3 with a bit rate of 192 kbps.

    ydl_opts['format'] = 'bestaudio/best'

    ydl_opts['postprocessors'].append(
        {
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            # 'preferredquality': '128'  # Bit rate (Set it to 256 for YouTube Premium)
        })

    if EMBED_SUB:
        ydl_opts['postprocessors'].append(
            # Converts downloaded subtitle to lyric format (lrc)
            {
                'key': 'FFmpegSubtitlesConvertor',
                'format': 'lrc'
            })

# ===== General post-processors =====

if EMBED_META:
    ydl_opts['postprocessors'].append(
        # Embeds metadata to the video file.
        # They can be read using tools e.g. MediaInfo
        {
            'key': 'FFmpegMetadata',
            'add_chapters': True,
            'add_metadata': True,
        })

if EMBED_THUMBNAIL:
    # ydl_opts['postprocessors'].append(
    #     {
    #         'key': 'FFmpegThumbnailsConvertor',
    #         # Convert .webp or .png to .jpg
    #         'format': 'jpg'
    #     })
    ydl_opts['postprocessors'].append(
        # Embeds thumbnail in the video as cover art.
        # Note that webm does not support thumbnail embedding
        {
            'key': 'EmbedThumbnail',
            # Set it to `True` to prevent the file from being deleted after embedding
            'already_have_thumbnail': False
        })

if EMBED_SUB:
    ydl_opts['postprocessors'].append(
        # Embeds subtitles in the video (only for mp4, mov, m4a, webm, mkv, mka files).
        {
            'key': 'FFmpegEmbedSubtitle',
            # Set it to `True` to prevent the file from being deleted after embedding
            'already_have_subtitle': False 
        })

# ----------------------------------------------------------------

# Read all video / audio URLs to be downloaded
urls = None
with open(URLS_FILE, mode='r') as f:
    urls = [line.strip() for line in f]

if urls:
    with YoutubeDL(ydl_opts) as ydl:
        # This is equivalent to the following command line executed once for
        # each URL:
        # yt-dlp --cookies cookies.txt --all-subs --write-sub --sub-format "srt" -f "best" -o "Lynda.com- %(playlist)s/%(chapter)s/%(playlist_index)s- %(title)s.%(ext)s" "YOUR_URL"
        ydl.download(urls)
else:
    print('Please check whether the location of', URLS_FILE, 'is correct and the file is not empty.')
