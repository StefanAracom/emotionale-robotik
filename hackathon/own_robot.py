from robot import Robot
import cv2 as cv
import pygame
import math

from cli import print_emotions

import os


class OwnRobot(Robot):
    count = 0

    WHITE =     (255, 255, 255)
    BLACK =     (0, 0, 0)
    BLUE =      (  0,   0, 255)
    GREEN =     (  0, 255,   0)
    RED =       (255,   0,   0)
    YELLOW =    (255, 255,   0)
    BROWN =     (165,  42,  42)
    (width, height) = (400, 400)

    weights = {
        "Happiness": 8,
        "Neutral": 7,
        "Surprise": 6,
        "Contempt": 5,
        "Sadness": 4,
        "Anger": 2,
        "Disgust": 3,
        "Fear": 1
    }

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Hackerkiste 2023")
    screen.fill(WHITE)
    pygame.display.update()

    def convertToWeight(self, emotion):
        return self.weights[emotion]

    def showHappiness(self):
        pygame.draw.circle(self.screen, self.YELLOW, (200, 200), 150)
        pygame.draw.circle(self.screen, self.BROWN, (150, 150), 20)
        pygame.draw.circle(self.screen, self.BROWN, (250, 150), 20)
        pygame.draw.arc(self.screen, self.BROWN, [100, 100, 200, 200], math.pi, math.pi/30, 10)

    def showSadness(self):
        pygame.draw.circle(self.screen, self.YELLOW, (200, 200), 150)
        pygame.draw.circle(self.screen, self.BROWN, (150, 150), 20)
        pygame.draw.circle(self.screen, self.BROWN, (250, 150), 20)
        pygame.draw.arc(self.screen, self.BROWN, [100, 200, 200, 200], math.pi/30, math.pi, 10)

    def showContempt(self):
        pygame.draw.circle(self.screen, self.YELLOW, (200, 200), 150)
        pygame.draw.circle(self.screen, self.BROWN, (150, 150), 20)
        pygame.draw.circle(self.screen, self.BROWN, (250, 150), 20)
        pygame.draw.line(self.screen, self.BROWN, (100, 250), (300, 220), 20)

    def showAnger(self):
        pygame.draw.circle(self.screen, self.YELLOW, (200, 200), 150)
        pygame.draw.circle(self.screen, self.BROWN, (150, 150), 20)
        pygame.draw.circle(self.screen, self.BROWN, (250, 150), 20)
        pygame.draw.line(self.screen, self.BROWN, (130, 100), (150, 120), 20)
        pygame.draw.line(self.screen, self.BROWN, (240, 120), (260, 100), 20)
        pygame.draw.arc(self.screen, self.BROWN, [100, 200, 200, 200], math.pi/30, math.pi, 10)

    def showSurprise(self):
        pygame.draw.circle(self.screen, self.YELLOW, (200, 200), 150)
        pygame.draw.circle(self.screen, self.BROWN, (150, 150), 20)
        pygame.draw.circle(self.screen, self.BROWN, (250, 150), 20)
        pygame.draw.circle(self.screen, self.BROWN, (200, 250), 50)
        pygame.draw.circle(self.screen, self.BROWN, (150, 150), 5)
        pygame.draw.circle(self.screen, self.BROWN, (250, 150), 5)
        pygame.draw.arc(self.screen, self.BROWN, [130, 80, 30, 20], math.pi/30, math.pi, 10)
        pygame.draw.arc(self.screen, self.BROWN, [240, 80, 30, 20], math.pi/30, math.pi, 10)

    def showDisgusted(self):
        pygame.draw.circle(self.screen, self.GREEN, (200, 200), 150)
        # right eye
        pygame.draw.line(self.screen, self.BROWN, (220, 160), (270, 120), 5)
        pygame.draw.line(self.screen, self.BROWN, (220, 160), (270, 150), 5)
        # left eye
        pygame.draw.line(self.screen, self.BROWN, (120, 120), (170, 160), 5)
        pygame.draw.line(self.screen, self.BROWN, (120, 150), (170, 160), 5)
        # mouth
        pygame.draw.ellipse(self.screen, self.BLACK, [130, 220, 130, 70])
        # tongue
        pygame.draw.ellipse(self.screen, self.RED, [160, 240, 70, 130])

    def showFear(self):
        pygame.draw.circle(self.screen, self.YELLOW, (200, 200), 150)
        pygame.draw.circle(self.screen, self.BROWN, (150, 150), 20)
        pygame.draw.circle(self.screen, self.BROWN, (250, 150), 20)
        pygame.draw.circle(self.screen, (51, 153, 255), (200, 200), 150,  draw_top_right=True, draw_top_left=True)
        pygame.draw.circle(self.screen, self.BROWN, (200, 270), 50)
        pygame.draw.circle(self.screen, self.YELLOW, (200, 300), 50)

        pygame.draw.circle(self.screen, self.BROWN, (150, 150), 5)
        pygame.draw.circle(self.screen, self.BROWN, (250, 150), 5)
        pygame.draw.arc(self.screen, self.BROWN, [130, 80, 30, 20], math.pi/30, math.pi, 10)
        pygame.draw.arc(self.screen, self.BROWN, [240, 80, 30, 20], math.pi/30, math.pi, 10)


    def showNeutral(self):
        pygame.draw.circle(self.screen, self.YELLOW, (200, 200), 150)
        pygame.draw.circle(self.screen, self.BROWN, (150, 150), 20)
        pygame.draw.circle(self.screen, self.BROWN, (250, 150), 20)
        pygame.draw.line(self.screen, self.BROWN, (100, 250), (300, 250), 20)

    def update(self, image, emotions):
        self.count += 1
        if self.count > 10:
            self.count = 1
        print_emotions(emotions)
        #cv.imwrite(os.sep.join(["img", f"ownRobot{self.count}.png"]), image)

        sumOfWeights = sum(list(map(self.convertToWeight, emotions)))
        score = round(sumOfWeights / len(emotions)) if len(emotions) > 0 else sumOfWeights

        print("SCORE: ", score)

        self.screen.fill(self.WHITE)

        if ("Happiness" in emotions):
            self.showHappiness()
        elif ("Sadness" in emotions):
            self.showSadness()
        elif ("Contempt" in emotions):
            self.showContempt()
        elif ("Anger" in emotions):
            self.showAnger()
        elif ("Surprise" in emotions):
            self.showSurprise()
        elif ("Disgust" in emotions):
            self.showDisgusted()
        elif ("Fear" in emotions):
            self.showFear()
        else:
            self.showNeutral()

        pygame.display.update()
