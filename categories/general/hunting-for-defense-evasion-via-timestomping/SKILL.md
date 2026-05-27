---
name: hunting-for-defense-evasion-via-timestomping
description: "Detect NTFS timestamp manipulation (MITRE T1070.006) by comparing $STANDARD_INFORMATION vs $FILE_NAME timestamps in the MFT. Uses analyzeMFT and Python to identify files with anomalous temporal pat..."
license: MIT
tags: [timestomping, ntfs-forensics, mft-analysis, defense-evasion]
domain: cybersecurity
subdomain: threat-hunting
version: 1.0
author: mahipal
---

# Hunting for Defense Evasion via Timestomping

Detect timestamp manipulation by analyzing NTFS MFT entries for
discrepancies between $STANDARD_INFORMATION and $FILE_NAME attributes.