# proxy (server)
This folder contains the proxy server that forwards requests to OpenAI.
Set environment variable OPENAI_API_KEY in your hosting platform (Render, Railway, etc.).
Endpoints:
  POST /chat  -> accepts JSON {"message":"..."} and returns model response.
