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

# Function to generate a project idea by user input
def generate_project_idea(theme, project_type):
    unique_feature = random.choice(unique_features)
    return f"Build a {theme} {project_type} {unique_feature}"

# Input part
if __name__ == "__main__":
    print("Welcome to the Interactive Hackathon Project Idea Generator!\n")
    print("Please enter your preferences to generate a project idea.\n")
    
    theme = input("Enter a theme or technology (e.g., Blockchain, AI and Machine Learning, IoT): ").strip()
    project_type = input("Enter a project type (e.g., App, Platform, Game): ").strip()
    
    # Generate and print project idea 
    idea = generate_project_idea(theme, project_type)
    print("\nHere's your randomly generated project idea:")
    print(idea)
