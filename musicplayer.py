import tkinter as tk
from tkinter.filedialog import askopenfilename
from pygame import mixer
import os

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")
        self.root.geometry("300x200")

        mixer.init()

        self.track = tk.StringVar()
        self.status = tk.StringVar()

    
        self.top_frame = tk.Frame(self.root)
        self.top_frame.pack(pady=20)

        self.track_label = tk.Label(self.top_frame, textvariable=self.track, font=("Arial", 12))
        self.track_label.pack()

        self.status_label = tk.Label(self.top_frame, textvariable=self.status, font=("Arial", 12))
        self.status_label.pack()

        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(pady=10)

        self.play_button = tk.Button(self.button_frame, text="Play", command=self.play_music)
        self.play_button.pack(side=tk.LEFT, padx=10)

        self.pause_button = tk.Button(self.button_frame, text="Pause", command=self.pause_music)
        self.pause_button.pack(side=tk.LEFT, padx=10)

        self.stop_button = tk.Button(self.button_frame, text="Stop", command=self.stop_music)
        self.stop_button.pack(side=tk.LEFT, padx=10)

        self.open_button = tk.Button(self.button_frame, text="Open", command=self.open_music)
        self.open_button.pack(side=tk.LEFT, padx=10)

    def play_music(self):
        self.status.set("Playing")
        filename = self.track.get()
        mixer.music.load(filename)
        mixer.music.play()

    def pause_music(self):
        self.status.set("Paused")
        mixer.music.pause()

    def stop_music(self):
        self.status.set("Stopped")
        mixer.music.stop()

    def open_music(self):
        print("Open music method called")
        path = askopenfilename(filetypes=[("MP3 files", "*.mp3")])
        self.track.set(path)

if __name__ == "__main__":
    root = tk.Tk()
    music_player = MusicPlayer(root)
    root.mainloop()