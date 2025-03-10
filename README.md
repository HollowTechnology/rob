![rob-logo](assets/favicon/rob-logo.ico)
# rob - "robocopies other brother"
rob - youtube &amp; file downloader

## What is "rob"?
rob is a command-line tool to download files (using cURL), or YouTube Videos (using the yt-dlp Python3 library.)

## Why not use standalone tools?
rob is designed to group all theese tools together, to be used in one command.

## Usage
```
usage:
[-h] - displays this help menu
[-q <QUALITY>] - specify the quality of the video to be downloaded (to be used after the -v flag) 
[-f] - specifies that the image/video to download IS a file (.txt, .bat .sh, etc)
[-v] specifies that the image/video to download IS a video (a YouTube video)
url - has to be included, doesn't have to be specified.
```
## Example
Video Example<br>
![rob-video-example](assets/screenshots/rob-video-example.png)
![rob-video-example](assets/screenshots/rob-file-example.png)<br>
File Example

## Prerequesites & How to install

Prerequesites:<br>
1: cURL: download at `https://curl.se/download.html`<br>
2: Python 3.11 or higher: download at `https://www.python.org/downloads/`<br>
3: pip: download using `py -m ensurepip --upgrade`<br>
or<br>
download: `https://bootstrap.pypa.io/get-pip.py`<br>
then, run `py get-pip.py`<br>
4. yt-dlp: using pip, run `pip install yt-dlp`<br>

Install:<br>
1: Get the latest release from clicking [here](https://github.com/HollowTechnology/rob/releases/latest/download/rob-installer.bat)<br>or<br>
run: `curl https://github.com/HollowTechnology/rob/releases/latest/download/rob-installer.bat`<br>
2: Run `rob-installer.bat` as administrator<br><br>

Done! Reboot, then run `rob` to test the installation.
