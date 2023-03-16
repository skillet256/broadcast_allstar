# broadcast_allstar
This enables the broadcast of audio files over an AllStar enabled repeater. Useful in particular for broadcasting Amateur Radio Newsline on a regular basis.
Broadcas Allstar is designed by KA5D. Its used is intended primarily for amateur radio.

Overview of component scripts:

arnewsline:
This bash script arnewsline is the master script to broadcast arnewsline on allstar.
First, it will call get-arnewsline.py to get the arnewsline audio url and save it in a file in the script directory
It can also get the ARRL news url and save it in a file as well.
Then, it runs the broadcast_allstar script and generates a log.
Optionally, this can be modified to broadcast ARRL news instead. This is disabled by default.
Intended to be run as a cron job at broadcast time, as root on the ASL node you want, using this command in root's crontab:

#----sample crontab entry start----
#KTD 12/11/20 broadcast Amateur Radio Newsline audio every Friday evening
0  18   *   *   5    . /root/.profile && /root/bin/arnewsline
#----sample crontab entry end----

get-arnewsline.py:
Scrape the Amateur Radio Newsline site for the latest audio broadcast, and download it
Destination file to be read and written is passed as the first (and only) argument with full path.
Amateur Radio newsline usually publishes new content every Friday morning.

get-arrlnews.py:
Scrape the ARRL NEWS site for the latest audio broadcast, and download it
Destination file to be read and written is passed as the first (and only) argument with full path.
Not sure when or how often this podcast is published.

broadcast_allstar:
Converts mp3 or wav URI or files to ulaw for AllStar.
This script can be run either interactively, or via crontab

Designed to accept a URI as input, or this file as input argument #1 (but could take any file, or multiples!)
~/bin/arnewsline_audio.mp3

Dependencies (linux packages required):
lame sox ffmpeg asterisk wget

Interactive CLI Usage: broadcast_allstar input_audio_file1 [input_audio_file2...]

Example Usage: broadcast_allstar [options: -a </path/to/asterisk>
                                           -c <chunksize in secs>
                                           -n <allstar node number>
                                           -r <volume in DB reduction>] input_audio_file1 [input_audio_file2...]
Use either full path name or full URI for "input_audio_file<x>"

Usage guide:
1. use full path for all input files. Input files will not be altered or deleted.
2. output files will reside in the same path as input with the .ulaw extension, and will be deleted after use                                       
3. This will also take one argument in the form of a URI that starts with 'http' and ends with 'mp3' or 'wav' and it will wget the file, then process it.
4. If you want to play audio files, then have them deleted afterward, put them in the /tmp directory. If not, put them somewhere else.

