#!/usr/bin/env python3
import pygame
import sys

# Initialize Pygame
pygame.init()
# Get screen dimensions
screen_info = pygame.display.Info()
screen_width = screen_info.current_w
screen_height = screen_info.current_h

# Screen dimensions
#screen_width = 800
#screen_height = 600

# Colors
red = (255, 0, 0)
black = (0, 0, 0)
white = (255, 255, 255)

# Set up the display
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Wrap It Up")

# Font settings
#font_size = 100
#font = pygame.font.SysFont(None, font_size)
# Font settings - dynamically adjust font size based on screen height
font_size = screen_height // 3  # Adjust the division factor as needed
font = pygame.font.SysFont(None, font_size)
# Text rendering
text = font.render("WRAP IT UP", True, white)
text_rect = text.get_rect(center=(screen_width / 2, screen_height / 2))

# Flashing settings
flash_duration = 500  # duration of one flash in milliseconds
flash_timer = pygame.time.get_ticks()
flash_state = True  # True for red, False for black

# Load and play sound
pygame.mixer.init()
#sound = pygame.mixer.Sound("Red-Alert.wav")
sound = pygame.mixer.Sound("Tornado.wav")
sound.play(loops=-1)  # Play sound on loop

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Flashing logic
    current_time = pygame.time.get_ticks()
    if (current_time - flash_timer) > flash_duration:
        flash_state = not flash_state
        flash_timer = current_time

    # Set background color based on flash state
    if flash_state:
        screen.fill(red)
    else:
        screen.fill(black)

    # Draw the text
    screen.blit(text, text_rect)

    # Update the display
    pygame.display.flip()

# Clean up Pygame
pygame.quit()
sys.exit()
