"""
================================================================================
PYTHON FUNDAMENTALS: THE DATETIME MODULE
================================================================================
Day: 11

Description:
    Complete guide to Python's datetime module for date and time manipulation.
    Covers date/time creation, arithmetic, formatting, parsing, timezones,
    and practical patterns essential for logging, scheduling, and data analysis.

Learning Objectives:
    - Create and manipulate date and time objects
    - Perform date/time arithmetic with timedelta
    - Format dates for display (strftime)
    - Parse date strings into datetime objects (strptime)
    - Work with timezones using pytz
    - Handle timestamps and epoch time
    - Apply datetime in ML/AI workflows

Prerequisites:
    - Basic Python syntax
    - Imports and modules (Day 5)
================================================================================
"""

import datetime
import time

# =============================================================================
# 1. WHAT IS THE DATETIME MODULE?
# =============================================================================

"""
The datetime module provides classes for manipulating dates and times.

Why is it important for AI/ML?
- Timestamping model training runs and experiments
- Time-series data analysis and feature engineering
- Log file processing and analysis
- Scheduling automated training jobs
- Data versioning and tracking

Main classes:
- datetime.date: Date (year, month, day)
- datetime.time: Time (hour, minute, second, microsecond)
- datetime.datetime: Combined date and time
- datetime.timedelta: Duration between two dates/times
- datetime.timezone: Timezone information
"""


# =============================================================================
# 2. DATE OBJECTS (datetime.date)
# =============================================================================

# --- Create a specific date ---
d = datetime.date(2016, 7, 24)  # year, month, day
print(f"Date: {d}")
# Output: Date: 2016-07-24

# --- Get today's date ---
today = datetime.date.today()
print(f"Today: {today}")
# Output: Today: 2024-12-17

# --- Access individual components ---
print(f"Year: {today.year}")
print(f"Month: {today.month}")
print(f"Day: {today.day}")

# --- Get day of week ---
print(f"Weekday (0=Mon): {today.weekday()}")    # Monday = 0
print(f"ISO Weekday (1=Mon): {today.isoweekday()}")  # Monday = 1

# --- Get day name ---
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 
        'Friday', 'Saturday', 'Sunday']
print(f"Day name: {days[today.weekday()]}")

# --- Create from timestamp ---
timestamp = time.time()  # Current Unix timestamp
date_from_ts = datetime.date.fromtimestamp(timestamp)
print(f"From timestamp: {date_from_ts}")

# --- Create from ISO format string ---
date_from_iso = datetime.date.fromisoformat("2024-12-25")
print(f"From ISO: {date_from_iso}")

# --- Get ISO calendar (year, week number, weekday) ---
iso_cal = today.isocalendar()
print(f"ISO Calendar: Year {iso_cal[0]}, Week {iso_cal[1]}, Day {iso_cal[2]}")


# =============================================================================
# 3. TIME OBJECTS (datetime.time)
# =============================================================================

# --- Create a specific time ---
t = datetime.time(12, 30, 45, 100000)  # hour, min, sec, microsec
print(f"Time: {t}")
# Output: Time: 12:30:45.100000

# --- Create simple time ---
t_simple = datetime.time(9, 30)
print(f"Simple time: {t_simple}")
# Output: Simple time: 09:30:00

# --- Access components ---
print(f"Hour: {t.hour}")
print(f"Minute: {t.minute}")
print(f"Second: {t.second}")
print(f"Microsecond: {t.microsecond}")

# --- Min and max time ---
print(f"Min time: {datetime.time.min}")  # 00:00:00
print(f"Max time: {datetime.time.max}")  # 23:59:59.999999

# --- Create from ISO format ---
time_from_iso = datetime.time.fromisoformat("14:30:00")
print(f"From ISO: {time_from_iso}")


# =============================================================================
# 4. DATETIME OBJECTS (datetime.datetime)
# =============================================================================

# --- Create specific datetime ---
dt = datetime.datetime(2016, 7, 26, 12, 30, 45, 10000)
print(f"DateTime: {dt}")
# Output: DateTime: 2016-07-26 12:30:45.010000

# --- Extract date and time parts ---
print(f"Date part: {dt.date()}")
print(f"Time part: {dt.time()}")

# --- Access all components ---
print(f"Year: {dt.year}, Month: {dt.month}, Day: {dt.day}")
print(f"Hour: {dt.hour}, Minute: {dt.minute}, Second: {dt.second}")

