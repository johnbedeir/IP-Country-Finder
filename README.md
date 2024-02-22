# IP Country Finder

<p align="center">
<img src=imgs/logo.png width=400px>
</p>
IP Country Finder is a Python application that identifies the country of origin for any given IP address. Using advanced geolocation services, it provides instant insights into the geographical distribution of web traffic. This tool is ideal for developers, researchers, and IT professionals needing to map IP addresses to their corresponding countries.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed on your system.
- The `requests` library installed. If you haven't installed it yet, you can do so by running

```
pip3 install requests
```

## How to Run

1. Clone the repository or download the source code to your local machine.

   ```
   git clone https://github.com/your-username/IPCountryFinder.git
   ```

2. Navigate to the directory containing the application.

   ```
   cd IP-Country-Finder
   ```

3. Make sure you add the list of IPs you need to check in `ips.txt` file.

<p align="center">
   <img src=imgs/ips.png width=300px>
</p>

4. Run the script.

   ```
   python3 app.py
   ```

<p align="center">
   <img src=imgs/output.png width=500px>
</p>

### Saving Results to a File

To save the output of IP-Country-Finder to a file, you can use the redirection operator `>` in your command line. For example, to save the output to a file named `output.txt`, you can run:

```
python3 app.py > output.txt
```

This command will execute the application and save the results in `output.txt`, located in the same directory as your command prompt or terminal window.
