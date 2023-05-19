import pandas as pd
from typing import *
# import os
# import matplotlib.pyplot as plt
import numpy as np

class TrajectoryADECalculator:
    
    
    def getAADE(self, tracksDf: pd.DataFrame, idCol, xCol, yCol, trackIds=None):
        total_ade = 0
        
        if trackIds is None:
            trackIds = tracksDf[idCol].unique()


        # print(f"Track Ids length: {len(trackIds)}")
        for trackId in trackIds:
            trackDf = tracksDf[tracksDf[idCol] == trackId]
            ade = self.getADE(trackDf=trackDf, idCol=idCol, xCol=xCol, yCol=yCol)
            total_ade += ade 
            
            
        AADE = total_ade / len(trackIds)
        # print(f"AADE : {AADE}")
        return AADE

    
    def getADE(self, trackDf: pd.DataFrame, idCol, xCol, yCol, trackIds=None):

        diff = 0
        # plt.plot(trackDf[xCol], trackDf[yCol])
        
        # plot direction
        lastRow = trackDf.tail(1)
        endPoint = (lastRow[xCol] , lastRow[yCol])
        # print(f"end point {endPoint[0].values[0]}")
        firstRow = trackDf.head(1)
        startPoint = (firstRow[xCol] , firstRow[yCol])
        # print(f"start point {startPoint[0].values[0]}")
        # print(startPoint[0].values[0], startPoint[1].values[0])
        for col in trackDf[xCol]:
            diff += abs(col - startPoint[0].values[0])   
        # diff = abs(endPoint[0].values[0] - startPoint[0].values[0])
        # print(f"diff {diff}")
        return diff / len(trackDf)
    
    def getADEs(self, tracksDf: pd.DataFrame, idCol, xCol, yCol) -> List[float]:
        trackIds = tracksDf[idCol].unique()

        adeList = []
        for trackId in trackIds:
            trackDf = tracksDf[tracksDf[idCol] == trackId]
            adeList.append(self.getADE(trackDf=trackDf, idCol=idCol, xCol=xCol, yCol=yCol))
        
        return adeList
        