# --- Current datetime options ---
dt_today = datetime.datetime.today()      # Local, no timezone
dt_now = datetime.datetime.now()          # Local, optional timezone
dt_utcnow = datetime.datetime.now(datetime.timezone.utc)  # UTC aware

print(f"today(): {dt_today}")
print(f"now(): {dt_now}")
print(f"now(utc): {dt_utcnow}")

"""
Difference between today() and now():
- today(): Returns local datetime, cannot specify timezone
- now(): Returns local datetime, CAN specify timezone
- Always prefer now() with timezone for clarity
"""

# --- Create from timestamp ---
ts = time.time()
dt_from_ts = datetime.datetime.fromtimestamp(ts)
print(f"From timestamp: {dt_from_ts}")

# UTC from timestamp
dt_utc_from_ts = datetime.datetime.fromtimestamp(ts, tz=datetime.timezone.utc)
print(f"UTC from timestamp: {dt_utc_from_ts}")

# --- Create from date and time objects ---
d = datetime.date(2024, 12, 25)
t = datetime.time(10, 30)
dt_combined = datetime.datetime.combine(d, t)
print(f"Combined: {dt_combined}")

# --- Create from ISO format ---
dt_from_iso = datetime.datetime.fromisoformat("2024-12-25T10:30:00")
print(f"From ISO: {dt_from_iso}")


# =============================================================================
# 5. TIMEDELTA - DATE/TIME ARITHMETIC
# =============================================================================

"""
timedelta represents a duration - the difference between two dates/times.
Essential for:
- Calculating age of files/data
- Setting expiration times
- Time-series windowing
- Scheduling future events
"""

# --- Create timedelta ---
tdelta = datetime.timedelta(days=7)
print(f"One week: {tdelta}")

# Full constructor
tdelta_full = datetime.timedelta(
    weeks=1,
    days=2,
    hours=3,
    minutes=30,
    seconds=45,
    milliseconds=100,
    microseconds=50
)
print(f"Full timedelta: {tdelta_full}")

# --- Date arithmetic ---
today = datetime.date.today()
one_week = datetime.timedelta(days=7)

next_week = today + one_week
last_week = today - one_week
print(f"Today: {today}")
print(f"Next week: {next_week}")
print(f"Last week: {last_week}")

# --- Calculate difference between dates ---
bday = datetime.date(2025, 9, 24)
till_bday = bday - today
print(f"Days until birthday: {till_bday.days}")
print(f"Seconds until birthday: {till_bday.total_seconds()}")

# --- DateTime arithmetic ---
now = datetime.datetime.now()
future = now + datetime.timedelta(hours=5, minutes=30)
print(f"Now: {now}")
print(f"In 5.5 hours: {future}")

# --- Difference between datetimes ---
start = datetime.datetime(2024, 1, 1, 0, 0, 0)
end = datetime.datetime(2024, 12, 31, 23, 59, 59)
duration = end - start
print(f"Year duration: {duration}")
print(f"Total days: {duration.days}")
print(f"Total seconds: {duration.total_seconds()}")

# --- Timedelta components ---
td = datetime.timedelta(days=5, hours=3, minutes=30, seconds=45)
print(f"Days: {td.days}")
print(f"Seconds (remainder): {td.seconds}")  # Only seconds part
print(f"Total seconds: {td.total_seconds()}")  # Everything in seconds

# --- Multiply and divide timedeltas ---
one_hour = datetime.timedelta(hours=1)
three_hours = one_hour * 3
half_hour = one_hour / 2
print(f"Three hours: {three_hours}")
print(f"Half hour: {half_hour}")

# --- Practical: Age calculator ---
def calculate_age(birthdate):
    """Calculate age in years from birthdate"""
    today = datetime.date.today()
    age = today.year - birthdate.year
    # Adjust if birthday hasn't occurred this year
    if (today.month, today.day) < (birthdate.month, birthdate.day):
        age -= 1
    return age

birth = datetime.date(1995, 5, 15)
print(f"Age: {calculate_age(birth)} years")


# =============================================================================
# 6. FORMATTING DATES - strftime()
# =============================================================================

"""
strftime = "string format time"
Converts datetime to formatted string for display.
"""

now = datetime.datetime.now()

# --- Common format codes ---
print(f"Full: {now.strftime('%Y-%m-%d %H:%M:%S')}")
# Output: 2024-12-17 14:30:45

