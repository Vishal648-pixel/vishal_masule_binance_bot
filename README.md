# vishal_masule_binance_bot

🛠 Setup with venv
1. Create Virtual Environment
Go to your project root (where src/, README.md etc. are):

bash
cd project_root
python -m venv venv
👉 This will create a folder named venv/ with its own Python + pip.

2. Activate venv
Windows (PowerShell):

bash
venv\Scripts\activate
Linux / macOS (bash/zsh):

bash
source venv/bin/activate
After activation, you’ll see (venv) before your terminal prompt.

3. Install Dependencies
If you have a requirements.txt (check README.md), run:

bash
pip install -r requirements.txt
If not, manually install needed packages (example):

bash
pip install requests pandas numpy
4. Run Your Files
Now you can run any script inside src/:

Market orders:

bash
python src/market_orders.py
Limit orders:

bash
python src/limit_orders.py
Advanced strategies:

bash
python src/advanced/oco.py
python src/advanced/twap.py
Logs will go into bot.log, and you can check them live:

bash
tail -f bot.log
5. Deactivate venv
When you’re done:

bash
deactivate
