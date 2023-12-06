from pytube import YouTube

def get_video_duration(youtube_url):
    yt = YouTube(youtube_url)
    duration_seconds = yt.length
    return duration_seconds

def format_duration(seconds):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return "{:02}:{:02}:{:02}".format(int(hours), int(minutes), int(seconds))

def calculate_total_duration(video_links):
    total_seconds = 0

    for link in video_links:
        try:
            video_duration_seconds = get_video_duration(link)
            total_seconds += video_duration_seconds
        except Exception as e:
            print(f"Hata: {e} ({link})")

    formatted_total_duration = format_duration(total_seconds)
    return formatted_total_duration

def main():
    video_links = []
    while True:
        link = input("YouTube video link (press q for exit aga): ")
        if link.lower() == 'q':
            break
        video_links.append(link)

    try:
        total_duration = calculate_total_duration(video_links)
        print(f"\nToplam video süresi: {total_duration}")
    except Exception as e:
        print(f"Hata: {e}")

if __name__ == "__main__":
    main()