print(f"Date only: {now.strftime('%Y-%m-%d')}")
# Output: 2024-12-17

print(f"Time only: {now.strftime('%H:%M:%S')}")
# Output: 14:30:45

print(f"Human readable: {now.strftime('%B %d, %Y')}")
# Output: December 17, 2024

print(f"With day: {now.strftime('%A, %B %d, %Y')}")
# Output: Tuesday, December 17, 2024

print(f"12-hour: {now.strftime('%I:%M %p')}")
# Output: 02:30 PM

print(f"ISO format: {now.strftime('%Y-%m-%dT%H:%M:%S')}")
# Output: 2024-12-17T14:30:45

# --- Format Code Reference ---
"""
DATE CODES:
%Y - Year with century (2024)
%y - Year without century (24)
%m - Month as zero-padded number (01-12)
%B - Full month name (December)
%b - Abbreviated month (Dec)
%d - Day of month zero-padded (01-31)
%j - Day of year (001-366)

TIME CODES:
%H - Hour 24-hour zero-padded (00-23)
%I - Hour 12-hour zero-padded (01-12)
%M - Minute zero-padded (00-59)
%S - Second zero-padded (00-59)
%f - Microsecond (000000-999999)
%p - AM/PM

WEEKDAY CODES:
%A - Full weekday (Monday)
%a - Abbreviated weekday (Mon)
%w - Weekday as number (0=Sunday, 6=Saturday)
%u - ISO weekday (1=Monday, 7=Sunday)

WEEK CODES:
%U - Week number (Sunday first) (00-53)
%W - Week number (Monday first) (00-53)

OTHER:
%Z - Timezone name
%z - UTC offset (+0000)
%% - Literal %
"""

# --- ML/AI common formats ---
# Model checkpoint naming
checkpoint_name = now.strftime("model_%Y%m%d_%H%M%S.h5")
print(f"Checkpoint: {checkpoint_name}")
# Output: model_20241217_143045.h5

# Log file naming
log_name = now.strftime("training_%Y-%m-%d.log")
print(f"Log file: {log_name}")

# Experiment ID
exp_id = now.strftime("exp_%Y%m%d%H%M%S")
print(f"Experiment ID: {exp_id}")


# =============================================================================
# 7. PARSING DATES - strptime()
# =============================================================================

"""
strptime = "string parse time"
Converts string to datetime object.
Essential for reading dates from files, APIs, user input.
"""

# --- Basic parsing ---
dt_str = 'July 26, 2016'
dt = datetime.datetime.strptime(dt_str, '%B %d, %Y')
print(f"Parsed: {dt}")
# Output: Parsed: 2016-07-26 00:00:00

# --- Common formats to parse ---
# ISO format
iso_str = "2024-12-17T14:30:45"
dt_iso = datetime.datetime.strptime(iso_str, '%Y-%m-%dT%H:%M:%S')
print(f"ISO parsed: {dt_iso}")

# US format
us_str = "12/17/2024"
dt_us = datetime.datetime.strptime(us_str, '%m/%d/%Y')
print(f"US parsed: {dt_us}")

# European format
eu_str = "17-12-2024"
dt_eu = datetime.datetime.strptime(eu_str, '%d-%m-%Y')
print(f"EU parsed: {dt_eu}")

# With time
full_str = "2024-12-17 14:30:45"
dt_full = datetime.datetime.strptime(full_str, '%Y-%m-%d %H:%M:%S')
print(f"Full parsed: {dt_full}")

# Log format
log_str = "Dec 17 14:30:45 2024"
dt_log = datetime.datetime.strptime(log_str, '%b %d %H:%M:%S %Y')
print(f"Log parsed: {dt_log}")

# --- Safe parsing with error handling ---
def parse_date(date_string, formats=None):
    """Try multiple formats to parse a date string"""
    if formats is None:
        formats = [
            '%Y-%m-%d',
            '%Y-%m-%d %H:%M:%S',
            '%Y-%m-%dT%H:%M:%S',
            '%d/%m/%Y',
            '%m/%d/%Y',
            '%B %d, %Y',
            '%d-%b-%Y',
        ]
    
    for fmt in formats:
        try:
            return datetime.datetime.strptime(date_string, fmt)
        except ValueError:
            continue
    
    raise ValueError(f"Unable to parse date: {date_string}")

# Test flexible parsing
print(parse_date("2024-12-17"))
print(parse_date("December 17, 2024"))
print(parse_date("17/12/2024"))


