#  Desktop Reminder App (Python)

A simple Python-based **Desktop Reminder Application** that sends periodic system notifications to remind users to take breaks, stretch, and stay hydrated. This project demonstrates how to use Python for automation and desktop notifications.


##  Features

* Sends desktop notifications at regular intervals
* Helps maintain healthy work habits
* Runs continuously in the background
* Lightweight and easy to use
* Beginner-friendly Python code



##  Tech Stack

* **Python**
* **Plyer** (for cross-platform notifications)
* **Time Module**



##  Project Structure

```
reminder-app/
│
├── main.py        # Main application file
├── README.md      # Project documentation
```



##  Customization

### Change Reminder Interval

Modify the sleep time in `main.py`:

```python
time.sleep(60 * 60)  # 1 hour
```

Examples:

```python
time.sleep(30 * 60)  # 30 minutes
time.sleep(10 * 60)  # 10 minutes
```

### Change Notification Message

```python
message="Time to take a short break, stretch and drink water!"
```



##  Sample Notification

**Title:** Reminder
**Message:** Time to take a short break, stretch and drink water!



##  What I Learned

* Creating background scripts in Python
* Using `plyer` for system notifications
* Automating repetitive tasks
* Writing clean and maintainable code

