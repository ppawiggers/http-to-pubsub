# http-to-pubsub
Send the headers and body of an HTTP request to a Pub/Sub topic with Google Cloud Functions.

## Deploying to Google Cloud Functions
```
gcloud beta functions deploy http-to-pubsub 
    --region=europe-west1
    --runtime=python37
    --entry-point=F
    --trigger-http
    --set-env-vars PUBSUB_TOPIC_PATH=[YOUR_PUBSUB_TOPIC_PATH]
```

It currently uses `gcloud beta` because setting environment variables via the CLI is not available in stable yet.

Make sure `YOUR_PUBSUB_TOPIC_PATH` exists.

## Test
```
curl \
    --request POST \
    --header "Content-Type: application/json" \
    --header "X-MyHeader: 123" \
    --data '{"foo": "bar"}' \
    [YOUR_CLOUD_FUNCTION_TRIGGER_URL]
```
