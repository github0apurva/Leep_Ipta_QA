from pathlib import Path 
from IPTA_QA import logger
from box.exceptions import BoxValueError
import yaml
from ensure import ensure_annotations

@ensure_annotations
def read_yaml (path_yaml:Path) :
    """
    reads yaml file and returns it
    """
    try:
        with open(path_yaml,'r') as f:
            content = yaml.safe_load(f)
            logger.info(f"read_yaml file: {path_yaml} loaded successfully")
            return (content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
