# NGO Management System

A web-based system for managing NGO operations. Follow these steps to set up the project locally.

## Prerequisites
- [Git](https://git-scm.com/downloads)
- Python 3.6+
- pip (Python package installer)

## Installation Guide

### 1. Clone the Repository

#### All Operating Systems:
```bash
# Create project directory
mkdir ngo_system
cd ngo_system

# Clone repository
git clone https://github.com/Dullah2k/ngo.git

# Enter project directory
cd ngo
```

### 2. Set Up Virtual Environment

#### Windows (CMD):
```cmd
:: Create virtual environment
python -m venv env

:: Activate environment
env\Scripts\activate.bat
```

#### Windows (Git Bash)/macOS/Linux:
```bash
# Create virtual environment
python -m venv env

# Activate environment
source env/bin/activate
```

### 3. Install Dependencies

For all systems (ensure you're in project root directory where requirement.txt exists):
```bash
pip install -r requirement.txt
```

*Alternative for Chinese users (Tsinghua mirror):*
```bash
pip install -r requirement.txt --index-url https://pypi.tuna.tsinghua.edu.cn/simple
```

### 4. Run the Server

#### All Systems (ensure you're in project root with manage.py):
```bash
python manage.py runserver
```

Access the system at: [http://localhost:8000](http://localhost:8000)

## Directory Structure Notes
- `manage.py` is located in the project root (ngo/ directory)
- `requirement.txt` should be in the project root
- Virtual environment (env/) is created in project root

## Platform-Specific Tips

### Windows Users
- Use CMD for simpler path management
- If activation fails in Git Bash:
  ```bash
  source env/Scripts/activate
  ```

### macOS/Linux Users
- Use `python3` instead of `python` if needed
  ```bash
  python3 -m venv env
  ```

## Common Commands

| Action                  | Command                          |
|-------------------------|----------------------------------|
| Activate virtual env    | `env\Scripts\activate` (CMD)    |
|                         | `source env/bin/activate` (Bash)|
| Deactivate              | `deactivate`                    |
| Run server              | `python manage.py runserver`    |
| Install packages        | `pip install -r requirement.txt`|

## Troubleshooting
1. **"python: command not found"**
   - Use `python3` instead of `python`
   - Check Python installation

2. **"No such file/directory" errors**
   - Ensure you're in project root (ngo/ directory)
   - Verify file exists:
     - `requirement.txt`
     - `manage.py`

3. **Port conflicts**
   ```bash
   python manage.py runserver 8080  # Use alternative port
   ```

4. **Activation issues**
   - Windows CMD: Use full path:
     ```cmd
     .\env\Scripts\activate.bat
     ```
   - Delete and recreate virtual environment if corrupted

## Supported Systems
- Windows 10/11 (CMD & Git Bash)
- macOS Ventura and newer
- Ubuntu/Debian-based Linux distributions