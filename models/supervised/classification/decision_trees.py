from typing import Optional
import tensorflow as tf

from tensorflow_decision_forests.keras import core_inference
from tensorflow_decision_forests.keras import core


print(tf.__version__)


class Decision_tree:

    def __init__(self, task: core_inference.Task.CLASSIFICATION,
                 features: Optional[list[core.FeatureUsage]] = None):


hyperparameters = {"task": core_inference.Task.CLASSIFICATION,
                   "features": core.FeatureUsage,
                   "exclude_non_specified_featureside": False,
                   ""}
#              exclude_non_specified_features: ,
#               preprocessing,
#              postprocessing,
#              training_preprocessing,
#              ranking_group, uplift_treatment,
#              temp_directory,
#              verbose,
#              hyperparameter_template,
#              advanced_arguments,
#              num_threads,
#              name,
#              try_resume_training,
#              check_dataset,
#              tuner,
#              discretize_numerical_features,
#              multitask,
#              allow_na_conditions,
#              categorical_algorithms,
#              categorical_set_split_greedy_sampling,
#              categorical_set_split_max_nums_items,
#              categorical_set_split_min_item_frequency,
#              growing_strategy,
#              honest,
#              honest_fixed_separation,
#             honest_ratio_leaf_examples}
