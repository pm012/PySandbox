# PySandbox

Create virtual environment

```bash
python -msou venv env
```

Activate virtual environment

```bash
source env/bin/activate
```

Install all libraries from requirements.txt

```bash
pip install -r /path/to/requirements.txt
```

to create file in the same directory where script is located do the following in the script:

```python
import os
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "test.txt")
```

Note!: Don't forget to replace "test.txt" to your file or variable setting the filename
and use file_path to create file

to import the file from the directory above before import:

```python
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
```
