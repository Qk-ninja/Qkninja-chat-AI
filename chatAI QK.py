import openai_secret_manager

# Let's use the openai secret manager to get the API key
assert "openai" in openai_secret_manager.get_services()
secrets = openai_secret_manager.get_secrets("openai")

# Let's use the openai python sdk
import openai
openai.api_key = secrets["api_key"]

def generate_code(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )

    message = completions.choices[0].text
    return message.strip()

prompt = "Write a function that takes in a list of numbers and returns the sum of the list in python"
code = generate_code(prompt)
print(code)

resultWorkerErr := make(chan error)
defer close(resultWorkerErr)
go func() {
	defer cancel()
	resultWorkerErr <- b.resultWorker(ctx)
}()

err := b.worker(ctx)
cancel()
if err == nil {
	return <-resultWorkerErr
}
return multierror.Append(err, <-resultWorkerErr)

