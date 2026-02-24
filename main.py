#import pygame
import keyboard
import time

points = 0
upgrades = {"cps": 1, "click_power": 1}

def on_release(event):
    global points, upgrades
    if event.name == "space":
        points += upgrades["cps"]


def main():
    global points, upgrades
    keyboard.on_release(on_release)
    while True:
        print(f"\033[2K\033[1APoints: {points}\n\033[2KUpgrades: {upgrades}", end="\r", flush=True)
        time.sleep(0.1)
if __name__ == "__main__":
    main()