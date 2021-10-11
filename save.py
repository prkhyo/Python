

import csv  # 파이썬에서 제공

def save_to_file(jobs):

  file = open("jobs.csv", mode ="w")
  writer = csv.writer(file)
  writer.writerow(['title', 'company', 'location', 'link'])
  for job in jobs:
    writer.writerow(list(job.values()))





