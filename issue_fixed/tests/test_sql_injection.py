from app.database import init_db
from app.auth import authenticate

def test_sql_injection_prevention():
    init_db()
    malicious_input = "admin' OR '1'='1"
    assert authenticate(malicious_input, "anything") is False