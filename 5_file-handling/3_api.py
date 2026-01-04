"""
================================================================================
PYTHON FILE HANDLING: WORKING WITH APIs
================================================================================
Day: 19 (Part 2)

Description:
    Complete guide to consuming REST APIs in Python. Covers urllib for basic
    requests, the requests library for advanced usage, JSON parsing from APIs,
    error handling, and practical patterns for data collection.

Learning Objectives:
    - Understand REST APIs and HTTP methods
    - Make HTTP requests with urllib and requests
    - Parse JSON responses from APIs
    - Handle errors, timeouts, and rate limits
    - Build reusable API client classes
    - Apply API consumption in ML/AI data pipelines

Prerequisites:
    - JSON handling (Day 19 Part 1)
    - File handling basics (Day 12)
================================================================================
"""

import json
from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError
from urllib.parse import urlencode
import time

# =============================================================================
# 1. WHAT ARE APIs?
# =============================================================================

"""
API (Application Programming Interface):
- Allows programs to communicate with each other
- REST APIs use HTTP requests (GET, POST, PUT, DELETE)
- Return data in JSON format (usually)

Common HTTP Methods:
- GET: Retrieve data
- POST: Create new data
- PUT: Update existing data
- DELETE: Remove data

HTTP Status Codes:
- 200: OK (Success)
- 201: Created
- 400: Bad Request
- 401: Unauthorized
- 403: Forbidden
- 404: Not Found
- 429: Too Many Requests (Rate Limited)
- 500: Server Error

Why APIs matter for AI/ML:
- Collect training data
- Access pre-trained models
- Deploy models as APIs
- Get real-time data for predictions
"""


# =============================================================================
# 2. BASIC REQUESTS WITH urllib
# =============================================================================

"""
urllib is Python's built-in library for HTTP requests.
No installation needed!
"""

print("=== Basic urllib Request ===")

# --- Simple GET request ---
# Using JSONPlaceholder - a free fake API for testing
url = "https://jsonplaceholder.typicode.com/users/1"

try:
    with urlopen(url) as response:
        # Read response
        data = response.read()
        # Decode bytes to string
        text = data.decode('utf-8')
        # Parse JSON
        user = json.loads(text)
        
        print(f"Status: {response.status}")
        print(f"User: {user['name']}")
        print(f"Email: {user['email']}")
        print(f"Company: {user['company']['name']}")

except URLError as e:
    print(f"URL Error: {e}")
except HTTPError as e:
    print(f"HTTP Error {e.code}: {e.reason}")


# =============================================================================
# 3. FETCHING EXCHANGE RATES
# =============================================================================

print("\n=== Exchange Rate API ===")

# Using free exchange rate API
exchange_url = "https://open.er-api.com/v6/latest/USD"

try:
    with urlopen(exchange_url, timeout=10) as response:
        source = response.read().decode('utf-8')
        data = json.loads(source)
        
        if data.get('result') == 'success':
            rates = data['rates']
            
            print(f"Base: {data['base_code']}")
            print(f"Last Updated: {data['time_last_update_utc']}")
            print("\nSample Rates (1 USD = ):")
            
            # Common currencies
            currencies = ['EUR', 'GBP', 'JPY', 'INR', 'CAD', 'AUD']
            for curr in currencies:
                if curr in rates:
                    print(f"  {curr}: {rates[curr]:.4f}")
            
            # Currency conversion example
            usd_amount = 100
            inr_rate = rates.get('INR', 0)
            print(f"\n${usd_amount} USD = ₹{usd_amount * inr_rate:.2f} INR")
        else:
            print("API request was not successful")

except URLError as e:
    print(f"Error fetching exchange rates: {e}")
except json.JSONDecodeError as e:
    print(f"Error parsing JSON: {e}")


# =============================================================================
# 4. WORKING WITH QUERY PARAMETERS
# =============================================================================

print("\n=== Query Parameters ===")

# Building URLs with parameters
base_url = "https://jsonplaceholder.typicode.com/posts"
params = {
    'userId': 1,
    '_limit': 3
}

# Properly encode parameters
query_string = urlencode(params)
full_url = f"{base_url}?{query_string}"

print(f"URL: {full_url}")

try:
    with urlopen(full_url) as response:
        posts = json.loads(response.read().decode('utf-8'))
        
        print(f"\nPosts by user 1 (limited to 3):")
        for post in posts:
            print(f"  - {post['title'][:50]}...")

except URLError as e:
    print(f"Error: {e}")


# =============================================================================
# 5. CUSTOM HEADERS AND USER-AGENT
# =============================================================================

print("\n=== Custom Headers ===")

url = "https://jsonplaceholder.typicode.com/posts/1"

# Create request with custom headers
headers = {
    'User-Agent': 'Mozilla/5.0 (Python ML Client)',
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}

request = Request(url, headers=headers)

try:
    with urlopen(request) as response:
        data = json.loads(response.read().decode('utf-8'))
        print(f"Title: {data['title']}")
        print(f"Response Headers: {dict(response.headers)['Content-Type']}")

except URLError as e:
    print(f"Error: {e}")


