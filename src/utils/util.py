from datetime import datetime
from typing import Optional
import psycopg2
from psycopg2.extensions import connection
from src.config import config

def get_connection() -> connection:
    return psycopg2.connect(database=config.DB_NAME, 
                            user=config.DB_USER, 
                            password=config.DB_PASSWORD, 
                            host=config.DB_HOST, 
                            port=config.DB_PORT)

def parse_date(date_str: Optional[str]) -> Optional[str]:
    if date_str:
        try:
            return datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%SZ').strftime('%d %B %Y')
        except ValueError:
            try:
                return datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S.%fZ').strftime('%d %B %Y')
            except ValueError:
                return None
    return None
