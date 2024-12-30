import pygame

# Initialize Pygame
pygame.init()

# Set screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Set background color (white)
background_color = (255, 255, 255)

# Set the window title
pygame.display.set_caption("Pygame Text Display")

# Define font and text properties
font = pygame.font.SysFont("Arial", 48)  # You can change "Arial" to any other font available on your system
text = "Hello, Pygame!"
text_color = (0, 0, 0)  # Black color for text

# Create the text surface
text_surface = font.render(text, True, text_color)

# Get the text's rectangle and position it at the center of the screen
text_rect = text_surface.get_rect(center=(screen_width // 2, screen_height // 2))

# Main loop
running = True
while running:
    # Fill the screen with the background color
    screen.fill(background_color)

    # Display the text
    screen.blit(text_surface, text_rect)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