# =============================================================================
# 6. ERROR HANDLING AND RETRIES
# =============================================================================

def fetch_with_retry(url, max_retries=3, timeout=10, delay=1):
    """
    Fetch URL with automatic retry on failure.
    
    Args:
        url: URL to fetch
        max_retries: Maximum number of retry attempts
        timeout: Request timeout in seconds
        delay: Delay between retries in seconds
    
    Returns:
        Parsed JSON data or None on failure
    """
    last_error = None
    
    for attempt in range(1, max_retries + 1):
        try:
            print(f"  Attempt {attempt}/{max_retries}...")
            
            with urlopen(url, timeout=timeout) as response:
                if response.status == 200:
                    return json.loads(response.read().decode('utf-8'))
                else:
                    print(f"  Unexpected status: {response.status}")
                    
        except HTTPError as e:
            last_error = e
            if e.code == 429:  # Rate limited
                print(f"  Rate limited. Waiting {delay * 2}s...")
                time.sleep(delay * 2)
            elif e.code >= 500:  # Server error - retry
                print(f"  Server error ({e.code}). Retrying...")
                time.sleep(delay)
            else:  # Client error - don't retry
                print(f"  Client error ({e.code}): {e.reason}")
                return None
                
        except URLError as e:
            last_error = e
            print(f"  Connection error: {e.reason}")
            time.sleep(delay)
            
        except Exception as e:
            last_error = e
            print(f"  Unexpected error: {e}")
            time.sleep(delay)
    
    print(f"  All {max_retries} attempts failed. Last error: {last_error}")
    return None


print("\n=== Fetch with Retry ===")
data = fetch_with_retry("https://jsonplaceholder.typicode.com/users")
if data:
    print(f"Fetched {len(data)} users successfully")


# =============================================================================
# 7. FETCHING MULTIPLE ITEMS
# =============================================================================

def fetch_all_paginated(base_url, pages=3, per_page=10):
    """Fetch data from paginated API"""
    all_data = []
    
    for page in range(1, pages + 1):
        url = f"{base_url}?_page={page}&_limit={per_page}"
        
        try:
            with urlopen(url, timeout=10) as response:
                data = json.loads(response.read().decode('utf-8'))
                all_data.extend(data)
                print(f"  Page {page}: fetched {len(data)} items")
                
                if len(data) < per_page:
                    print("  Reached end of data")
                    break
                    
        except URLError as e:
            print(f"  Error on page {page}: {e}")
            break
        
        # Be nice to the API
        time.sleep(0.5)
    
    return all_data


print("\n=== Paginated Fetching ===")
posts = fetch_all_paginated("https://jsonplaceholder.typicode.com/posts", pages=3, per_page=5)
print(f"Total fetched: {len(posts)} posts")


# =============================================================================
# 8. SAVING API DATA TO FILES
# =============================================================================

print("\n=== Save API Data to File ===")

def fetch_and_save(url, filepath):
    """Fetch JSON from API and save to file"""
    try:
        with urlopen(url, timeout=10) as response:
            data = json.loads(response.read().decode('utf-8'))
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)
        
        print(f"Saved data to {filepath}")
        return True
        
    except (URLError, json.JSONDecodeError) as e:
        print(f"Error: {e}")
        return False


# Fetch and save users
fetch_and_save(
    "https://jsonplaceholder.typicode.com/users",
    "5_file-handling/api_users.json"
)


# =============================================================================
# 9. PRACTICAL API CLIENT CLASS
# =============================================================================

class APIClient:
    """Reusable API client with error handling and caching"""
    
    def __init__(self, base_url, timeout=10, cache_enabled=True):
        self.base_url = base_url.rstrip('/')
        self.timeout = timeout
        self.cache_enabled = cache_enabled
        self._cache = {}
    
    def _make_request(self, endpoint, params=None):
        """Make HTTP request to endpoint"""
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        
        if params:
            url = f"{url}?{urlencode(params)}"
        
        # Check cache
        if self.cache_enabled and url in self._cache:
            print(f"  [Cache hit] {endpoint}")
            return self._cache[url]
        
        try:
            headers = {
                'User-Agent': 'Python API Client',
                'Accept': 'application/json'
            }
            request = Request(url, headers=headers)
            
            with urlopen(request, timeout=self.timeout) as response:
                data = json.loads(response.read().decode('utf-8'))
                
                # Cache successful response
                if self.cache_enabled:
                    self._cache[url] = data
                
                return data
                
        except HTTPError as e:
            print(f"HTTP Error {e.code}: {e.reason}")
            return None
        except URLError as e:
            print(f"URL Error: {e.reason}")
            return None
        except json.JSONDecodeError as e:
            print(f"JSON Error: {e}")
            return None
    
    def get(self, endpoint, params=None):
        """GET request"""
        return self._make_request(endpoint, params)
    
    def clear_cache(self):
        """Clear the response cache"""
        self._cache.clear()


print("\n=== API Client Class ===")

# Create client
client = APIClient("https://jsonplaceholder.typicode.com")

# Fetch data
users = client.get("/users")
if users:
    print(f"Fetched {len(users)} users")

