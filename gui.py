import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from logic import convert_playlist  


def run_conversion():
    sp_id = spotify_id_entry.get()
    yt_name = yt_name_entry.get()

    if not sp_id or not yt_name:
        log("please fill in both fields.")
        return

    log("fetching Spotify tracks...")
    try:
        yt_id = convert_playlist(sp_id, yt_name)
        log(f"conversion complete!\nYouTube playlist ID: {yt_id}")
    except Exception as e:
        log(f"error: {str(e)}")


def log(text):
    output_box.insert(tk.END, text + "\n")
    output_box.see(tk.END)


# GUI window
root = tk.Tk()
root.title("Spotify → YouTube Playlist Converter")
root.geometry("600x400")
root.resizable(False, False)

main_frame = tk.Frame(root, bg="#FFE7EE", padx=20, pady=20)
main_frame.pack(fill="both", expand=True)


#fonts
TITLE_FONT = ("Arial", 16, "bold")
LABEL_FONT = ("Arial", 11)
BUTTON_FONT = ("Arial", 11, "bold")

# labels + inputs
tk.Label(
    main_frame,
    text="Spotify playlist URL",
    font=LABEL_FONT,
    bg="#FFE7EE"
).pack(anchor="n", pady=(0, 4))

spotify_id_entry = tk.Entry(main_frame, width=50)
spotify_id_entry.pack(pady=(0, 12))

tk.Label(
    main_frame,
    text="YouTube playlist name",
    font=LABEL_FONT,
    bg="#FFE7EE"
).pack(anchor="n", pady=(0, 4))

yt_name_entry = tk.Entry(main_frame, width=50)
yt_name_entry.pack(pady=(0, 15))


# convert button
convert_button = tk.Button(
    main_frame,
    text="convert playlist",
    font=BUTTON_FONT,
    bg="#FEA4C1",       # Spotify green
    fg="white",
    activebackground="#FD90B2",
    relief="flat",
    padx=12,
    pady=6,
    command=run_conversion
)
convert_button.pack(pady=15)


# output log box
output_box = scrolledtext.ScrolledText(
    main_frame,
    width=55,
    height=12,
    font=("Consolas", 9),
    bg="#ffffff",
    fg="#333333",
    relief="flat",
    padx=10,
    pady=10
)
output_box.pack(pady=10)


root.mainloop()
