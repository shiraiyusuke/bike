# -*- coding: utf-8 -*-
import numpy as np
import scipy as sc
import pandas as pd
import os
import sys
from api_util import BaseApi

class FfLeftKeyPointDetection(BaseApi):

    def __init__(self, architect_file, weight_file, ):