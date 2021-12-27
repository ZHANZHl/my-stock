import torch
import torch.nn as nn


class StockModel(nn.Module):
    def __init__(self):
        super(StockModel, self).__init__()
        self.net1 = torch.nn.Sequential(
            nn.Linear()
        )
