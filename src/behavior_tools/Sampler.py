import pandas as pd
import numpy as np

class Sampler:

    def getRandom(self, tracksDf: pd.DataFrame, idCol: str, n: int) -> pd.DataFrame:
        trackIds = list(tracksDf[idCol].unique())
        trackIdsSampled = np.random.choice(trackIds, n)
        return tracksDf[tracksDf[idCol].isin(trackIdsSampled)]