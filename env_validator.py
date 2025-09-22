import os
import sys
from urllib.parse import urlparse
from dotenv import load_dotenv, dotenv_values


def mask_sensitive_value(var_name: str, value: str) -> str:
    """Mask sensitive values for display."""
    if "TOKEN" in var_name:
        if len(value) > 8:
            first_chars = value[:8]
            last_chars = value[-8:]
            return f"{first_chars}...{last_chars}"
        else:
            return "***"
    return value


def read_env_sample_defaults(sample_path: str = '.env.sample') -> dict:
    """Read default values from .env.sample file."""
    defaults = {}
    
    try:
        defaults = dotenv_values(sample_path)
        defaults = {k: v for k, v in defaults.items() if v}
    except FileNotFoundError:
        print(f"   ❌  Could not find {sample_path} file to check defaults")
    except Exception as e:
        print(f"   ❌  Error reading {sample_path}: {str(e)}")
    
    return defaults


def check_required_variables(required_vars: list = None, vars_needing_customization: list = None, env_sample_path: str = '.env.sample') -> bool:
    """Check if all required environment variables are set."""
    if required_vars is None:
        required_vars = [
            "PHARIA_API_BASE_URL",
            "PHARIA_AI_TOKEN", 
            "PHARIA_DATA_NAMESPACE",
            "PHARIA_DATA_COLLECTION",
            "INDEX",
            "HYBRID_INDEX",
            "FILTER_INDEX",
            "EMBEDDING_MODEL_NAME"
        ]
    
    if vars_needing_customization is None:
        vars_needing_customization = [
            "PHARIA_DATA_COLLECTION",
            "INDEX",
            "HYBRID_INDEX",
            "FILTER_INDEX"
        ]
    
    defaults = read_env_sample_defaults(env_sample_path)
    
    has_errors = False
    print("1️⃣  Checking required environment variables:")
    
    for var in required_vars:
        value = os.getenv(var)
        if not value or value.strip() == "":
            print(f"   ❌ {var}: NOT SET")
            has_errors = True
        else:
            display_value = mask_sensitive_value(var, value)
            
            if var in vars_needing_customization and var in defaults:
                default_value = defaults[var]
                if value == default_value:
                    print(f"   ❌  {var}: {display_value} - Using default value! Please add a unique suffix (e.g., {default_value}-yourname)")
                    has_errors = True
                else:
                    print(f"   ✅ {var}: {display_value}")
            else:
                print(f"   ✅ {var}: {display_value}")
    
    return has_errors


def validate_api_url(api_base_url: str) -> bool:
    """Validate the API base URL format."""
    print("\n2️⃣  Validating URL format:")
    
    if not api_base_url:
        return False
    
    try:
        parsed = urlparse(api_base_url)
        if not parsed.scheme or not parsed.netloc:
            print(f"   ❌ PHARIA_API_BASE_URL: Invalid URL format")
            return True
        else:
            print(f"   ✅ PHARIA_API_BASE_URL: Valid format")
            return False
    except Exception as e:
        print(f"   ❌ PHARIA_API_BASE_URL: Error parsing URL - {str(e)}")
        return True


def test_api_connection(api_base_url: str, token: str) -> bool:
    """Test connection to PhariaAI API."""
    print("\n3️⃣  Testing PhariaAI API access:")
    
    if not api_base_url or not token:
        print("   ❌  Skipping API test - Missing API URL or token")
        return False
    
    try:
        from pharia_data_sdk.connectors import DocumentIndexClient
        
        search_api_url = f"{api_base_url}/v1/studio/search"
        
        search_client = DocumentIndexClient(
            token=token,
            base_url=search_api_url,
        )
        
        try:
            namespaces = search_client.list_namespaces()
            print(f"   ✅ API connection successful")
            return False
                
        except Exception as e:
            if "401" in str(e) or "403" in str(e):
                print("   ❌ Authentication failed - Invalid token")
            else:
                print(f"   ❌ API connection failed: {str(e)}")
                print(f"   ❌ Attempted URL: {search_api_url}")
            return True
                
    except ImportError:
        print("   ❌ pharia-data-sdk not installed - Please run: uv pip install pharia-data-sdk")
        return True
    except Exception as e:
        print(f"   ❌ Unexpected error: {str(e)}")
        return True


def validate_environment(env_path: str = '.env', load_env: bool = True, override: bool = True, env_sample_path: str = '.env.sample') -> bool:
    """
    Run all environment validation checks.
    
    Args:
        env_path: Path to the .env file to load
        load_env: Whether to load .env file
        override: Whether to override existing environment variables
        env_sample_path: Path to the .env.sample file for defaults comparison
        
    Returns:
        True if validation passed, False otherwise
    """
    if load_env:
        load_dotenv(env_path, override=override)
    
    print("🔍 Validating environment configuration...\n")
    
    has_var_errors = check_required_variables(env_sample_path=env_sample_path)
    
    api_base_url = os.getenv("PHARIA_API_BASE_URL", "")
    has_url_errors = validate_api_url(api_base_url)
    
    token = os.getenv("PHARIA_AI_TOKEN")
    has_connection_errors = test_api_connection(api_base_url, token)
    
    print("\n" + "="*50)
    
    if not (has_var_errors or has_url_errors or has_connection_errors):
        print("✅ All validation checks passed! Your environment is properly configured.")
        print("\nYou can now proceed with the tutorial.")
        return True
    else:
        print("❌ Validation failed! Please check the errors above.")
        return False


if __name__ == "__main__":
    validate_environment()
