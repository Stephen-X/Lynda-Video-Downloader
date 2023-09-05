# Lynda.com Video Downloader

**Note: you must have a valid [Lynda.com](https://www.lynda.com/) subscription to download paid contents.**

A convenient script for downloading and organizing [Lynda.com](https://www.lynda.com/) course videos and subtitles in batch.


## Usage

1. Make sure you have Python 3.7+ installed and accessible via command line, then install [yt-dlp](https://github.com/yt-dlp/yt-dlp/wiki/Installation) by `pip install yt-dlp`. If you have both Python 2 and 3 installed in your system, check that you're using the correct `pip` alias for the target python version (e.g. it could be `pip3` for Python 3).

2. Install [FFmpeg](https://www.ffmpeg.org/), and make sure it's accessible via command line. It is required to mux video and audio into one single file when downloading from sites like YouTube (they keep videos and audios with *best possible* qualities to their separate files). I recommend that you use a package manager to install it. On Windows, you may install [Scoop](https://scoop.sh/) then `scoop install ffmpeg`; on MacOS, you may install [Homebrew](https://brew.sh/) then `brew install ffmpeg` for FFmpeg ([More options](https://trac.ffmpeg.org/wiki/CompilationGuide/macOS#ffmpegthroughHomebrew)).

3. (Optional) Set up your credentials. There're two scenarios:
    1) You have your own Lynda.com account:

        Set line 26 of `down.py` to `USE_COOKIES = False`, then fill in your username and password in line 37 and 38.

    2) Your Lynda.com account is associated with your organization account, i.e. you sign in with your organization portal:

        2.1. Log into your account using your preferred browser. Supported browsers are listed in the documentation for [`--cookies-from-browser`](https://github.com/yt-dlp/yt-dlp#filesystem-options).

        2.2. Set line 26 of `down.py` to `USE_COOKIES = True`. Modify line 34 to instruct yt-dlp to load cookies from the target browser.

4. Put URLs of all courses that you wish to download inside a file named `urls.txt` and place it in the same directory as `down.py`. Here I included a sample `urls.txt` file (FYI the included courses are from the famous Adobe Photoshop & Illustrator One-on-One series by [Deke McClelland](https://www.deke.com/)), but you should remember to clear the file content first if you'd like to download something else.

5. Run the script by `./down.py` or `python down.py` (similar to stated previously, check your `python` alias if you have both Python 2 and 3 installed on your system). It will download specified courses to the same directory as `down.py`. Here's a sample download outcome after running the script with the sample URLs:

```
Lynda.com- Photoshop CC 2018 One-on-One - Fundamentals
├── Introduction
│   ├── 001- Welcome.en.srt
│   ├── 001- Welcome.mp4
│   ├── 002- Updates to the Photoshop CC 2018 interface.en.srt
│   └── 002- Updates to the Photoshop CC 2018 interface.mp4
├── 1. Opening an Image
│   ├── 003- How it all starts.en.srt
│   ├── 003- How it all starts.mp4
│   ├── 004- Opening from the Windows desktop.en.srt
│   ├── 004- Opening from the Windows desktop.mp4
│   ├── ...
├── 2. Getting Around
│   ├── 010- Navigating your image.en.srt
│   ├── 010- Navigating your image.mp4
│   ├── 011- Zooming in and out.en.srt
│   ├── 011- Zooming in and out.mp4
│   ├── 012- Using the more precise Zoom tool.en.srt
│   ├── 012- Using the more precise Zoom tool.mp4
│   ├── ...
├── ...
└── Conclusion
    ├── 177- Until next time.en.srt
    └── 177- Until next time.mp4
Lynda.com- Illustrator CC 2018 One-on-One Fundamentals
├── ...
...
```

FYI for Windows users, if you're looking for an all-purpose media player that can recognize subtitle languages from file names shown above, I'd suggest [Potplayer](https://potplayer.daum.net/) by Kang Yong-Huee, the original author of the famous KMPlayer.


## Notes

**2023-09-04**: This was originally written for `youtube-dl`. The script has since been updated to use the more powerful folk [`yt-dlp`](https://github.com/yt-dlp/yt-dlp). 

This is just a wrapper program of the wonderful [youtube-dl](http://rg3.github.io/youtube-dl/), a powerful command-line tool that allows you to conveniently download videos, audios, playlists and episodes from [many websites](http://rg3.github.io/youtube-dl/supportedsites.html). My intention of creating this script is to provide a simple cross-platform wrapper script that can quickly download multiple courses / playlists without going through the entire lengthy [documentation](https://github.com/rg3/youtube-dl/blob/master/README.md) (I got you covered there :wink:). __In fact, with minor or no tweaking, this script can also be reused to download contents from other websites such as courses on Udemy, TV episodes on YouTube or music collections on SoundCloud!__ All credits go to the [contributors](http://rg3.github.io/youtube-dl/about) behind `youtube-dl`! :heart_eyes:
