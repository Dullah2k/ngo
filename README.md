# NGO Management System

A web-based system for managing NGO operations. Follow the steps below to set up the project on your local machine.

## Prerequisites
- [Git](https://git-scm.com/downloads)
- Python 3.6+
- pip (Python package installer)

## Installation

### 1. Clone the Repository

#### Windows (CMD) / macOS / Linux:
```bash
# Create project directory
mkdir ngo_system
cd ngo_system

# Clone repository
git clone https://github.com/Dullah2k/ngo.git

# Enter project directory
cd ngo
```

#### Windows (Git Bash):
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
```bash
python -m venv env
env\Scripts\activate.bat
```

#### Windows (Git Bash)/macOS/Linux:
```bash
python -m venv env
source env/bin/activate
```

### 3. Install Dependencies

For all systems (with activated virtual environment):
```bash
pip install -r requirement.txt
```

*For users in China/mainland China, use Tsinghua mirror:*
```bash
pip install -r requirement.txt --index-url https://pypi.tuna.tsinghua.edu.cn/simple
```

## Running the Server

With virtual environment activated:
```bash
python manage.py runserver
```

Access the system at: [http://localhost:8000](http://localhost:8000)

## Additional Notes

### Virtual Environment Management
- To deactivate virtual environment:
  ```bash
  deactivate
  ```
- To reactivate later:
  - CMD: `env\Scripts\activate.bat`
  - Git Bash/macOS/Linux: `source env/bin/activate`

### Supported Platforms
Tested and works on:
- Windows 10/11 (CMD & Git Bash)
- macOS Monterey (12.0+)
- Ubuntu 20.04 LTS

### Common Issues
1. If Python commands aren't recognized:
   - Use `python3` instead of `python`
   - Ensure Python is added to system PATH
2. If `requirement.txt` installation fails:
   - Verify file exists in project root
   - Check for typos in filename
3. Port conflict: Add specific port if default is busy
   ```bash
   python manage.py runserver 8080
   ```