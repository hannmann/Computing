# 4)
def has_experience_as(cv_list, job_title):
    return [cv['user'] for cv in cv_list if job_title in cv['jobs']]

# 5)
def job_counts(cv_list):
    job_count = {}
    for cv in cv_list:
        for job in cv['jobs']:
            if job in job_count:
                job_count[job] += 1
            else:
                job_count[job] = 1
    return job_count

# 6)
def most_popular_job(cv_list):
    job_count = job_counts(cv_list)
    return max(job_count.items(), key=lambda x: x[1])
