"""Common utility functions for tutorial notebooks."""

from datetime import datetime
import pytz


def format_time_ago(created_time, current_time=None):
    """
    Format a timestamp as a human-readable 'time ago' string.
    
    Args:
        created_time: datetime object when the resource was created
        current_time: datetime object for current time (optional, defaults to now in UTC)
    
    Returns:
        str: Human-readable time difference (e.g., "5 minutes ago", "2 hours ago")
    """
    # Handle timezone-aware comparison
    if created_time.tzinfo is None:
        # If server timestamp is naive (no timezone), assume UTC
        created_time = created_time.replace(tzinfo=pytz.UTC)
    
    # Get current time in UTC for proper comparison
    if current_time is None:
        current_time = datetime.now(pytz.UTC)
    elif current_time.tzinfo is None:
        current_time = current_time.replace(tzinfo=pytz.UTC)
    
    time_diff = current_time - created_time
    seconds_ago = int(time_diff.total_seconds())
    
    if seconds_ago < 60:
        return f"{seconds_ago} seconds ago"
    elif seconds_ago < 3600:
        minutes_ago = seconds_ago // 60
        return f"{minutes_ago} minutes ago"
    elif seconds_ago < 86400:  # Less than 24 hours
        hours_ago = seconds_ago // 3600
        return f"{hours_ago} hours ago"
    else:
        days_ago = seconds_ago // 86400
        return f"{days_ago} days ago"


def print_documents_with_time(docs, collection_name=None):
    """
    Print a formatted list of documents with upload times.
    
    Args:
        docs: List of document objects with document_path.document_name and created attributes
        collection_name: Optional collection name for the header
    """
    print("\n")
    if collection_name:
        print(f"\033[94mℹ️  INFO: Documents in collection '{collection_name}'\033[0m")
    else:
        print("\033[94mℹ️  INFO: Documents in collection\033[0m")
    print("\n")

    for doc in docs:
        document_name = doc.document_path.document_name
        time_str = format_time_ago(doc.created)
        print(f"   📄 {document_name}: uploaded {time_str}")

    print("\n")
    print(f"\033[92m✅ SUCCESS: Found {len(docs)} documents in collection\033[0m")
    print("\n")


def print_search_results(results, query=None, max_text_length=150):
    """
    Print formatted search results with scores, document names, and content.
    
    Args:
        results: List of SearchResult objects
        query: Optional query string to display in header
        max_text_length: Maximum length of text excerpt to display
    """
    print("\n")
    if query:
        print(f"\033[94mℹ️  INFO: Search results for query: '{query}'\033[0m")
    else:
        print("\033[94mℹ️  INFO: Search results\033[0m")
    print("\n")
    
    for i, result in enumerate(results, 1):
        score = result.score
        doc_name = result.id.document_name
        text = result.document_chunk.text
        
        # Truncate text if too long
        if len(text) > max_text_length:
            text = text[:max_text_length] + "..."
        
        # Clean up text (remove wiki markup, extra spaces)
        text = text.replace("[[", "").replace("]]", "").replace("'''", "")
        text = " ".join(text.split())  # Normalize whitespace
        
        # Use consistent color for all scores
        score_color = "\033[93m"  # Yellow for all scores
        
        print(f"   \033[96m#{i}\033[0m 📄 \033[94m{doc_name}\033[0m")
        print(f"      {score_color}Score: {score:.3f}\033[0m")
        print(f"      💬 \"{text}\"")
        print()  # Empty line between results
    
    print(f"\033[92m✅ SUCCESS: Found {len(results)} relevant documents\033[0m")
    print("\n")


def print_document_chunks(chunks, document_name=None, max_text_length=200):
    """
    Print formatted document chunks with position and content.
    
    Args:
        chunks: List of document chunks
        document_name: Optional document name for header
        max_text_length: Maximum length of text to display per chunk
    """
    print("\n")
    if document_name:
        print(f"\033[94mℹ️  INFO: Document chunks for '{document_name}'\033[0m")
    else:
        print("\033[94mℹ️  INFO: Document chunks\033[0m")
    print("\n")
    
    for i, chunk in enumerate(chunks, 1):
        text = chunk.section
        start = chunk.position.start_position
        end = chunk.position.end_position
        
        # Truncate text if too long
        if text and len(text) > max_text_length:
            text = text[:max_text_length] + "..."
        
        # Clean up text (remove wiki markup, extra spaces) if it's a string
        if isinstance(text, str):
            text = text.replace("[[", "").replace("]]", "").replace("'''", "")
            text = " ".join(text.split())  # Normalize whitespace
        
        print(f"   \033[96m#{i}\033[0m 📄 Chunk {i}")
        print(f"      \033[93mPosition: {start}-{end}\033[0m")
        print(f"      💬 \"{text}\"")
        print()  # Empty line between chunks
    
    print(f"\033[92m✅ SUCCESS: Found {len(chunks)} chunks\033[0m")
    print("\n")
