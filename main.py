import runpod


def is_even(job):
    job_input = job["input"]

    prompt = job_input["prompt"]
    if prompt == "a resource that fails":
        return {"error": "you have entered (a resource that fails)"}

    return {
        "resource_url": "https://delivery.fanmade.ai/05_b2dd4b5c-c714-4e30-b980-01045e472fb1.png",
        "nsfw": False,
    }


runpod.serverless.start({"handler": is_even})
