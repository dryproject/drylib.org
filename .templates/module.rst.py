import os

def filter_basename(s):
    return os.path.basename(s)

FILTERS = {
    'basename': filter_basename,
}
