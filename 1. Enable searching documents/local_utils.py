"""Local wrapper for common utility functions."""
import sys
from pathlib import Path

# Add project root to Python path to import utils
PROJECT_ROOT = Path(__file__).parent.parent.absolute()
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from utils import format_time_ago as _format_time_ago
from utils import print_documents_with_time as _print_documents_with_time
from utils import print_search_results as _print_search_results
from utils import print_document_chunks as _print_document_chunks


def format_time_ago(created_time, current_time=None):
    """
    Format a timestamp as a human-readable 'time ago' string.
    
    Args:
        created_time: datetime object when the resource was created
        current_time: datetime object for current time (optional, defaults to now in UTC)
    
    Returns:
        str: Human-readable time difference (e.g., "5 minutes ago", "2 hours ago")
    """
    return _format_time_ago(created_time, current_time)


def print_documents_with_time(docs, collection_name=None):
    """
    Print a formatted list of documents with upload times.
    
    Args:
        docs: List of document objects with document_path.document_name and created attributes
        collection_name: Optional collection name for the header
    """
    return _print_documents_with_time(docs, collection_name)


def print_search_results(results, query=None, max_text_length=150):
    """
    Print formatted search results with scores, document names, and content.
    
    Args:
        results: List of SearchResult objects
        query: Optional query string to display in header
        max_text_length: Maximum length of text excerpt to display
    """
    return _print_search_results(results, query, max_text_length)


def print_document_chunks(chunks, document_name=None, max_text_length=200):
    """
    Print formatted document chunks with position and content.
    
    Args:
        chunks: List of document chunks
        document_name: Optional document name for header
        max_text_length: Maximum length of text to display per chunk
    """
    return _print_document_chunks(chunks, document_name, max_text_length)