# =============================================================================
# 8. TIMEZONES WITH PYTZ
# =============================================================================

"""
Timezone handling is CRITICAL for:
- Distributed ML training across regions
- Log correlation from multiple servers
- API timestamp normalization
- Scheduling jobs globally

Install: pip install pytz
"""

try:
    import pytz
    PYTZ_AVAILABLE = True
except ImportError:
    PYTZ_AVAILABLE = False
    print("pytz not installed. Run: pip install pytz")

if PYTZ_AVAILABLE:
    # --- Naive vs Aware datetimes ---
    """
    Naive: No timezone info (dangerous for comparisons!)
    Aware: Has timezone info (always prefer this)
    """
    
    naive_dt = datetime.datetime.now()
    print(f"Naive (no tz): {naive_dt}")
    print(f"Has timezone? {naive_dt.tzinfo}")
    # Output: None
    
    # --- Create timezone-aware datetime ---
    # Method 1: Create with UTC
    dt_utc = datetime.datetime(2024, 7, 27, 12, 30, 45, tzinfo=pytz.UTC)
    print(f"UTC aware: {dt_utc}")
    
    # Method 2: Localize existing datetime (RECOMMENDED)
    dt_naive = datetime.datetime.now()
    mtn_tz = pytz.timezone('US/Mountain')
    dt_mtn = mtn_tz.localize(dt_naive)
    print(f"Mountain time: {dt_mtn}")
    
    # --- Convert between timezones ---
    dt_east = dt_mtn.astimezone(pytz.timezone("US/Eastern"))
    print(f"Eastern time: {dt_east}")
    
    dt_utc = dt_mtn.astimezone(pytz.UTC)
    print(f"UTC: {dt_utc}")
    
    dt_london = dt_mtn.astimezone(pytz.timezone("Europe/London"))
    print(f"London: {dt_london}")
    
    dt_tokyo = dt_mtn.astimezone(pytz.timezone("Asia/Tokyo"))
    print(f"Tokyo: {dt_tokyo}")
    
    # --- ISO format with timezone ---
    print(f"ISO format: {dt_mtn.isoformat()}")
    # Output: 2024-12-17T14:30:45.123456-07:00
    
    # --- List available timezones ---
    # for tz in pytz.all_timezones:
    #     print(tz)
    
    # Common timezones
    common_tzs = [
        'US/Eastern', 'US/Central', 'US/Mountain', 'US/Pacific',
        'Europe/London', 'Europe/Paris', 'Europe/Berlin',
        'Asia/Tokyo', 'Asia/Shanghai', 'Asia/Kolkata',
        'Australia/Sydney', 'UTC'
    ]
    print(f"\nCommon timezones: {common_tzs[:5]}...")
    
    # --- Best practice: Always work in UTC internally ---
    def get_utc_now():
        """Get current time in UTC (always use this!)"""
        return datetime.datetime.now(pytz.UTC)
    
    def to_local(utc_dt, timezone_str):
        """Convert UTC datetime to local timezone"""
        local_tz = pytz.timezone(timezone_str)
        return utc_dt.astimezone(local_tz)
    
    utc_now = get_utc_now()
    local_times = {
        'UTC': utc_now,
        'New York': to_local(utc_now, 'US/Eastern'),
        'London': to_local(utc_now, 'Europe/London'),
        'Tokyo': to_local(utc_now, 'Asia/Tokyo'),
    }
    
    print("\nCurrent time around the world:")
    for city, dt in local_times.items():
        print(f"  {city}: {dt.strftime('%Y-%m-%d %H:%M:%S %Z')}")


# =============================================================================
# 9. TIMESTAMPS AND EPOCH TIME
# =============================================================================

"""
Unix timestamp = seconds since January 1, 1970 (epoch)
Common in APIs, databases, and log files.
"""

# --- Current timestamp ---
current_ts = time.time()
print(f"Current timestamp: {current_ts}")
# Output: 1702834245.123456

# --- Convert datetime to timestamp ---
dt = datetime.datetime.now()
ts = dt.timestamp()
print(f"DateTime to timestamp: {ts}")

# --- Convert timestamp to datetime ---
ts = 1702834245
dt_from_ts = datetime.datetime.fromtimestamp(ts)
print(f"Timestamp to datetime: {dt_from_ts}")

