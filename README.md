# Image Resizing using Step Functions

## Note

- Need to create S3 and Lambda Resource Permission first and only then add Notification Trigger for S3 bucket
- Cannot provide Lambda role to start execution of state machine with other lambda roles..It will give us cirxular dependency due to which we have to create 2 roles separately.