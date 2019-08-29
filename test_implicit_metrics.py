import hinpy


import pandas as pd
import numpy as np
pd.options.mode.chained_assignment = "raise"
from random import choice
from hinpy.rs.implicit_utility import *

likes_func = lambda x: True if x>2.5 else False

hin = hinpy.classes.HIN(name='m100k',filename='datasets/movielens100k_hin.csv',inverse_relations=True)
#hin = hinpy.classes.HIN(name='example',filename='datasets/example1.csv',inverse_relations=True)
hin.CreateLinkGroupFromLinkGroup(relation_name='rates',new_relation_name='likes',condition_method=likes_func)
hin.CreateInverseLinkGroup(existing_relation_name='likes',new_relation_name='inverse_likes')

params = {'method':'CB', 'topK_predictions': 4, 'seen_relation':'rates', 
#          'paths':[['likes','inverse_likes','likes'],
#                   ['likes','is_of_type','inverse_is_of_type'],
#                   ['has_occupation','inverse_has_occupation','likes'],
#                   ['has_age','inverse_has_age','likes'],
#                   ['likes','was_released','inverse_was_released'],
#                   ['is_located','inverse_is_located','likes']], 
#          'paths_weights':[0.3,0.3,0.03,0.3,0.03,0.04],
          'paths':[['likes','inverse_likes','likes']], 
          'paths_weights':[1],
          'implicit_metrics':True,
          'implicit_metrics_N':[5,10,15,20,25,30,35,40,45,50],
#          'implicit_metrics_N':[5],
          'implicit_metrics_fraction':0.1,
          'test_control':0}


hin.CreateLinkGroupFromRS(relation_name='likes',new_relation_name='CB-recos',parameters=params)
hin.GetLinkGroup('CB-recos').info
