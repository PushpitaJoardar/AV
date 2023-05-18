import pandas as pd
from typing import *
# import os
# import matplotlib.pyplot as plt
import numpy as np

class TrajectoryADECalculator:
    
    def calculate(self, df: pd.DataFrame, idCol, xCol, yCol, trackIds=None):
        
        total_diff = 0
        
        if trackIds is None:
            trackIds = df[idCol].unique()


        for trackId in trackIds:
            diff = 0
            trackDf = df[df[idCol] == trackId]
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
            # plt.plot(endPoint[0], endPoint[1], marker='x')
            # diff = abs(endPoint[0].values[0] - startPoint[0].values[0])
            # print(f"diff {diff}")
            total_diff += (diff / len(trackDf[xCol]))
            
            
        avg_displacement_error = total_diff / len(trackIds)
        print(f"ADE : {avg_displacement_error}")
        
        # # Sampling 
        # total_diff = 0
        # trackIdsSampled = trackIds[::10]
        # for trackId in trackIdsSampled:
        #     diff = 0
        #     trackDf = df[df[idCol] == trackId]
        #     # plt.plot(trackDf[xCol], trackDf[yCol])
        #     firstRow = trackDf.head(1)
        #     startPoint = (firstRow[xCol] , firstRow[yCol])
        #     for col in trackDf[xCol]:
        #         diff += abs(col - startPoint[0].values[0])   
        #     # plt.plot(endPoint[0], endPoint[1], marker='x')
        #     total_diff += (diff / len(trackDf[xCol]))
            
        # sample_avg_displacement_error = total_diff / len(trackIdsSampled)
        # print(f"ADE Sampled: {sample_avg_displacement_error}")