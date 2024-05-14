from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service

# Especifique o caminho para o ChromeDriver
driver_path = "C:\Program Files\Google\Chrome\Application\chrome.exe"

# Inicialize o serviço do ChromeDriver
service = Service(driver_path)

# Inicialize o WebDriver do Chrome
driver = Chrome(service=service)

# Agora você pode usar o 'driver' para interagir com o navegador Chrome






