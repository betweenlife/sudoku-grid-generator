# Sudoku Grid Generator

Sudoku Grid Generator allows you to create sudoku grids deciding the difficulty level (easy, medium, hard) and store them into an excel file.

## Prerequisites

1. **Python 3.7+**: Ensure you have Python installed on your system.
2. **Virtual Environment**: It's recommended to use a virtual environment for managing dependencies.

## Setup

### 1. Clone the Repository

```bash
git clone https://github.com/betweenlife/sudoku-grid-generator.git
cd sudoku-grid-generator
```

### 2. Create and Activate a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Generator

```bash
python generate.py
```

The console will ask you the difficulty to set for the grid.

### 6. Open sudoku.xlsx to check the grid

The file will be overwritten every time the generator is run. 
The file is formatted as a Sudoku, it's better avoiding modifies.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.