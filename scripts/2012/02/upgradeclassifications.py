#!/usr/bin/env python

from olapi import OpenLibrary

ol = OpenLibrary()
ol.login("VacuumBot", "somePassword")

# Top level classifications don't go in the classifications dict.
tl_classifications = ["lc_classifications","dewey_decimal_class"]

def upgrade_classifications(olid):
  """Changes classification from list of (name,value)-dict
  to dict of lists.
  """
  record = ol.get(olid)
  # Check if the classifications are a list:
  if not isinstance(record["classifications"], list):
    return
  
  # Create a new dict to replace the list:
  c = {}
  
  # Read the dicts from the classifications list:
  for k in record["classifications"]:
    if k["name"] in tl_classifications:
      if k["name"] in record.keys():
        record[k["name"]].append(k["value"])
      else:
        record[k["name"]] = [k["value"]]
    elif k["name"] not in c.keys():
      c["name"] = [k["value"]]
    else:
      c["name"].append(k["value"])
  
  # If the dict is empty, there were only top level classifications
  if len(c) > 0:
    record["classifications"] = c
  else:
    del record["classifications"]
  
  ol.save(olid, record, "Upgraded classification list to dict")

def load(file):
  for line in open(file):
    olid, reason = line.strip().split()
    upgrade_classifications(olid)

if __name__ == "__main__":
  import sys
  load(sys.argv[1])