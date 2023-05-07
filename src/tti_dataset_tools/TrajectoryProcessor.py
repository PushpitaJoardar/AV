import numpy as np
import pandas as pd
from .ColMapper import ColMapper

class TrajectoryProcessor:

    def __init__(self,
            colMapper: ColMapper
        ):
        self.idCol = colMapper.idCol
        self.xCol = colMapper.xCol
        self.yCol = colMapper.yCol
        self.xVelCol = colMapper.xVelCol
        self.yVelCol = colMapper.yVelCol
        self.xAccCol = colMapper.xAccCol
        self.yAccCol = colMapper.yAccCol
        self.speedCol = colMapper.speedCol
        self.accelerationCol = colMapper.accelerationCol
        
        self.displacementXCol = colMapper.displacementXCol
        self.displacementYCol = colMapper.displacementYCol
        self.localXCol = colMapper.localXCol
        self.localYCol = colMapper.localYCol
