import inspect
import app.config as config

def test_no_hardcoded_secrets():
    source = inspect.getsource(config)
    forbidden_keywords = ["SuperSecret", "hardcoded", "password", "API_KEY"]
    for word in forbidden_keywords:
        assert word not in source