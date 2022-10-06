# MQTT Projects

Activate the virtual environment **venv** inside the project folder

`.\venv\Scripts\activate`

Install the necessary packages using

`pip install -r requirements.txt --upgrade`

## 01. Test publisher and subscriber

Project that creates an mqtt publisher client on the localhost, publishes some data on a topic, establishes connection with the client and subscribes the data from the topic.  

Open a shell a run  `python .\test_publisher.py`. If success, you'll see the following
```python
    Connected with result code 0
```
Open another shell and run `python .\test_subscriber.py`. If success, it displays the data every two seconds in the following format
```python
    Connected with result code 0
    test/temperature b'{"temp": 34.50818905180168}'
    test/temperature b'{"temp": 49.860567045131575}'
    test/temperature b'{"temp": 40.999546767349244}'
    test/temperature b'{"temp": 38.369234668449195}'
```


## 02. Alerting system based on inactivity
The idea of this project is to notify users in case something is inactive for a certain duration. If the user gets notified about the period of inactivity at predefined intervals rather than in a repeating fashion, then the user is not bombarded with notifications. For this example, lets say we have an elevator. If the elevator is working as usual, there is no need for repair. But if is inactive for an hour during the peak hours, something is wrong with it and it needs to be checked. We don't want to alert the technician every minute once this one hour window is surpassed. It would be wiser to notify the technician at user defined intervals lets say once after 45 minutes, 1 hour, 2 hours, 3 hours, etc of inactivity. The project addresses this scenario.
Open a shell a run  `python .\inactivity_publisher.py`. If success, it publishes the inactivity period in hours every 1/10 seconds
```python
    Connected with result code 0
    Publishing 0.0
    Publishing 0.016666666666666666
    Publishing 0.03333333333333333
    .
    .
    .    
    Publishing 10.15
```
The publisher exits once it has run over the default 10.15 hours of inactivity time. To run the subscriber, open another shell and run `python .\inactivity_subscriber.py`. The subscriber returns the following during the entire publishing cycle.
```python
    Connected with result code 0
    The elevator is inactive for the last 45.0 minutes
    The elevator is inactive for the last 1.0 hours
    The elevator is inactive for the last 2.0 hours
    The elevator is inactive for the last 3.0 hours
    The elevator is inactive for the last 4.0 hours
    The elevator is inactive for the last 8.0 hours
    The elevator is inactive for the last 10.0 hours
```
