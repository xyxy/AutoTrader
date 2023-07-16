import autotrader
from autotrader.login import login

class Trader():
    def __init__(self):
        self._tesseract_cmd = r'.\tesseract\tesseract.exe'

    def init_trader(self, folder_path=r"C:\同花顺软件\同花顺"):
        login(folder_path)
        user = autotrader.use()

        user.connect(
            exe_path=folder_path + '\\xiadan.exe',
            tesseract_cmd=self._tesseract_cmd
        )

        return user
