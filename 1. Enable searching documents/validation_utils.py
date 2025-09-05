"""Local wrapper for environment validation."""
import sys
from pathlib import Path

# Add project root to Python path to import env_validator
PROJECT_ROOT = Path(__file__).parent.parent.absolute()
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from env_validator import validate_environment as _validate_environment


def validate_environment():
    """
    Validate environment configuration for the current directory.
    Automatically finds .env and .env.sample in the current working directory.
    """
    cwd = Path.cwd()
    env_path = cwd / '.env'
    env_sample_path = cwd / '.env.sample'
    
    return _validate_environment(
        env_path=str(env_path),
        env_sample_path=str(env_sample_path)
    )
