import tkinter as tk
from tkinter import filedialog
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

def select_file():
    file_name = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_name:
        file_entry.delete(0, tk.END)
        file_entry.insert(0, file_name)

def process_file():
    file_name = file_entry.get()
    try:
        with open(file_name, 'r') as file:
            video_links = [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        result_label.config(text="File not found.")
        return

    try:
        total_duration = calculate_total_duration(video_links)
        result_label.config(text=f"Total video time: {total_duration}")
    except Exception as e:
        result_label.config(text=f"Error: {e}")

# Create GUI
root = tk.Tk()
root.title("YoutubeDurationCounter")

file_label = tk.Label(root, text="Select txt file:")
file_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")

file_entry = tk.Entry(root, width=50)
file_entry.grid(row=0, column=1, padx=5, pady=5)

select_button = tk.Button(root, text="Select", command=select_file)
select_button.grid(row=0, column=2, padx=5, pady=5)

process_button = tk.Button(root, text="Process", command=process_file)
process_button.grid(row=1, column=1, padx=5, pady=5)

result_label = tk.Label(root, text="")
result_label.grid(row=2, column=1, padx=5, pady=5)

root.mainloop()
