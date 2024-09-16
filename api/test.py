from django.core.cache import cache

# Test cache set and get
cache.set('test_key', 'test_value', timeout=60)  # Set cache for 60 seconds
cached_value = cache.get('test_key')

if cached_value:
    print(f"Cache working, test_key: {cached_value}")
else:
    print("Cache not working")
