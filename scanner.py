# scanner.py
import subprocess

def scan_ports(target):
    command = f"nmap -sS -sV -A -T5 {target}"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout  # Nmap result

def run_osint(target):
    sherlock_results = run_sherlock(target)
    harvester_results = run_theharvester(target)
    return sherlock_results + "\n\n" + harvester_results

def run_nuclei(target):
    command = f"nuclei -u {target} -t root/.local/nuclei-templates"  # Replace with your Nuclei template path
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout  # Nuclei result

def run_sqlmap(target_url):
    command = f"sqlmap -u {target_url} --batch --crawl=3"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout  # SQLMap result

def run_sherlock(username):
    command = f"python3 sherlock/sherlock.py {username}"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout

def run_theharvester(target):
    command = f"python3 theHarvester/theHarvester.py -d {target} -b all"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout

def run_openvas(target):
    command = f"gvm-cli socket --xml='<get_reports report_id=\"target-report-id\"/>'"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout




if __name__ == '__main__':
    print(run_nuclei('example.com'))
