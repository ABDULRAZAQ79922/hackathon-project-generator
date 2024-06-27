import tkinter as tk
from tkinter import messagebox
import random

# List of possible unique features or innovations
unique_features = [
    "using blockchain for secure voting",
    "employing AI for real-time language translation",
    "integrating IoT sensors for environmental monitoring",
    "creating AR experiences for historical education",
    "developing VR simulations for healthcare training",
    "building a wellness app with personalized AI coaching",
    "designing an education platform with adaptive learning",
    "implementing sustainability analytics for businesses",
    "enhancing cybersecurity through machine learning algorithms",
    "innovating social media integration with VR",
    "revolutionizing e-commerce with AI-driven recommendation systems",
    "creating a mobile app for data visualization",
    "building smart city solutions with IoT devices",
    "developing autonomous robots for warehouse management"
]

# Function to generate a project idea based on user input
def generate_project_idea(theme, project_type):
    unique_feature = random.choice(unique_features)
    return f"Build a {theme} {project_type} {unique_feature}"

# Function to handle button click event
def generate_idea():
    theme = theme_entry.get().strip()
    project_type = project_type_entry.get().strip()
    
    if theme == "" or project_type == "":
        messagebox.showerror("Error", "Please enter both a theme and a project type.")
    else:
        idea = generate_project_idea(theme, project_type)
        idea_text.set(idea)

# Create the main window
root = tk.Tk()
root.title("Hackathon Project Idea Generator")

# Set window size
root.geometry("800x400") 

# Create labels and entry fields
tk.Label(root, text="Theme or Technology:").pack()
theme_entry = tk.Entry(root)
theme_entry.pack()

tk.Label(root, text="Project Type:").pack()
project_type_entry = tk.Entry(root)
project_type_entry.pack()

tk.Button(root, text="Generate Idea", command=generate_idea).pack()

# Label to display generated idea
idea_text = tk.StringVar()
idea_text.set("")
tk.Label(root, text="Generated Idea:", font=("Arial", 18)).pack()
tk.Label(root, textvariable=idea_text, wraplength=880, font=("Arial", 18)).pack()


root.mainloop()
