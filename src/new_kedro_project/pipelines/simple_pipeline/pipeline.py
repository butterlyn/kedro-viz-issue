"""
This is a boilerplate pipeline 'simple_pipeline'
generated using Kedro 0.19.2
"""

from kedro.pipeline import Pipeline, node, pipeline


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=lambda x: x,
                inputs="params:example_param",
                outputs="my_output",
            )
        ]
    )
