How to setup:

1. Install mysql and set up your usernames and passwords DO NOT FORGET YOUR PASSWORD as you will need it.
3. In your python application, create a .env file that has this:  <br> <br>
    HOST=localhost <br>
    PASSWORD=your password goes here <br>
    USER=root <br>
    DB=banking_system <br>
<br>
<b> IMPORTANT!!!! <b>

Usually, we should NOT be exposing credentials like this due to security reasons. However, since this is just a local project there should not be any risk.
If we end up using a database in the cloud we will have to provide those variables above to connect to it. If that happens, then we should definetely not expose credentials.
