from typing import List
from pydantic import AnyHttpUrl
from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path

# 1. Localiza o diretório onde este arquivo (config.py) está
# 2. Define o caminho para o .env na mesma pasta
current_dir = Path(__file__).parent # caminho do arquivo config.py
env_path = current_dir / ".env" # evita problemas com caminhos relativos

class Settings(BaseSettings): 
    # API Config 

    # definições de prefixos como /api/v1/login 
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "TODOfast"
    
    # Security
    JWT_SECRET_KEY: str
    JWT_REFRESH_SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACESS_TOKEN_EXPIRE_MINUTES: int = 60
    # 7 dias em minutos = 10080
    REFRESH_TOKEN_EXPIRE_MINUTES: float = 10080.0
    
    # Cors
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    # Database
    MONGO_CONNECTION_STRING: str

    # Configuração do Pydantic para ler o arquivo .env
    model_config = SettingsConfigDict(
        env_file=str(env_path), 
        case_sensitive=True,
        extra="ignore" # Ignora variáveis extras no .env que não estão na classe
    )

# Instancia as configurações
try:
    settings01 = Settings()
except Exception as e:
    print(f"Erro ao carregar configurações: {e}")
    print(f"Caminho tentado para o .env: {env_path}")
    raise e