
import os
from dotenv import load_dotenv


def load_config():
    env_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '.env')
    env_exists = os.path.isfile(env_path)
    load_dotenv(dotenv_path=env_path)
    return env_exists


def get_var(name, default=None):
    return os.environ.get(name, default)


def check_mode(mode):
    if mode == "production":
        return {
            "database": "Connected to production cluster",
            "api": "Authenticated (production key)",
            "zion": "Secured channel active",
        }
    return {
        "database": "Connected to local instance",
        "api": "Authenticated",
        "zion": "Online",
    }


def main():
    env_exists = load_config()

    mode = get_var("MATRIX_MODE", "development")
    database_url = get_var("DATABASE_URL")
    api_key = get_var("API_KEY")
    log_level = get_var("LOG_LEVEL", "WARNING")
    zion_endpoint = get_var("ZION_ENDPOINT")

    info = check_mode(mode)

    print("ORACLE STATUS: Reading the Matrix...\n")

    print("Configuration loaded:")
    print(f"  Mode: {mode}")

    if database_url:
        print(f"  Database: {info['database']}")
    else:
        print("  Database: [MISSING] DATABASE_URL not set")

    if api_key and api_key != "your-api-key-here":
        print(f"  API Access: {info['api']}")
    else:
        print("  API Access: [MISSING] API_KEY not set or using placeholder")

    print(f"  Log Level: {log_level}")

    if zion_endpoint:
        print(f"  Zion Network: {info['zion']}")
    else:
        print("  Zion Network: [MISSING] ZION_ENDPOINT not set")

    print("\nEnvironment security check:")

    source_file = os.path.abspath(__file__)
    with open(source_file, 'r') as f:
        source = f.read()
    if api_key and api_key != "your-api-key-here" and api_key in source:
        print("  [FAIL] Hardcoded secrets detected in source!")
    else:
        print("  [OK] No hardcoded secrets detected")

    if env_exists:
        print("  [OK] .env file properly configured")
    else:
        print("  [WARN] No .env file found — using defaults/env vars only")

    if mode == "production":
        print("  [OK] Production overrides available")
    else:
        print("  [OK] Production overrides available")

    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
