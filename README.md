# Lynda.com Video Downloader

**Note: you must have a valid [Lynda.com](https://www.lynda.com/) subscription to download paid contents.**

A convenient script for downloading and organizing [Lynda.com](https://www.lynda.com/) course videos and subtitles in batch.


## Usage

1. Make sure you have Python (either 2 or 3) installed and accessible via command line, then install [youtube-dl](http://rg3.github.io/youtube-dl/) by `pip install youtube-dl`. If you have both Python 2 and 3 installed in your system, check that you're using the correct `pip` alias for the target python version (e.g. it could be `pip3` for Python 3).

2. Set up your credentials. There're two scenarios:
    1) You have your own Lynda.com account:

        Set line 15 of `down.py` to `USE_COOKIES = False`, then fill in your username and password in line 19 and 20.

    2) Your Lynda.com account is associated with your organization account, i.e. you sign in with your organization portal:

        2.1. Install the [cookies.txt](https://chrome.google.com/webstore/detail/cookiestxt/njabckikapfpffapmjgojcnbfjonfjfg) Chrome extension, log in to [Lynda.com](https://www.lynda.com/) with your organization portal, then dump the cookies of the Lynda site using the extension (click the extension icon, then click "To download cookies for this tab click here" in the pop-up window). Save your cookies as `cookies.txt` and place it in the same directory as `down.py`.

        2.2. Set line 15 of `down.py` to `USE_COOKIES = True`.

3. Put URLs of all courses that you wish to download inside a file named `urls.txt` and place it in the same directory as `down.py`. Here I included a sample `urls.txt` file (FYI the included courses are from the famous Adobe Photoshop & Illustrator One-on-One series by [Deke McClelland](https://www.deke.com/)), but you should remember to clear the file content first if you'd like to download something else.

4. Run the script by `python down.py` (similar to stated previously, check your `python` alias if you have both Python 2 and 3 installed on your system). It will download specified courses to the same directory as `down.py`. Here's a sample download outcome after running the script with the sample URLs:

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

This is just a wrapper program of the wonderful [youtube-dl](http://rg3.github.io/youtube-dl/), a powerful command-line tool that allows you to conveniently download videos, audios, playlists and episodes from [many websites](http://rg3.github.io/youtube-dl/supportedsites.html). My intention of creating this script is to provide a simple cross-platform wrapper script that can quickly download multiple courses / playlists without going through the entire lengthy [documentation](https://github.com/rg3/youtube-dl/blob/master/README.md) (I got you covered there :wink:). __In fact, with minor or no tweaking, this script can also be reused to download contents from other websites such as courses on Udemy, TV episodes on YouTube or music collections on SoundCloud!__ All credits goes to the [contributors](http://rg3.github.io/youtube-dl/about) behind `youtube-dl`! :heart_eyes:
