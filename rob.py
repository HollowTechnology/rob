import yt_dlp
import argparse
import os

parser = argparse.ArgumentParser(description="rob - file and YouTube downloader")
parser.add_argument("url", help="File URL or YouTube video URL")
parser.add_argument("-q", "--quality", help="Video quality (e.g., 720, 480, best, worst)(to be used with -v)", default="best")
parser.add_argument("-f", "--file", help="Download a normal file instead of a video", action="store_true")
parser.add_argument("-v", "--video", help="Download a Youtube video", action="store_true")

args = parser.parse_args()

if args.file:
    # Use curl to download the file
    output_filename = args.url.split("/")[-1]  # Extract filename from URL
    os.system(f'curl -o "{output_filename}" "{args.url}"')
    print(f"File downloaded as: {output_filename}")
elif args.video:
    # Define yt-dlp options
    if args.quality.isdigit():  # If user provides a number like 720 or 480
        format_string = f"bestvideo[height<={args.quality}]+bestaudio/best"
    else:  # If user provides "best" or "worst"
        format_string = args.quality

    ydl_opts = {
        "format": format_string
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([args.url])
else:
    print("Please provide a flag, -v for video, or -f for a normal file.")