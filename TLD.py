def grade_url(url):
  if url.count(".com/"):
    return 3
  elif url.count(".org/"):
    return 5
  elif url.count(".edu/"):
    return 8
  elif url.count(".gov/"):
    return 10
  else:
    return int(-1)
# If we want to add more TLDs (Top-level Domains) that can happen, this is just a basic set for now
