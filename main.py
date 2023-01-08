import tkinter as tk
import json
import tkinter.filedialog

def load_json(filepath):
    with open(filepath) as file:
        data = json.load(file)
    return data

def get_following_list(following_json, followers_json):
    following_list = []
    for following in following_json["relationships_following"]:
        following_list.append(following["string_list_data"][0]["value"])

    for follower in followers_json["relationships_followers"]:
        if follower["string_list_data"][0]["value"] in following_list:
            following_list.remove(follower["string_list_data"][0]["value"])
    return following_list

def display_following_list(following_list):
    for user in following_list:
        result_listbox.insert(tk.END, user)

def show_following():
    followers_json_filepath = followers_entry.get()
    following_json_filepath = following_entry.get()
    followers_json = load_json(followers_json_filepath)
    following_json = load_json(following_json_filepath)
    following_list = get_following_list(following_json, followers_json)
    display_following_list(following_list)

def browse_file(entry):
    filepath = tk.filedialog.askopenfilename()
    entry.delete(0, tk.END)
    entry.insert(0, filepath)

root = tk.Tk()
root.title("Following List")

followers_label = tk.Label(text="Followers JSON file: ")
followers_label.pack()
followers_entry = tk.Entry(root)
followers_entry.pack()
followers_button = tk.Button(text="Browse", command=lambda: browse_file(followers_entry))
followers_button.pack()

following_label = tk.Label(text="Following JSON file:")
following_label.pack()
following_entry = tk.Entry(root)
following_entry.pack()
following_button = tk.Button(text="Browse", command=lambda: browse_file(following_entry))
following_button.pack()

show_button = tk.Button(text="Show Following", command=show_following)
show_button.pack()

result_listbox = tk.Listbox(root)
result_listbox.pack()

scrollbar = tk.Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# attach listbox to scrollbar
result_listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=result_listbox.yview)

root.mainloop()
