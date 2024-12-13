import runpod


def is_even(job):
    job_input = job["input"]
    job_metadata = job_input.get("metadata")

    prompt = job_input["prompt"]
    if prompt == "a resource that fails":
        return {"error": "you have entered (a resource that fails)"}

    return {
        "resource_url": "https://delivery.fanmade.ai/05_b2dd4b5c-c714-4e30-b980-01045e472fb1.png",
        "duration": 4.1,
        "status": "completed",
        "metadata": job_metadata,
    }


runpod.serverless.start({"handler": is_even})
