```bash
# Create main source directory
mkdir src

# 1. Frontend/UI Wizard folders and files
mkdir src\frontend
touch src\frontend\__init__.py
touch src\frontend\forms.py
touch src\frontend\layout.py
touch src\frontend\session_manager.py

# 2. Data Cruncher & Visualizer folders and files
mkdir src\analytics
touch src\analytics\__init__.py
touch src\analytics\calculator.py
touch src\analytics\visualizer.py
touch src\analytics\risk_analyzer.py

# 3. AI/OpenAI Specialist folders and files (already mentioned)
mkdir src\ai_engine
touch src\ai_engine\__init__.py
touch src\ai_engine\portfolio_analyzer.py
touch src\ai_engine\prompts.py

# 4. Report & Export Guru folders and files
mkdir src\export
touch src\export\__init__.py
touch src\export\pdf_generator.py
touch src\export\csv_exporter.py
touch src\export\report_templates.py

# Common/Shared resources
mkdir src\common
touch src\common\__init__.py
touch src\common\config.py
touch src\common\utils.py

# Main application file
touch app.py
touch requirements.txt
touch .env
```

Brief explanation of each folder's purpose:

### 1. Frontend (`src/frontend/`)
- `forms.py`: Streamlit input forms and widgets
- `layout.py`: UI layout and styling components
- `session_manager.py`: Handles Streamlit session state

### 2. Analytics (`src/analytics/`)
- `calculator.py`: Portfolio calculations and metrics
- `visualizer.py`: Charts and visualization functions
- `risk_analyzer.py`: Risk assessment algorithms

### 3. AI Engine (ai_engine)
- `portfolio_analyzer.py`: OpenAI integration
- `prompts.py`: GPT prompt templates

### 4. Export (`src/export/`)
- `pdf_generator.py`: PDF report generation
- `csv_exporter.py`: CSV export functionality
- `report_templates.py`: Report layout templates

### Common (`src/common/`)
- `config.py`: Configuration settings
- `utils.py`: Shared utility functions

Since you're on Windows, you can use these commands in PowerShell or replace `touch` with `ni` (New-Item) command:

```powershell
# Example for Windows PowerShell
ni src\frontend\__init__.py
```

This structure follows modular design principles and makes it easy for all team members to work independently on their components while maintaining clear integration points.