# UTC from timestamp (recommended)
dt_utc = datetime.datetime.fromtimestamp(ts, tz=datetime.timezone.utc)
print(f"Timestamp to UTC: {dt_utc}")

# --- Millisecond timestamps (common in JS/APIs) ---
ms_timestamp = 1702834245123
dt_from_ms = datetime.datetime.fromtimestamp(ms_timestamp / 1000)
print(f"Millisecond timestamp: {dt_from_ms}")

# --- Epoch reference ---
epoch = datetime.datetime(1970, 1, 1, tzinfo=datetime.timezone.utc)
print(f"Epoch: {epoch}")


# =============================================================================
# 10. PRACTICAL ML/AI UTILITIES
# =============================================================================

class Timer:
    """Context manager for timing code blocks"""
    
    def __init__(self, name="Timer"):
        self.name = name
        self.start = None
        self.end = None
        self.duration = None
    
    def __enter__(self):
        self.start = datetime.datetime.now()
        return self
    
    def __exit__(self, *args):
        self.end = datetime.datetime.now()
        self.duration = self.end - self.start
        print(f"{self.name}: {self.duration.total_seconds():.4f} seconds")

# Usage:
# with Timer("Model Training"):
#     train_model()


def get_experiment_id():
    """Generate unique experiment ID from timestamp"""
    return datetime.datetime.now().strftime("exp_%Y%m%d_%H%M%S")


def get_checkpoint_path(base_dir, model_name, epoch=None):
    """Generate timestamped checkpoint path"""
    import os
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    if epoch is not None:
        filename = f"{model_name}_epoch{epoch:03d}_{timestamp}.h5"
    else:
        filename = f"{model_name}_{timestamp}.h5"
    return os.path.join(base_dir, filename)


def parse_log_timestamp(log_line, format_str='%Y-%m-%d %H:%M:%S'):
    """Extract timestamp from log line"""
    # Assumes timestamp is at start of line
    try:
        ts_str = log_line[:19]  # Typical timestamp length
        return datetime.datetime.strptime(ts_str, format_str)
    except ValueError:
        return None


def time_since(start_time):
    """Human-readable time since start"""
    delta = datetime.datetime.now() - start_time
    total_seconds = int(delta.total_seconds())
    
    if total_seconds < 60:
        return f"{total_seconds}s"
    elif total_seconds < 3600:
        minutes = total_seconds // 60
        seconds = total_seconds % 60
        return f"{minutes}m {seconds}s"
    else:
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        return f"{hours}h {minutes}m"


def create_date_range(start, end, step_days=1):
    """Generate list of dates between start and end"""
    dates = []
    current = start
    step = datetime.timedelta(days=step_days)
    while current <= end:
        dates.append(current)
        current += step
    return dates


def get_week_boundaries(date=None):
    """Get start (Monday) and end (Sunday) of week for given date"""
    if date is None:
        date = datetime.date.today()
    start = date - datetime.timedelta(days=date.weekday())
    end = start + datetime.timedelta(days=6)
    return start, end


def get_month_boundaries(year, month):
    """Get first and last day of month"""
    import calendar
    first_day = datetime.date(year, month, 1)
    last_day = datetime.date(year, month, calendar.monthrange(year, month)[1])
    return first_day, last_day


class ExperimentLogger:
    """Log experiment timing and metadata"""
    
    def __init__(self, experiment_name=None):
        self.experiment_id = experiment_name or get_experiment_id()
        self.start_time = datetime.datetime.now()
        self.checkpoints = []
        self.metrics = {}
    
    def checkpoint(self, name):
        """Record a checkpoint"""
        self.checkpoints.append({
            'name': name,
            'time': datetime.datetime.now(),
            'elapsed': time_since(self.start_time)
        })
        print(f"[{self.experiment_id}] Checkpoint '{name}': {self.checkpoints[-1]['elapsed']}")
    
    def log_metric(self, name, value):
        """Log a metric with timestamp"""
        if name not in self.metrics:
            self.metrics[name] = []
        self.metrics[name].append({
            'value': value,
            'time': datetime.datetime.now()
        })
    
    def summary(self):
        """Print experiment summary"""
        duration = datetime.datetime.now() - self.start_time
        print(f"\n{'='*50}")
        print(f"Experiment: {self.experiment_id}")
        print(f"Duration: {time_since(self.start_time)}")
        print(f"Checkpoints: {len(self.checkpoints)}")
        print(f"{'='*50}")


