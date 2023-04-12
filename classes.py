class Plane:
    def __init__(self, velocityMin, velocityMax, height, time):
        self.velocityMin = velocityMin
        self.velocityMax = velocityMax
        self.height = height
        self.time = time


class Camera:
    def __init__(self, sizeOfMatrix, sizeOfPixel, spectralCanals, focalLength, workCycle, weigth):
        self.sizeOfMatrix = sizeOfMatrix
        self.sizeOfPixel = sizeOfPixel
        self.spectralCanals = spectralCanals
        self.focalLength = focalLength
        self.workCycle = workCycle
        self.weigth = weigth