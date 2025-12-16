## CLI tools

### sys_tool
python src/sys_tool.py
python -c "import src.sys_tool"
python src/sys_tool.py --help

### click_tool
python src/click_tool.py say --name Alice
python src/click_tool.py say --name peter
python src/click_tool.py --help

### fire_expose
python src/fire_expose.py greet Alice
python src/fire_expose.py goodbye Bob
python src/fire_expose.py --help
