## Custom Word Count Tool

`ccwc` (Custom Word Count) is a Python-based command-line tool inspired by the Unix `wc` command. It counts bytes, lines, words, and characters in a text file or from standard input, supporting various command-line options. This tool was built to provide a lightweight, customizable alternative for file content analysis.

## Features
- **`-c`**: Outputs the number of bytes in a file.
- **`-l`**: Outputs the number of lines in a file.
- **`-w`**: Outputs the number of words in a file.
- **`-m`**: Outputs the number of characters in a file (locale-dependent; matches `-c` if multibyte characters are not supported).
- **Default (no options)**: Outputs lines, words, and bytes (equivalent to `-l -w -c`).
- **Standard Input**: Supports reading from `stdin` if no file is specified.

## Prerequisites
- Python 3.6 or higher.
- A text editor or IDE (e.g., VS Code).
- Git installed for version control.
- The `test.txt` file for testing (see Setup).

## Setup
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/AsifMinar/WordCountTool.git
   cd WordCountTool
   ```

2. **Download the Test File**:
   - Obtain the `test.txt` file (a sample text file for testing).
   - Save it in the root directory of the project.

3. **Verify Python Installation**:
   - Ensure Python is installed by running:
     ```bash
     python --version
     ```
   - No additional dependencies are required.

4. **Run the Program**:
   - Execute the script with:
     ```bash
     python ccwc.py
     ```

## Usage
Run the `ccwc` command with the desired options and file, or pipe input via `stdin`. Below are examples based on the expected outputs for `test.txt`.

### Count Bytes
```bash
python ccwc.py -c test.txt
```
**Output**:
```
  342190 test.txt
```

### Count Lines
```bash
python ccwc.py -l test.txt
```
**Output**:
```
    7145 test.txt
```

### Count Words
```bash
python ccwc.py -w test.txt
```
**Output**:
```
   58164 test.txt
```

### Count Characters
```bash
python ccwc.py -m test.txt
```
**Output** (locale-dependent):
```
  339292 test.txt
```

### Default (Lines, Words, Bytes)
```bash
python ccwc.py test.txt
```
**Output**:
```
    7145   58164  342190 test.txt
```

### Read from Standard Input
```bash
cat test.txt | python ccwc.py -l
```
**Output**:
```
    7145
```

## Development
The tool was developed incrementally:
1. Implemented byte counting (`-c`).
2. Added line counting (`-l`).
3. Added word counting (`-w`).
4. Added character counting (`-m`), with locale awareness.
5. Enabled default mode (lines, words, bytes).
6. Added support for reading from standard input.

## Project Structure
- `ccwc.py`: The main Python script containing the `ccwc` implementation.
- `test.txt`: Sample text file for testing (not included in the repository; user must provide).

## Testing
- Use `test.txt` to verify outputs match the expected results.
- Compare character counts with `wc -m test.txt` to ensure locale compatibility.
- Test `stdin` by piping input (e.g., `cat test.txt | python ccwc.py -l`).

## Contributing
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m "Add your feature"`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a Pull Request.

## License
This project is licensed under the MIT License.

## Acknowledgments
- Inspired by the Unix `wc` command.
- Built to explore Python's capabilities for command-line tools and file processing.