from RatingsBreakdown import RatingsBreakdown
job=RatingsBreakdown(args=[args])
with job.make_runner() as runner:
    runner.run()