# Notebooks

BoomX plays nicely with Jupyter notebooks.

## Install the jupyterlab Python package

First, add `jupyterlab` to the `python_packages` array in your [`boomx.yaml`](yaml.md) file:

```yaml
build:
  python_packages:
    - "jupyterlab==3.3.4"
```


## Run a notebook

BoomX can run notebooks in the environment you've defined in `boomx.yaml` with the following command:

```sh
boomx run -p 8888 jupyter notebook --allow-root --ip=0.0.0.0
```

## Use notebook code in your predictor

You can also import a notebook into your BoomX [Predictor](python.md) file.

First, export your notebook to a Python file:

```sh
jupyter nbconvert --to script my_notebook.ipynb # creates my_notebook.py
```

Then import the exported Python script into your `predict.py` file. Any functions or variables defined in your notebook will be available to your predictor:

```python
from boomx import BasePredictor, Input

import my_notebook

class Predictor(BasePredictor):
    def predict(self, prompt: str = Input(description="string prompt")) -> str:
      output = my_notebook.do_stuff(prompt)
      return output
```