# =============================================================================
# KEY TAKEAWAYS
# =============================================================================
"""
1. Date/Time Creation
   - datetime.date(year, month, day)
   - datetime.time(hour, minute, second)
   - datetime.datetime(year, month, day, hour, minute, second)
   - .today(), .now(), .now(timezone.utc)

2. Timedelta Arithmetic
   - timedelta(days, hours, minutes, seconds)
   - date + timedelta = date
   - date - date = timedelta
   - .total_seconds() for calculations

3. Formatting (strftime)
   - %Y-%m-%d for dates
   - %H:%M:%S for times
   - %B %d, %Y for human-readable

4. Parsing (strptime)
   - Match format exactly
   - Handle multiple formats gracefully
   - Always validate user input

5. Timezones (pytz)
   - Use aware datetimes (with timezone)
   - Store in UTC, display in local
   - localize() naive datetimes
   - astimezone() to convert

6. Best Practices
   - Always use UTC internally
   - Store timestamps, not formatted strings
   - Use ISO format for interchange
   - Handle timezone-naive data carefully
"""


# =============================================================================
# PRACTICE EXERCISES
# =============================================================================

# Exercise 1: Age Calculator [EASY]
# Create function that takes birthdate string "YYYY-MM-DD"
# Returns age in years, months, and days
# TODO: Write your code here

# Solution:
# def detailed_age(birthdate_str):
#     birth = datetime.datetime.strptime(birthdate_str, '%Y-%m-%d').date()
#     today = datetime.date.today()
#     
#     years = today.year - birth.year
#     months = today.month - birth.month
#     days = today.day - birth.day
#     
#     if days < 0:
#         months -= 1
#         days += 30
#     if months < 0:
#         years -= 1
#         months += 12
#     
#     return f"{years} years, {months} months, {days} days"
# print(detailed_age("1995-05-15"))


# Exercise 2: Meeting Scheduler [EASY]
# Create function that adds business days (skip weekends) to a date
# TODO: Write your code here

# Solution:
# def add_business_days(start_date, num_days):
#     current = start_date
#     added = 0
#     while added < num_days:
#         current += datetime.timedelta(days=1)
#         if current.weekday() < 5:  # Mon-Fri
#             added += 1
#     return current
# today = datetime.date.today()
# print(f"5 business days from today: {add_business_days(today, 5)}")


# Exercise 3: Log File Parser [MEDIUM]
# Parse log entries with format: "2024-12-17 14:30:45 [INFO] Message"
# Return list of (datetime, level, message) tuples
# TODO: Write your code here

# Solution:
# def parse_log_entries(log_lines):
#     entries = []
#     for line in log_lines:
#         try:
#             ts_str = line[:19]
#             dt = datetime.datetime.strptime(ts_str, '%Y-%m-%d %H:%M:%S')
#             rest = line[20:].strip()
#             level = rest[1:rest.index(']')]
#             message = rest[rest.index(']')+2:]
#             entries.append((dt, level, message))
#         except:
#             continue
#     return entries


# Exercise 4: Time Zone Converter [MEDIUM]
# Create function that converts time between any two timezones
# Input: time string, source tz, target tz
# TODO: Write your code here

# Solution:
# def convert_timezone(time_str, from_tz, to_tz, fmt='%Y-%m-%d %H:%M:%S'):
#     import pytz
#     dt_naive = datetime.datetime.strptime(time_str, fmt)
#     source = pytz.timezone(from_tz)
#     target = pytz.timezone(to_tz)
#     dt_source = source.localize(dt_naive)
#     dt_target = dt_source.astimezone(target)
#     return dt_target.strftime(fmt + ' %Z')
# print(convert_timezone("2024-12-17 09:00:00", "US/Pacific", "Europe/London"))


# Exercise 5: Duration Formatter [MEDIUM]
# Format timedelta as human readable: "2 days, 3 hours, 45 minutes"
# TODO: Write your code here

# Solution:
# def format_duration(td):
#     total = int(td.total_seconds())
#     days, remainder = divmod(total, 86400)
#     hours, remainder = divmod(remainder, 3600)
#     minutes, seconds = divmod(remainder, 60)
#     
#     parts = []
#     if days: parts.append(f"{days} day{'s' if days != 1 else ''}")
#     if hours: parts.append(f"{hours} hour{'s' if hours != 1 else ''}")
#     if minutes: parts.append(f"{minutes} minute{'s' if minutes != 1 else ''}")
#     if seconds: parts.append(f"{seconds} second{'s' if seconds != 1 else ''}")
#     
#     return ", ".join(parts) if parts else "0 seconds"


