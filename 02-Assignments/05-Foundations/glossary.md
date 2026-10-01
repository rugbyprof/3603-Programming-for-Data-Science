# 📚 Glossary: 06 - Foundations

Terms are in alphabetical order. The number in brackets shows the notebook where each term is introduced.

**Absolute Path** [05]  
A path that starts from the root of the drive, e.g. `C:/Users/me/data.csv` or `/Users/me/data.csv`. It always points to the same place, but only on one computer. Compare **Relative Path**.

**Axes** [07]  
In Matplotlib, the chart area where data is drawn (not the same as an x- or y-*axis*). A **Figure** can hold several Axes. See **Subplots**.

**Boolean Mask** [07]  
An array of `True`/`False` values used to select items, e.g. `scores[scores >= 85]` keeps only the scores that pass.

**Box Plot** [07]  
A chart showing a distribution's median (line in the box), middle 50% (the box), spread (whiskers), and possible outliers (dots beyond the whiskers).

**Category (dtype)** [08]  
A Pandas column type for text with only a few distinct values. Each value is stored once, which can save a lot of memory.

**Cell** [02]  
A block in a Jupyter notebook that can contain **code** or **Markdown**. Code cells run Python; Markdown cells render formatted text.

**Cell Magic** [01]  
A magic command starting with `%%` that applies to the entire cell and must be its first line, e.g. `%%writefile`, `%%time`. Compare **Line Magic**.

**Chunk** [08]  
A piece of a large file read one at a time with `pd.read_csv(..., chunksize=...)`, so the whole file never has to fit in memory.

**Command Mode** [02]  
Notebook mode where you operate on whole cells (add, delete, move, change type). Enter with `Esc`.

**Command Palette** [02]  
A searchable list of every command in VS Code (`Ctrl+Shift+P`, or `Cmd+Shift+P` on Mac). Useful when you don't remember a shortcut.

**CSV (Comma-Separated Values)** [05]  
A plain-text format for tabular data: one row per line, with columns separated by commas. It stores no types, so everything is read back as text unless a tool like Pandas converts it.

**DataFrame** [06]  
A 2D table of data provided by Pandas. Has rows, columns, and labels.

**Docstring** [03]  
The documentation text (in triple quotes) at the top of a function or class. It's what `?` and `help()` display.

**dtype** [06, 07]  
The data type of the values in a NumPy array or Pandas column, e.g. `int64`, `float64`, `str`. It decides how values behave and how much memory each one uses.

**Edit Mode** [02]  
Notebook mode where you type inside a cell. Enter with `Enter`.

**Encoding** [05]  
How text characters are stored as bytes. Use `encoding='utf-8'` when opening text files so accents and emoji work on every operating system.

**Execution Count** [02]  
The number next to a code cell, like `[7]`. It shows the order cells were **run in**, not their position in the notebook.

**Export** [02]  
Saving a notebook in another format (`.html`, `.pdf`, `.py`, Markdown). In VS Code, use the `...` menu → **Export**.

**Figure** [07]  
In Matplotlib, the whole image, which contains one or more **Axes**.

**glob** [05]  
A pattern for finding files by name, where `*` means "anything", e.g. `Path('data').glob('*.csv')`. `rglob` also searches subfolders.

**Histogram** [07]  
A chart showing the distribution of one numeric variable by grouping its values into ranges called **bins**. Compare a bar chart, which compares categories.

**JSON (JavaScript Object Notation)** [05, 06]  
A structured text format using key–value pairs and lists. Often used for configs and web APIs. Tuples come back as lists, and dictionary keys come back as strings.

**JSON Lines (`.jsonl`)** [06]  
A JSON format with one complete record per line. Read and write it with `lines=True` in Pandas.

**Kernel** [02]  
The Python process that runs a notebook's code and holds its variables. The notebook is the recipe; the kernel is the kitchen. Restarting the kernel wipes all variables.

**LaTeX** [04]  
A math typesetting language. Used in notebooks for equations like $E = mc^2$, inline with `$...$` or as a block with `$$...$$`.

**Line Magic** [01]  
A magic command starting with `%` that applies to one line, e.g. `%pwd`, `%timeit`. Compare **Cell Magic**.

**Magic Command** [01]  
A special IPython command starting with `%` (line magic) or `%%` (cell magic) that provides a shortcut, e.g. `%pwd`, `%whos`, `%%writefile`, `%timeit`.

**Markdown** [04]  
A lightweight markup language for formatting text in notebooks: `**bold**`, `*italic*`, `# heading`, lists, links, and tables.

**Nested JSON** [06]  
JSON with dictionaries inside dictionaries, common in API responses. `pd.json_normalize()` flattens it into regular columns.

**NumPy** [07]  
A Python library for fast numeric **arrays**. Math on an array applies to every element at once, e.g. `arr ** 2`.

**Orient** [06]  
The layout Pandas uses when writing JSON. `orient='records'` gives a list with one dictionary per row, the layout most APIs use.

**Output Files Folder (`NN-OutputFiles`)** [all]  
The folder where each notebook saves the files it creates, e.g. `05-OutputFiles`. Upload it along with the notebook so your work can be graded.

**`pathlib`** [05]  
A built-in module for building and inspecting file paths that work on Windows, Mac, and Linux, e.g. `Path('data') / 'file.csv'`, `.exists()`, `.suffix`, `.mkdir()`.

**Performance** [08]  
How efficiently code runs, in time and memory. Measured with `%time`, `%timeit`, `%prun`, `.nbytes`, and `memory_usage`.

**Profiling** [08]  
Measuring **where** the time goes inside code. `%prun` reports time per function; `%lprun` (from `line_profiler`) reports time per line.

**Relative Path** [05]  
A path resolved from the current working directory, e.g. `data/file.csv` or `../notes.txt`. Use relative paths in shared notebooks so they work on anyone's machine.

**Restart & Run All** [02]  
Restarting the kernel and running every cell from top to bottom. The best way to prove a notebook works with no leftover state. Do it before every submission.

**Shell Command** [01]  
A line starting with `!` that runs in your operating system's shell, e.g. `!ls`. Output can be captured (`files = !ls`), and Python variables can be passed in with `{name}`.

**Signature** [03]  
The list of arguments a function accepts, shown at the top of `?` output, e.g. `linspace(start, stop, num=50)`. Arguments without `=` are required; `name=value` shows a default.

**Subplots** [07]  
Several charts in one figure, created with `fig, axes = plt.subplots(rows, cols)`. Each chart is drawn with `ax.` methods like `ax.set_title()`.

**Tab Completion** [03]  
Pressing `Tab` (or `Ctrl+Space` in VS Code) to see the names, methods, and attributes available, e.g. after typing `obj.`.

**Traceback** [03]  
The error report Python prints when something fails. Read it from the **bottom up**: the last line names the error type and the reason.

**Variable Explorer** [01]  
`%who` and `%whos`: magic commands that list the variables currently in memory (and, for `%whos`, their types and values).

**Vectorization** [07, 08]  
Applying an operation to an entire array or column at once (NumPy/Pandas) instead of looping over it element by element. Usually much faster, and often clearer.

**Virtual Environment (`.venv`)**  
A self-contained Python environment with its own installed packages. Covered in depth in `_StartHere` and not repeated here. It's listed because you'll see the term throughout the course.

**Wall Time** [08]  
Real "clock on the wall" time, meaning how long you actually waited. Reported by `%time` alongside CPU time.

**Working Directory** [01, 05]  
The folder that relative paths start from. Check it with `%pwd` or `Path.cwd()`. A `%cd` stays in effect for every later cell.
