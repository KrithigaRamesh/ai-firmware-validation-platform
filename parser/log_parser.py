import re
import pandas as pd

log_file = "C:/Users/Dines/OneDrive/Documents/firmware-ai-lab/logs/device_log.txt"

data = []

with open(log_file, "r") as file:
    for line in file:

        temp = re.search(r"TEMP:(\d+)", line)
        volt = re.search(r"VOLT:(\d+\.\d+)", line)
        status = re.search(r"STATUS:(\w+)", line)

        if temp and volt and status:
            data.append({
                "temperature": int(temp.group(1)),
                "voltage": float(volt.group(1)),
                "status": status.group(1)
            })

df = pd.DataFrame(data)

print(df)

print("\nFirmware Test Summary")
high_temp = df[df["temperature"] > 45]
critical = df[df["status"] == "CRITICAL"]

print("\nHigh Temperature Entries:")
print(high_temp)
print("\nCritical Status Entries:")
print(critical)

print("High temperature events:", len(high_temp))
print("Critical failures:", len(critical))
df.to_csv("C:/Users/Dines/OneDrive/Documents/firmware-ai-lab/output/parsed_results.csv", index=False)