#!/usr/bin/env python3

import re
def rearrange_name(name):
  result = re.search(r"^([\w \.-]*), ([\w \.-]*)$", name) #el resultado es una tupla
  if result == None:
    return name
  return "{} {}".format(result[2], result[1])