# Exercise 6: Date Range Generator [CHALLENGE]
# Create generator for date ranges with custom frequency
# Support: daily, weekly, monthly
# TODO: Write your code here

# Solution:
# def date_range(start, end, freq='daily'):
#     current = start
#     while current <= end:
#         yield current
#         if freq == 'daily':
#             current += datetime.timedelta(days=1)
#         elif freq == 'weekly':
#             current += datetime.timedelta(weeks=1)
#         elif freq == 'monthly':
#             month = current.month + 1
#             year = current.year
#             if month > 12:
#                 month = 1
#                 year += 1
#             day = min(current.day, calendar.monthrange(year, month)[1])
#             current = datetime.date(year, month, day)


# Exercise 7: Training Time Estimator [CHALLENGE]
# Based on time per epoch, estimate remaining time and ETA
# TODO: Write your code here

# Solution:
# class TrainingEstimator:
#     def __init__(self, total_epochs):
#         self.total = total_epochs
#         self.start_time = None
#         self.epoch_times = []
#     
#     def start(self):
#         self.start_time = datetime.datetime.now()
#     
#     def epoch_complete(self, epoch):
#         now = datetime.datetime.now()
#         self.epoch_times.append(now)
#         
#         avg_time = (now - self.start_time).total_seconds() / epoch
#         remaining = (self.total - epoch) * avg_time
#         eta = now + datetime.timedelta(seconds=remaining)
#         
#         return {
#             'epoch': epoch,
#             'elapsed': time_since(self.start_time),
#             'remaining': format_duration(datetime.timedelta(seconds=remaining)),
#             'eta': eta.strftime('%H:%M:%S')
#         }


# =============================================================================
# COMMON MISTAKES TO AVOID
# =============================================================================
"""
1. Using naive datetimes for comparisons
   ❌ dt1 = datetime.now(); dt2 = datetime.utcnow()  # Can't compare!
   ✅ dt1 = datetime.now(pytz.UTC); dt2 = datetime.now(pytz.UTC)

2. Wrong strptime/strftime format
   ❌ strptime("2024-12-17", "%Y/%m/%d")  # Wrong separator
   ✅ strptime("2024-12-17", "%Y-%m-%d")

3. Confusing strftime and strptime
   - strftime: datetime -> string (format)
   - strptime: string -> datetime (parse)

4. Not handling timezone conversions properly
   ❌ dt.replace(tzinfo=pytz.timezone('US/Eastern'))  # Wrong!
   ✅ pytz.timezone('US/Eastern').localize(dt)

5. Using today() instead of now() for timestamps
   ❌ datetime.datetime.today()  # No timezone support
   ✅ datetime.datetime.now(pytz.UTC)

6. Forgetting timedelta is immutable
   ❌ td.days = 5  # Can't modify
   ✅ td = datetime.timedelta(days=5)  # Create new

7. Integer division with timestamps
   ❌ ms_timestamp / 1000  # Python 2 issue
   ✅ ms_timestamp / 1000.0  # Explicit float

8. Assuming month lengths
   ❌ next_month = date + timedelta(days=30)
   ✅ Use calendar.monthrange() or dateutil
"""


# =============================================================================
# RUN EXAMPLES
# =============================================================================

if __name__ == "__main__":
    print("\n" + "="*60)
    print("DATETIME MODULE DEMONSTRATION")
    print("="*60)
    
    # Current date and time
    now = datetime.datetime.now()
    print(f"\n1. Current datetime: {now}")
    print(f"2. Formatted: {now.strftime('%B %d, %Y at %I:%M %p')}")
    
    # Date arithmetic
    next_week = now + datetime.timedelta(weeks=1)
    print(f"3. One week from now: {next_week.strftime('%Y-%m-%d')}")
    
    # Parse a date
    parsed = datetime.datetime.strptime("December 25, 2024", "%B %d, %Y")
    days_until = (parsed.date() - now.date()).days
    print(f"4. Days until Christmas: {days_until}")
    
    # Timestamp
    print(f"5. Current timestamp: {now.timestamp():.0f}")
    
    # Timer demo
    print("\n6. Timer demo:")
    with Timer("Quick operation"):
        sum(range(1000000))
    
    print("\n" + "="*60)
    print("Run the exercises to practice!")
    print("="*60)