# Fetch with parameters
posts = client.get("/posts", {'userId': 1, '_limit': 3})
if posts:
    print(f"Fetched {len(posts)} posts for user 1")

# Cache demonstration
print("\nSecond request (should be cached):")
users_cached = client.get("/users")


# =============================================================================
# 10. ML/AI DATA COLLECTION EXAMPLE
# =============================================================================

class DataCollector:
    """Collect and save data from multiple API endpoints"""
    
    def __init__(self, output_dir):
        self.output_dir = output_dir
        self.collected = []
    
    def collect_from_api(self, url, name, transform_func=None):
        """Collect data from API endpoint"""
        print(f"Collecting {name}...")
        
        try:
            with urlopen(url, timeout=15) as response:
                data = json.loads(response.read().decode('utf-8'))
            
            # Apply transformation if provided
            if transform_func:
                data = transform_func(data)
            
            # Save to file
            filepath = f"{self.output_dir}/{name}.json"
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2)
            
            self.collected.append({
                'name': name,
                'url': url,
                'count': len(data) if isinstance(data, list) else 1,
                'filepath': filepath
            })
            
            print(f"  Saved {name} to {filepath}")
            return data
            
        except Exception as e:
            print(f"  Error collecting {name}: {e}")
            return None
    
    def summary(self):
        """Print collection summary"""
        print("\n=== Collection Summary ===")
        for item in self.collected:
            print(f"  {item['name']}: {item['count']} items")


# Example usage
print("\n=== Data Collection Example ===")

collector = DataCollector("5_file-handling")

# Collect users
collector.collect_from_api(
    "https://jsonplaceholder.typicode.com/users",
    "collected_users"
)

# Collect posts with transformation
def extract_titles(posts):
    return [{'id': p['id'], 'title': p['title']} for p in posts]

collector.collect_from_api(
    "https://jsonplaceholder.typicode.com/posts",
    "post_titles",
    transform_func=extract_titles
)

collector.summary()


# =============================================================================
# 11. CRYPTOCURRENCY PRICES (Real-World Example)
# =============================================================================

print("\n=== Cryptocurrency Prices ===")

# Using CoinGecko free API
crypto_url = "https://api.coingecko.com/api/v3/simple/price"
params = {
    'ids': 'bitcoin,ethereum,dogecoin',
    'vs_currencies': 'usd,inr',
    'include_24hr_change': 'true'
}

full_url = f"{crypto_url}?{urlencode(params)}"

try:
    with urlopen(full_url, timeout=10) as response:
        data = json.loads(response.read().decode('utf-8'))
        
        print("Current Prices:")
        for crypto, prices in data.items():
            print(f"\n{crypto.upper()}:")
            print(f"  USD: ${prices.get('usd', 'N/A'):,.2f}")
            print(f"  INR: ₹{prices.get('inr', 'N/A'):,.2f}")
            change = prices.get('usd_24h_change', 0)
            arrow = "↑" if change > 0 else "↓"
            print(f"  24h Change: {arrow} {abs(change):.2f}%")

except URLError as e:
    print(f"Error fetching crypto prices: {e}")
except Exception as e:
    print(f"Error: {e}")


# =============================================================================
# KEY TAKEAWAYS
# =============================================================================
"""
1. urllib Basics
   - urlopen(url): Simple GET request
   - Request(url, headers): Custom headers
   - response.read().decode('utf-8'): Get response text
   - json.loads(): Parse JSON response

2. Error Handling
   - HTTPError: HTTP status errors (4xx, 5xx)
   - URLError: Connection errors
   - Always use try/except with API calls

3. Best Practices
   - Use timeout to prevent hanging
   - Implement retry logic for failures
   - Respect rate limits (add delays)
   - Cache responses when appropriate
   - Use descriptive User-Agent

4. Query Parameters
   - urlencode(params): Safely encode parameters
   - Add to URL: f"{base}?{query_string}"

5. Production Patterns
   - Create reusable API client classes
   - Save raw responses to files
   - Transform data before storing
   - Log all API interactions
"""


# =============================================================================
# PRACTICE EXERCISES
# =============================================================================

# Exercise 1: Weather API [EASY]
# Fetch weather data for a city
# TODO: Use a free weather API

# Exercise 2: Rate-Limited Fetcher [MEDIUM]
# Implement proper rate limiting (X requests per minute)
# TODO: Write your code here

# Exercise 3: API Response Validator [CHALLENGE]
# Validate API responses against expected schema
# TODO: Write your code here


# =============================================================================
# RUN EXAMPLES
# =============================================================================

if __name__ == "__main__":
    print("\n" + "="*60)
    print("API HANDLING DEMONSTRATION")
    print("="*60)
    
    # Quick demo
    print("\n1. Simple API request:")
    url = "https://jsonplaceholder.typicode.com/todos/1"
    try:
        with urlopen(url) as response:
            data = json.loads(response.read().decode('utf-8'))
            print(f"   Todo: {data['title']}")
            print(f"   Completed: {data['completed']}")
    except Exception as e:
        print(f"   Error: {e}")
    
    print("\n" + "="*60)