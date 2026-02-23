import pygame, keyboard

points = 0
upgrades = {"cps": 1, "click_power": 1}

def main():
    global points, upgrades
    while True:
        print(f"Points: {points}", end="\r")
        if keyboard.is_pressed("space"):
            points += upgrades["cps"]