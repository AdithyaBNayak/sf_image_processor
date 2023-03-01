# Image Resizing using Step Functions

## Note

- Need to create S3 and Lambda Resource Permission first and only then add Notification Trigger for S3 bucket
  We get the following error if we done: 
  ``` 
  An error occurred: ImageProcessingSource - Unable to validate the following destination configurations (Service: Amazon S3; Status Code: 400; Error Code: InvalidArgument
  ```
  The reason being Circular Dependency. Amazon S3 must validate the notification configuration when it creates the bucket. The validation is done by checking if the bucket has permission to push events to the Lambda function. The permission resource (which must exist for this check to pass) requires the bucket name. This means that the permission resource depends on the bucket, and the bucket depends on the permission resource.
  Refer this [link](https://aws.amazon.com/premiumsupport/knowledge-center/unable-validate-circular-dependency-cloudformation/) to get a possible solution for this issue.
- Cannot provide Lambda role to start execution of state machine with other lambda roles..It will give us circular dependency due to which we have to create 2 roles separately.