import runpod


def is_even(job):
    job_input = job["input"]
    job_id = job_input["job_id"]
    job_metadata = job_input["metadata"]

    prompt = job_input["prompt"]
    if prompt == "a resource that fails":
        return {
            "status": "failed",
            "duration": 1.8,
            "error_message": "you have entered (a resource that fails)",
            "job_id": job_id,
            "metadata": job_metadata,
        }

    return {
        "resource_url": "https://delivery.fanmade.ai/05_b2dd4b5c-c714-4e30-b980-01045e472fb1.png",
        "duration": 4.1,
        "job_id": job_id,
        "status": "completed",
        "metadata": job_metadata,
    }


runpod.serverless.start({"handler": is_even})
