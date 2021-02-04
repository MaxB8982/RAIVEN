def grade_url(url):
  if url.count(".blog/"):
    # .blog is here since it is intended for personal blogging, which usually isnt a good source
    return 2
  elif url.count(".com/" or ".net/" or ".io/"):
    # these TLDs are here since they are very generic and general use
    return 5
  elif url.count(".org/" or ".biz/"):
    # These TLDs are generally for businesses and sources, generally trustworthy in some to most scenerios
    return 8
  elif url.count(".edu/"):
    # .edu is pretty trustworthy, its also probably a bad idea to put the education TLD low for a school project haha
    return 9
  elif url.count(".gov/" or ".co/" or ".us/"):
    # This decision might be controversial, but I would say the government TLds are very trustworthy, though there may be exceptions in the future. Currently though, this is probably the best idea
    return 10
  else:
    return int(-1)
# If we want to add more TLDs (Top-level Domains) that can happen, this is just a basic set for now