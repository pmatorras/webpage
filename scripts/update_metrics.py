import requests
import json
from pathlib import Path
from datetime import datetime
import time

AUTHOR_ID = '1642114'
AUTHOR_NAME = 'Pablo Matorras-Cuevas'
BASE_URL = 'https://inspirehep.net/api/literature'

def fetch_all_papers():
    """Fetch all papers with smaller page size"""
    all_papers = []
    page = 1
    size = 50  # Smaller batches to avoid timeout
    max_retries = 3
    
    while True:
        params = {
            'search_type': 'hep-author-publication',
            'author': f'{AUTHOR_ID}_{AUTHOR_NAME}',
            'size': size,
            'page': page
        }
        
        # Retry logic
        for attempt in range(max_retries):
            response = requests.get(BASE_URL, params=params, timeout=30)
            
            if response.status_code == 200:
                break
            
            if attempt < max_retries - 1:
                wait_time = 2 ** attempt
                print(f"Status {response.status_code}, retrying in {wait_time}s...")
                time.sleep(wait_time)
            else:
                print(f"Error: Status code {response.status_code} after {max_retries} attempts")
                return all_papers
        
        try:
            data = response.json()
        except json.JSONDecodeError:
            print(f"Error: Invalid JSON response")
            return all_papers
        
        hits = data['hits']['hits']
        all_papers.extend(hits)
        
        print(f"Fetched page {page}: {len(hits)} papers (total: {len(all_papers)})")
        
        if len(hits) < size:
            break
            
        page += 1
        time.sleep(1)  # Longer delay between requests
    
    return all_papers

# Fetch all papers
papers = fetch_all_papers()
from collections import Counter

# Check document types
doc_types = Counter()
for paper in papers:
    for dt in paper['metadata'].get('document_type', []):
        doc_types[dt] += 1

print("\nDocument type counts:")
for dt, count in doc_types.most_common():
    print(f"  {dt}: {count}")

# Check what has publication_info
has_pub_info = sum(1 for p in papers if p['metadata'].get('publication_info'))
print(f"\nPapers with publication_info: {has_pub_info}")

# Sample papers without publication_info
no_pub = [p for p in papers if not p['metadata'].get('publication_info')]
print(f"\nSample papers WITHOUT publication_info ({len(no_pub)} total):")
for p in no_pub[:5]:
    print(f"  - {p['metadata'].get('titles', [{}])[0].get('title', 'No title')}")
    print(f"    Doc types: {p['metadata'].get('document_type', [])}")
if not papers:
    print("No papers fetched!")
    exit(1)

# Calculate h-index
citation_counts = sorted(
    [p['metadata'].get('citation_count', 0) for p in papers],
    reverse=True
)

h_index = sum(1 for i, c in enumerate(citation_counts, 1) if c >= i)

# Citable: articles + conference papers + book chapters + thesis
citable_types = {'article', 'conference paper', 'thesis', 'book', 'book chapter'}
citable = [
    p for p in papers 
    if any(dt in citable_types for dt in p['metadata'].get('document_type', []))
]

# Published: Only articles with publication_info
published = [
    p for p in papers 
    if 'article' in p['metadata'].get('document_type', [])
    and p['metadata'].get('publication_info')
]

# Calculate citations
citable_citations = sum(p['metadata'].get('citation_count', 0) for p in citable)
published_citations = sum(p['metadata'].get('citation_count', 0) for p in published)

metrics = {
    'h_index': h_index,
    'papers_citable': len(citable),
    'papers_published': len(published),
    'citations_citable': citable_citations,
    'citations_published': published_citations,
    'avg_citations_citable': round(citable_citations / len(citable), 1) if citable else 0,
    'avg_citations_published': round(published_citations / len(published), 1) if published else 0,
    'last_updated': datetime.now().isoformat()
}

# Save
repo_root = Path(__file__).parent.parent
data_dir = repo_root / 'data'
data_dir.mkdir(exist_ok=True)

with open(data_dir / 'citations.json', 'w') as f:
    json.dump(metrics, f, indent=2)

print(f"\nMetrics saved:")
for key, value in metrics.items():
    print(f"  {key}: {value}")
