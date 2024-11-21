from tkinter import *
from PIL import Image, ImageTk  # Make sure to install Pillow (PIL)

# Function to toggle image and increase the counter
def change_image(event):
    global img_state, counter
    # Toggle image state (open/closed)
    if img_state == 'closed':
        label.config(image=open_img)  # Change to open mouth image
        img_state = 'open'
    else:
        label.config(image=closed_img)  # Change to closed mouth image
        img_state = 'closed'
    
    # Left click to increase counter
    if event.num == 1:  # Left-click (button 1)
        counter += 1  # Increase counter
        counter_label.config(text=f"Total Clicks: {counter}")  # Update counter label

# Create the main window
window = Tk()
window.geometry("400x400")  # Adjust window size

# Load the images (replace with your own image file paths)
closed_image = Image.open("C:/Users/dipsh/OneDrive/Desktop/Realtime/gallery/AAAAMRBEAN.jpg")
open_image = Image.open(r"C:\Users\dipsh\OneDrive\Desktop\Realtime\gallery\mr-bean-mouth-opening-and-closing.png")

# Resize images if needed
closed_img = ImageTk.PhotoImage(closed_image.resize((200, 200)))  # Resize as needed
open_img = ImageTk.PhotoImage(open_image.resize((200, 200)))  # Resize as needed

# Set initial image state
img_state = 'closed'
counter = 0  # Initialize counter

# Create the label with the initial image
label = Label(window, image=closed_img)
label.pack()

# Create a label to show the total number of clicks
counter_label = Label(window, text="Total Clicks: 0", font="Arial 16")
counter_label.pack()

# Create the button to change the image and count clicks
button = Button(window, text="Click to Change", font="Arial 16")
button.pack()

# Bind left-click (Button-1) to the change_image function
button.bind("<Button-1>", change_image)

# Start the Tkinter event loop
window.mainloop()
