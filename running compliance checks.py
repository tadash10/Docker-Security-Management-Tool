def run_compliance_checks():
    command = "docker exec -it my_container /path/to/compliance_script.sh"
    result = subprocess.run(command, capture_output=True, text=True, shell=True)
    if result.returncode == 0:
        compliance_results = result.stdout.strip()
        print("Compliance check results:")
        print(compliance_results)
    else:
        print("Failed to run compliance checks.")
