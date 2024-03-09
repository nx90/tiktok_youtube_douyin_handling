from pytube import YouTube

def download_video(url, save_path):
    try:
        yt = YouTube(url)
        streams = yt.streams.filter(progressive=True, file_extension="mp4")
        highest_resolution_stream = streams.get_highest_resolution()
        highest_resolution_stream.download(output_path=save_path)
        print("Video downloaded successfully!")
    except Exception as e:
        print(e)

if __name__ == '__main__':
    download_video("https://www.youtube.com/watch?v=CIDLRJga2U8", "D:")