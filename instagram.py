from tkinter import *
from instaloader import *
from tkinter import messagebox

def dp():
    T = Textvalue.get()
    ig.download_profile(T, profile_pic_only=True)
    messagebox.showinfo('Downloading...', 'Requested profile picture is downloaded!')


def post():
    T = Textvalue.get()
    post = Post.from_shortcode(ig.context, T)
    ig.download_post(post, target="INSTA")
    messagebox.showinfo('Downlog...', 'Requested post is downloaded!')


def story():
    T = Textvalue.get()
    story = ""
    story = Profile.from_username(ig.context, username=T)
    ig.download_stories(userids=[story.userid], filename_target='{}/stories'.format(story.username))
    messagebox.showinfo('Downloading...', 'Requested story is downloaded!')


def highlights():
    T = Textvalue.get()
    profile = Profile.from_username(ig.context, username=T)
    for highlight in ig.get_highlights(user=profile):
        # highlight is a Highlight object
        for item in highlight.get_items():
            # item is a StoryItem object
            ig.download_storyitem(item, '{}/{}'.format(highlight.owner_username, highlight.title))
    messagebox.showinfo('Downloading...', 'Requested story is downloaded!')


def completeprofile():
    T = Textvalue.get()
    ig.download_profile(profile_name=T)
    messagebox.showinfo('Downloading...', 'Requested profile  is downloaded!')


ig = instaloader.Instaloader()

root = Tk()
root.minsize(500, 200)
root.title("Instagram Content Downloader")
f1 = Frame(root, borderwidth=10, bg="grey", relief=SUNKEN)
f1.pack(side=TOP, fill="both")
my_label = Label(f1, text="Welcome to instagram content downloader", bg="skyblue", fg="RED", font="bold")
my_label.pack()

my_label_1 = Label(text="What do you want to download", bg="yellow", fg="purple", font="italian", borderwidth=10,
                   relief=SUNKEN)
my_label_1.pack(fill="both")

frame = Frame(root, borderwidth=6, bg="grey", relief=SUNKEN)  # created another frame for buttons
frame.pack(side=LEFT, anchor="nw")

USER = '_omkar25_'
PASSWORD = "Omshravani@2002"
ig.login(USER, PASSWORD)

Text = Label(root, text="Enter the id ").pack(fill="both")
Textvalue = StringVar()
Textentry = Entry(root, textvariable=Textvalue).pack(side=TOP, fill="both")

b1 = Button(frame, fg="red", text="5.Complete Profile", command=completeprofile)
b1.pack(side=BOTTOM, fill="both")
b2 = Button(frame, fg="red", text="4.Highlights", command=highlights)
b2.pack(side=BOTTOM, fill="both")
b3 = Button(frame, fg="red", text="3.Story", command=story)
b3.pack(side=BOTTOM, fill="both")
b4 = Button(frame, fg="red", text="2.Post", command=post)
b4.pack(side=BOTTOM, fill="both")
b5 = Button(frame, fg="red", text="1.Display Picture", command=dp)
b5.pack(side=BOTTOM, fill="both")

root.mainloop()