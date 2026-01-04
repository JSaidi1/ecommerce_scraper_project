"""
Centralized project configuration.
Use environment variables with default values.
"""
import os
from dataclasses import dataclass
import sys
from dotenv import load_dotenv
from quotes_scraper_project.utils.util_fncs import search_file_in_parents
# ======================================================================================
#                                       CONFIG.
# ======================================================================================
# --- Config for .env file
ENV_FILE_IS_REQUIRED = True
ENV_FILE_NAME = ".env"
ENV_FILE_RESEARCH_MAX_PARENTS_LEVEL = 5 # Maximum number of parent directories in which the .env file will be searched
# ======================================================================================
#                                 LOAD ENV. VARIABLES
# ======================================================================================
# --- Define .env file path
env_file = search_file_in_parents(ENV_FILE_NAME, ENV_FILE_RESEARCH_MAX_PARENTS_LEVEL)
# --- Check if .env file exists
if not env_file:
    print(f"\n[WARNING]: environment file '.env' file not found in the current and '{ENV_FILE_RESEARCH_MAX_PARENTS_LEVEL}' parent directories: {env_file}")
    if ENV_FILE_IS_REQUIRED:
        print(f"The '.env' environment file is required to start the application.")
        sys.exit(1)
# --- Load .env file
load_dotenv(env_file)
# ======================================================================================
#                                 GET ENV. VARIABLES
# ======================================================================================
@dataclass
class EnvironmentConfig:
    environment: str = os.getenv("ENV", "dev").lower()

@dataclass
class DebugConfig:
    debug_mode: str = os.getenv("DEBUG", "true").lower()

@dataclass
class MinIOConfig:
    endpoint: str = os.getenv("S3_ENDPOINT", "localhost:9000")
    access_key: str = os.getenv("S3_ACCESS_KEY", "minioadmin")
    secret_key: str = os.getenv("S3_SECRET_KEY", "minioadmin123")
    secure: bool = os.getenv("S3_SECURE", "false").lower() == "true"
    bucket_images:str = "author-images"
    bucket_exports:str = "quotes-exports"
    bucket_backups:str = "quotes-backups"

@dataclass
class MongoDBConfig:
    host: str = os.getenv("MONGO_HOST", "localhost")
    port: int = int(os.getenv("MONGO_PORT", "27017"))
    username: str = os.getenv("MONGO_USER", "admin")
    password: str = os.getenv("MONGO_PASSWORD", "admin123")
    database: str = os.getenv("MONGO_DB", "scraping_db")

    @property
    def connection_string(self) -> str:
        return f"mongodb://{self.username}:{self.password}@{self.host}:{self.port}/"

@dataclass
class ScraperConfig:
    base_url:str = "https://quotes.toscrape.com"
    delay: float = 1.0 
    timeout: int = 30
    max_retries: int = 3
    max_pages: int = 20

environment_config = EnvironmentConfig()
debug_config = DebugConfig()
minio_config = MinIOConfig()
mongo_config = MongoDBConfig()
scraper_config = ScraperConfig()



if __name__ == "__main__":
    print("-> in settings.py")