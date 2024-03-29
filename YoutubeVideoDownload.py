from tkinter import *
from tkinter import messagebox
from pytube import YouTube

def download_youtube():
    choice = download_choice.get()
    video_url = url_entry.get()
    option = path_choice.get()

    if not video_url:
        messagebox.showerror("Error", "Please enter a YouTube URL.")
        return

    if option == 1:
        download_path = "O:\\"
    elif option == 2:
        download_path = "C:\\"
    elif option == 3:
        download_path = "E:\\"
    else:
        messagebox.showerror("Error", "Invalid path option selected.")
        return

    yt = YouTube(video_url)

    if choice == 1:
        audio_stream = yt.streams.get_audio_only()
        audio_stream.download(download_path)
        messagebox.showinfo("Success", "Audio downloaded successfully!")
    elif choice == 2:
        video_stream = yt.streams.get_highest_resolution()
        video_stream.download(download_path)
        messagebox.showinfo("Success", "Video and Audio downloaded successfully!")

# GUI setup
root = Tk()
root.title("YouTube Downloader")
root.configure(bg="#f0f0f0")  # Set background color

# Labels
Label(root, text="YouTube URL:", bg="#f0f0f0").grid(row=0, column=0, padx=5, pady=5)
Label(root, text="Download Choice:", bg="#f0f0f0").grid(row=1, column=0, padx=5, pady=5)
Label(root, text="Download Path:", bg="#f0f0f0").grid(row=2, column=0, padx=5, pady=5)

# Entry widgets
url_entry = Entry(root, width=50)
url_entry.grid(row=0, column=1, columnspan=2, padx=5, pady=5)

download_choice = IntVar(root)
Radiobutton(root, text="Audio", variable=download_choice, value=1, bg="#f0f0f0").grid(row=1, column=1, padx=5, pady=5)
Radiobutton(root, text="Audio & Video", variable=download_choice, value=2, bg="#f0f0f0").grid(row=1, column=2, padx=5, pady=5)

path_choice = IntVar(root)
Radiobutton(root, text="O-drive", variable=path_choice, value=1, bg="#f0f0f0").grid(row=2, column=1, padx=5, pady=5)
Radiobutton(root, text="C-drive", variable=path_choice, value=2, bg="#f0f0f0").grid(row=2, column=2, padx=5, pady=5)
Radiobutton(root, text="E-drive", variable=path_choice, value=3, bg="#f0f0f0").grid(row=2, column=3, padx=5, pady=5)

# Download button
Button(root, text="Download", command=download_youtube, bg="#007bff", fg="white").grid(row=3, column=1, columnspan=2, padx=5, pady=5)

root.mainloop()
