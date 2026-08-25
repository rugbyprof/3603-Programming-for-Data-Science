# 📚 Glossary: 06 - Foundations

**Cell**  
A block in a Jupyter notebook that can contain **code** or **Markdown**. Code cells run Python; Markdown cells render formatted text.

**Command Mode**  
Notebook mode where you operate on whole cells (add, delete, move, change type). Enter with `Esc`.

**Edit Mode**  
Notebook mode where you type inside a cell. Enter with `Enter`.

**Kernel**  
The "engine" that runs code inside Jupyter. For Python, this is IPython.

**Magic Command**  
Special IPython commands starting with `%` (line magic) or `%%` (cell magic) that provide shortcuts, e.g. `%time`, `%pwd`, `%%writefile`.

**DataFrame**  
A 2D table of data provided by Pandas. Has rows, columns, and labels.

**Docstring**  
The built-in documentation attached to a Python object, viewable with `?`, `??`, or `help()`.

**Export**  
Saving a notebook as another format (`.py`, `.html`, `.pdf`) via *File → Save and Export Notebook As…* or `%save`.

**File Path**  
The location of a file in your system. Looks different across platforms — e.g. `C:\Users\me\data.csv` on Windows vs. `/Users/me/data.csv` on Mac. Prefer relative paths (`data/file.csv`) in your notebooks so they work on anyone's machine, including yours next semester.

**JSON (JavaScript Object Notation)**  
A structured file format using key–value pairs. Often used for configs and web APIs.

**LaTeX**  
A math typesetting language. Used in notebooks for equations like $E = mc^2$.

**Markdown**  
A lightweight markup language for text formatting in notebooks: `**bold**`, `*italic*`, `# heading`.

**NumPy**  
A Python library for fast array operations. Supports vectorized math like `arr ** 2`. You'll get a proper introduction to it soon — Foundations only uses it lightly.

**Performance**  
How efficiently code runs. Measured with `%time`, `%timeit`. Vectorized operations (NumPy/Pandas) are usually faster than a Python-level loop.

**Tab Completion**  
Pressing `Tab` after a dot (`obj.`) in Jupyter to see available methods and attributes.

**Variable Explorer**  
`%who` and `%whos` — magic commands that list the variables currently in memory (and, for `%whos`, their types and values).

**`pathlib`** *(Challenge)*  
A built-in module for building file paths that work correctly across Windows, Mac, and Linux, e.g. `Path('data') / 'file.csv'`.

**Vectorization**  
Applying an operation to an entire array at once (NumPy/Pandas) instead of looping over it element by element.

**Virtual Environment (`.venv`)**  
A self-contained Python environment with its own installed packages. Covered in depth in `_StartHere`, not repeated here — just listed since you'll see the term throughout the course.
