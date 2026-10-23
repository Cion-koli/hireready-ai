"""
Cybersecurity Analyst Question Bank - 25 distinct technical questions.
Covers network security, OWASP top 10 vulnerabilities, cryptography, IAM & authentication, incident response, SIEM log analysis, and threat intelligence.
"""

CYBERSECURITY_ANALYST_QUESTIONS = [
    {
        "role": "Cybersecurity Analyst",
        "technology": "cybersecurity",
        "category": "owasp_top_10",
        "difficulty": "medium",
        "question_text": "Explain Server-Side Request Forgery (SSRF). How can an attacker exploit SSRF against an AWS cloud environment to steal IAM role credentials via the metadata service?",
        "expected_answer": "SSRF occurs when a vulnerable web application accepts a user-supplied URL and makes an HTTP request on behalf of the server without adequate validation. In cloud environments like AWS, an attacker submits the instance metadata service IP (http://169.254.169.254/latest/meta-data/iam/security-credentials/). If the app fetches it, the attacker receives temporary STS credentials. Mitigation: enforce IMDSv2 (requires session token via PUT request) and URL whitelist filtering.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How does IMDSv2 mitigate SSRF attacks using session tokens and hop limits?",
        "code_snippet": "# Vulnerable endpoint fetching user image:\n@app.route('/fetch-avatar')\ndef fetch_avatar():\n    url = request.args.get('url')\n    return requests.get(url).content  # Vulnerable to SSRF!"
    },
    {
        "role": "Cybersecurity Analyst",
        "technology": "cybersecurity",
        "category": "cryptography",
        "difficulty": "easy",
        "question_text": "What is the difference between Hashing, Encryption, and Encoding? Why is MD5 or SHA-256 unsuitable for storing user passwords compared to bcrypt or Argon2?",
        "expected_answer": "Encoding is a reversible representation of data (e.g. Base64) for transport without confidentiality. Encryption is a two-way mathematical process transforming plaintext to ciphertext using a key. Hashing is a one-way mathematical function producing a fixed-size digest. SHA-256 is designed to be extremely fast for checksums, enabling attackers to compute billions of guesses per second with GPUs. Password hashes (bcrypt, Argon2) are intentionally slow, memory-hard, and incorporate salts and work factors.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What is the purpose of a cryptographic salt and what attack does it neutralize?",
        "code_snippet": None
    },
    {
        "role": "Cybersecurity Analyst",
        "technology": "cybersecurity",
        "category": "incident_response",
        "difficulty": "medium",
        "question_text": "Explain the 6 phases of the Incident Response lifecycle according to the NIST SP 800-61 standard: Preparation, Detection & Analysis, Containment, Eradication, Recovery, and Post-Incident Activity.",
        "expected_answer": "1. Preparation: policies, tools, trained team, logging. 2. Detection & Analysis: alert triage, verifying scope, identifying attack vectors. 3. Containment: short-term isolation (disconnecting infected network VLANs) and long-term containment. 4. Eradication: removing malware, closing vulnerabilities, resetting compromised credentials. 5. Recovery: restoring systems from clean backups, monitoring for persistence. 6. Post-Incident: root cause post-mortem, updating playbooks and defenses.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "Why is preserving forensic memory dumps (RAM) critical before rebooting a compromised server?",
        "code_snippet": None
    },
    {
        "role": "Cybersecurity Analyst",
        "technology": "cybersecurity",
        "category": "authentication_iam",
        "difficulty": "medium",
        "question_text": "Explain how JSON Web Token (JWT) vulnerabilities can lead to authentication bypass (such as the 'None' algorithm attack and key confusion attacks). How do you secure JWT implementations?",
        "expected_answer": "The 'None' algorithm attack tricks the server into accepting an unsigned token if the verification library honors the header 'alg': 'none'. Key confusion occurs when an RS256 (asymmetric) server verifies a token using the public key as the HMAC secret key for HS256. Mitigation: enforce explicit algorithm whitelisting in code (reject alg: none, verify with fixed algorithm), use strong random secrets, and validate exp, nbf, and iss claims.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "Where should JWT tokens be stored on the client side to prevent XSS access?",
        "code_snippet": "// Insecure verification:\njwt.verify(token, secret); // if library allows alg from header\n// Secure verification:\njwt.verify(token, secret, { algorithms: ['RS256'] });"
    },
    {
        "role": "Cybersecurity Analyst",
        "technology": "cybersecurity",
        "category": "network_security",
        "difficulty": "medium",
        "question_text": "What is a SYN Flood attack, and how do SYN Cookies mitigate this Denial of Service (DoS) attack at the TCP stack level?",
        "expected_answer": "In a TCP 3-way handshake (SYN, SYN-ACK, ACK), an attacker sends a flood of SYN packets with spoofed IPs and never sends the final ACK, filling the operating system's SYN backlog queue and blocking legitimate connections. SYN Cookies mitigate this: instead of allocating memory in the backlog table upon receiving SYN, the server encodes state into the initial TCP sequence number. State is only allocated if a valid ACK returns.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How do you enable SYN cookies in Linux via sysctl?",
        "code_snippet": "# Enable in /etc/sysctl.conf:\nnet.ipv4.tcp_syncookies = 1"
    },
    {
        "role": "Cybersecurity Analyst",
        "technology": "cybersecurity",
        "category": "owasp_top_10",
        "difficulty": "medium",
        "question_text": "What is Cross-Site Request Forgery (CSRF)? How do SameSite cookie attributes (Strict, Lax, None) and Anti-CSRF Synchronizer Tokens defend against it?",
        "expected_answer": "CSRF tricks an authenticated user's browser into executing unwanted actions on a trusted web application by embedding unauthorized requests (e.g. form post) on a malicious website. Anti-CSRF tokens generate unique, cryptographically random, per-session tokens that the server validates with every state-changing request. SameSite=Lax/Strict instructs browsers not to attach session cookies on cross-origin requests, blocking CSRF.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "Why does SameSite=Lax not prevent GET-based CSRF if an endpoint performs state changes on GET requests?",
        "code_snippet": "Set-Cookie: session_id=xyz123; Secure; HttpOnly; SameSite=Strict"
    },
    {
        "role": "Cybersecurity Analyst",
        "technology": "cybersecurity",
        "category": "siem_logging",
        "difficulty": "medium",
        "question_text": "What is a SIEM (Security Information and Event Management) system? How do detection engineers write correlation rules to identify potential brute-force attacks across authentication logs?",
        "expected_answer": "A SIEM aggregates, normalizes, and correlates log events across servers, firewalls, and cloud infrastructure in real time. A correlation rule for brute-force: trigger an alert if >= 5 failed login events (event_id=4625 on Windows or 'Failed password' on Linux sshd) occur from the same source IP or targeting the same username within a 5-minute rolling window, especially if immediately followed by a successful login.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What is the difference between a False Positive and a False Negative in SIEM alerting?",
        "code_snippet": "# Splunk query:\nindex=windows EventCode=4625 \n| stats count by src_ip, user \n| where count >= 5"
    },
    {
        "role": "Cybersecurity Analyst",
        "technology": "cybersecurity",
        "category": "threat_frameworks",
        "difficulty": "medium",
        "question_text": "Explain the MITRE ATT&CK framework. How do Tactics, Techniques, and Procedures (TTPs) help SOC teams map adversary behaviors?",
        "expected_answer": "MITRE ATT&CK is a globally accessible curated knowledge base of adversary tactics and techniques based on real-world observations. Tactics represent the adversary's tactical objective (e.g. Initial Access, Persistence, Privilege Escalation, Lateral Movement, Exfiltration). Techniques describe how they achieve it (e.g. T1059 Command and Scripting Interpreter). TTPs allow defenders to focus on blocking behavioral patterns rather than fleeting file hashes.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What is the Pyramid of Pain and why is detecting TTPs the most painful for adversaries?",
        "code_snippet": None
    },
    {
        "role": "Cybersecurity Analyst",
        "technology": "cybersecurity",
        "category": "cryptography",
        "difficulty": "hard",
        "question_text": "Explain Asymmetric Public Key Cryptography and Diffie-Hellman Key Exchange. What is Perfect Forward Secrecy (PFS), and why is it vital for TLS session privacy?",
        "expected_answer": "Asymmetric encryption uses a public key for encryption and private key for decryption. Diffie-Hellman allows two parties to establish a shared secret over an insecure channel without transmitting the secret itself. Perfect Forward Secrecy (PFS) generates ephemeral, unique session keys for every TLS connection. Even if the server's master private key is stolen years later, previously recorded encrypted traffic cannot be decrypted.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "Which cipher suites provide PFS (e.g. ECDHE)?",
        "code_snippet": None
    },
    {
        "role": "Cybersecurity Analyst",
        "technology": "cybersecurity",
        "category": "network_security",
        "difficulty": "medium",
        "question_text": "What is the difference between an IDS (Intrusion Detection System), IPS (Intrusion Prevention System), and a WAF (Web Application Firewall)?",
        "expected_answer": "An IDS monitors network traffic passively via a SPAN/tap port and alerts on signatures or anomalies without blocking packets. An IPS sits in-line with network traffic and actively drops malicious packets (e.g. exploits, port scans). A WAF inspects Layer 7 HTTP/HTTPS application traffic, filtering application attacks like SQLi, XSS, and path traversal before requests reach the web server.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "Why can an IPS cause network outages if false positives are triggered?",
        "code_snippet": None
    },
    {
        "role": "Cybersecurity Analyst",
        "technology": "cybersecurity",
        "category": "malware_analysis",
        "difficulty": "medium",
        "question_text": "What is the difference between Static Malware Analysis and Dynamic Malware Analysis? What precautions must be taken before analyzing suspicious attachments?",
        "expected_answer": "Static analysis inspects malware code and properties without executing it: extracting hashes, examining strings, analyzing PE headers, and decompiling bytecode. Dynamic analysis executes the malware in an isolated, monitored sandbox to observe behavior (file writes, registry keys, process spawning, network C2 beacons). Precautions: run in isolated offline air-gapped sandboxes with deep snapshot capability.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How do modern malware samples detect that they are running inside a virtual machine or sandbox?",
        "code_snippet": None
    },
    {
        "role": "Cybersecurity Analyst",
        "technology": "cybersecurity",
        "category": "zero_trust",
        "difficulty": "easy",
        "question_text": "Explain the Zero Trust Architecture model ('Never Trust, Always Verify'). What are its core pillars (Identity, Device, Network, Application, Data)?",
        "expected_answer": "Zero Trust rejects the traditional castle-and-moat perimeter model where anyone inside the corporate network is implicitly trusted. Instead, every request—regardless of origin—must be authenticated, authorized, and encrypted before granting access. Pillars: 1. Identity (strong MFA). 2. Device (health and compliance check). 3. Network (micro-segmentation). 4. Application (least privilege). 5. Data (encryption at rest and in transit).",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How does microsegmentation prevent lateral movement by attackers?",
        "code_snippet": None
    },
    {
        "role": "Cybersecurity Analyst",
        "technology": "cybersecurity",
        "category": "email_security",
        "difficulty": "easy",
        "question_text": "How do SPF, DKIM, and DMARC DNS records work together to prevent email spoofing, phishing, and business email compromise (BEC)?",
        "expected_answer": "SPF (Sender Policy Framework) publishes a list of authorized IP addresses permitted to send emails from that domain. DKIM (DomainKeys Identified Mail) attaches a cryptographic digital signature to email headers verified against the domain's public key in DNS. DMARC (Domain-based Message Authentication) defines the enforcement policy (none, quarantine, reject) if SPF or DKIM fails and provides reporting on spoofing attempts.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What does 'p=reject' in a DMARC record instruct receiving mail servers to do?",
        "code_snippet": "v=DMARC1; p=reject; rua=mailto:dmarc-reports@example.com; pct=100"
    },
    {
        "role": "Cybersecurity Analyst",
        "technology": "cybersecurity",
        "category": "owasp_top_10",
        "difficulty": "medium",
        "question_text": "Explain Insecure Direct Object References (IDOR) / Broken Object Level Authorization (BOLA). How do you systematically test and prevent IDOR vulnerabilities?",
        "expected_answer": "IDOR/BOLA occurs when an application exposes a reference to an internal database object (e.g. /api/invoices/1042) without validating that the authenticated session owns or has permission to access that specific object, allowing an attacker to change the ID to 1043 and access other users' private data. Prevention: implement row-level authorization checks: WHERE id = :invoice_id AND user_id = :current_user_id.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "Why does using random UUIDs instead of sequential integers not completely solve IDOR without authorization checks?",
        "code_snippet": "# Secure endpoint pattern:\ndef get_invoice(invoice_id, current_user):\n    invoice = db.query(Invoice).filter_by(id=invoice_id, account_id=current_user.account_id).first()\n    if not invoice:\n        raise HTTPException(status_code=404, detail=\"Invoice not found\")\n    return invoice"
    },
    {
        "role": "Cybersecurity Analyst",
        "technology": "cybersecurity",
        "category": "endpoint_security",
        "difficulty": "medium",
        "question_text": "What is EDR (Endpoint Detection and Response) vs traditional Antivirus? How does behavioral detection catch living-off-the-land (LotL) attacks using PowerShell or WMI?",
        "expected_answer": "Traditional AV relies on signature hashes of known malicious files. EDR monitors continuous endpoint telemetry (process execution trees, memory injections, network connections, file modifications). LotL attacks use legitimate built-in administrative binaries (PowerShell, mshta, certutil, WMI) so they have no file signature. EDR behavioral analysis detects anomalies: e.g. Word.exe spawning powershell.exe with an encoded command flag.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What is Sysmon and how does it enhance Windows event logging for security monitoring?",
        "code_snippet": None
    },
    {
        "role": "Cybersecurity Analyst",
        "technology": "cybersecurity",
        "category": "dns_security",
        "difficulty": "medium",
        "question_text": "Explain DNS Tunneling and DNS Cache Poisoning. How does DNSSEC (Domain Name System Security Extensions) protect DNS integrity?",
        "expected_answer": "DNS Tunneling encodes non-DNS protocol data (malware C2 communications or exfiltrated data) inside DNS queries (e.g. <base64_data>.attacker.com) to bypass firewalls that allow port 53. DNS Cache Poisoning injects forged DNS responses into a resolver cache, redirecting users to malicious IPs. DNSSEC cryptographically signs DNS records with digital signatures (RRSIG), allowing resolvers to verify record authenticity.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "Does DNSSEC encrypt DNS queries for confidentiality or just provide integrity?",
        "code_snippet": None
    },
    {
        "role": "Cybersecurity Analyst",
        "technology": "cybersecurity",
        "category": "vulnerability_management",
        "difficulty": "easy",
        "question_text": "What is CVSS (Common Vulnerability Scoring System)? How do Base, Temporal, and Environmental metrics determine vulnerability remediation prioritization?",
        "expected_answer": "CVSS calculates a numerical score (0.0 to 10.0) reflecting vulnerability severity: Low (0.1-3.9), Medium (4.0-6.9), High (7.0-8.9), Critical (9.0-10.0). Base metrics reflect intrinsic qualities (attack vector, complexity, privileges, impact on C-I-A). Temporal metrics adjust based on current exploit availability and patch status. Environmental metrics adjust based on the asset's specific organizational criticality.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "Why does a CVSS 9.8 score on an internal air-gapped machine have different priority than on a public internet-facing server?",
        "code_snippet": None
    },
    {
        "role": "Cybersecurity Analyst",
        "technology": "cybersecurity",
        "category": "network_sniffing",
        "difficulty": "medium",
        "question_text": "Using Wireshark or tcpdump, what filters and packet anomalies would you look for when analyzing a packet capture (PCAP) for suspected ARP spoofing or Man-in-the-Middle (MitM) attacks?",
        "expected_answer": "In Wireshark: filter 'arp.duplicate-address-frame' or examine ARP responses where multiple distinct MAC addresses claim ownership of the same default gateway IP address (gratuitous ARP floods). For MitM: look for unexpected TLS certificate authority warnings, duplicate TCP ACKs, or HTTP plaintext transmissions on redirected non-standard ports.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How does Dynamic ARP Inspection (DAI) on managed switches prevent ARP spoofing?",
        "code_snippet": "# tcpdump capturing ARP packets on eth0:\ntcpdump -i eth0 -n arp"
    },
    {
        "role": "Cybersecurity Analyst",
        "technology": "cybersecurity",
        "category": "active_directory",
        "difficulty": "hard",
        "question_text": "Explain Kerberoasting in Active Directory environments. How do adversaries extract and offline-crack Service Principal Name (SPN) passwords?",
        "expected_answer": "In Active Directory, any authenticated domain user can request a Kerberos Ticket Granting Service (TGS) ticket for any service with a registered SPN. The TGS ticket is encrypted using the service account's NTLM password hash. The attacker dumps the ticket memory from their session and uses hashcat or John the Ripper to crack the plaintext password offline without triggering domain account lockouts.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How do Group Managed Service Accounts (gMSA) with 128-character rotating passwords mitigate Kerberoasting?",
        "code_snippet": None
    },
    {
        "role": "Cybersecurity Analyst",
        "technology": "cybersecurity",
        "category": "cryptography",
        "difficulty": "medium",
        "question_text": "What is a Replay Attack? How do Nonces, Timestamps, and HMAC signatures prevent replay attacks in network APIs?",
        "expected_answer": "A replay attack occurs when an attacker intercepts valid transmission data (such as a signed payment request or session authentication) and re-transmits it later to duplicate the action. Defenses: 1. Nonces (Number used ONCE): unique cryptographic random tokens recorded in cache; duplicate nonces are rejected. 2. Timestamps: requests older than 5 minutes are discarded. 3. HMAC signatures: bind the nonce and timestamp to request body.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "Why does the server need a short time-to-live cache (e.g. Redis) to track used nonces?",
        "code_snippet": None
    },
    {
        "role": "Cybersecurity Analyst",
        "technology": "cybersecurity",
        "category": "cloud_security",
        "difficulty": "medium",
        "question_text": "Explain the Shared Responsibility Model in cloud security (AWS/Azure/GCP) across IaaS, PaaS, and SaaS. What is always the customer's responsibility?",
        "expected_answer": "Cloud provider secures the 'security OF the cloud' (physical data centers, host hardware, hypervisors, foundational network). Customer secures 'security IN the cloud'. In IaaS: customer manages OS patches, firewall rules, runtime, and data. In PaaS: provider manages OS and runtime; customer manages app code and data. In SaaS: provider manages infrastructure and app; customer manages IAM and data. Customer is ALWAYS responsible for data classification, IAM access, and credentials.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What is Cloud Security Posture Management (CSPM)?",
        "code_snippet": None
    },
    {
        "role": "Cybersecurity Analyst",
        "technology": "cybersecurity",
        "category": "threat_intelligence",
        "difficulty": "easy",
        "question_text": "What are Indicators of Compromise (IoCs) versus Indicators of Attack (IoAs)? Provide examples of each.",
        "expected_answer": "Indicators of Compromise (IoCs) are forensic evidence of past intrusions (reactive/post-breach artifacts): e.g. specific MD5/SHA256 malware file hashes, known malicious C2 IP addresses, suspicious domain names, or specific registry keys created. Indicators of Attack (IoAs) focus on real-time intent and behavioral methods regardless of malware used: e.g. suspicious process code injection into lsass.exe, mass file encryption, or lateral movement via SMB.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How do STIX and TAXII standards facilitate threat intelligence sharing between organizations?",
        "code_snippet": None
    },
    {
        "role": "Cybersecurity Analyst",
        "technology": "cybersecurity",
        "category": "honeypots",
        "difficulty": "easy",
        "question_text": "What is a Honeypot in defensive security? Why do alerts triggered on a honeypot have a near-zero false positive rate?",
        "expected_answer": "A honeypot is a decoy system or network resource intentionally deployed with no legitimate business purpose, designed to lure, detect, and analyze unauthorized access attempts. Because the honeypot has no valid users, services, or legitimate business traffic, ANY connection attempt, probe, or scan directed at it is inherently unauthorized or malicious, yielding virtually zero false positive alerts.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What is the difference between a low-interaction honeypot and a high-interaction honeypot?",
        "code_snippet": None
    },
    {
        "role": "Cybersecurity Analyst",
        "technology": "cybersecurity",
        "category": "web_security_headers",
        "difficulty": "easy",
        "question_text": "Explain Content Security Policy (CSP), Strict-Transport-Security (HSTS), and X-Content-Type-Options HTTP headers. What attacks does each mitigate?",
        "expected_answer": "Content Security Policy (CSP) restricts the domains from which scripts, styles, images, and fonts can be loaded, mitigating XSS and data exfiltration. Strict-Transport-Security (HSTS) forces browsers to only communicate over HTTPS, mitigating SSL stripping and man-in-the-middle attacks. X-Content-Type-Options: nosniff prevents browsers from MIME-sniffing response types, mitigating drive-by download attacks disguised as images.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What does the CSP directive 'upgrade-insecure-requests' do?",
        "code_snippet": "Strict-Transport-Security: max-age=31536000; includeSubDomains; preload\nX-Content-Type-Options: nosniff\nContent-Security-Policy: default-src 'self'; script-src 'self' https://trusted.cdn.com"
    },
    {
        "role": "Cybersecurity Analyst",
        "technology": "cybersecurity",
        "category": "ransomware_defense",
        "difficulty": "medium",
        "question_text": "What is the 3-2-1 Backup Strategy? Why are Immutable and Air-Gapped backups critical for surviving modern human-operated ransomware attacks?",
        "expected_answer": "The 3-2-1 strategy requires: 3 copies of data on 2 different media types, with 1 copy stored offsite. Modern ransomware operators intentionally seek out, encrypt, and delete online network backups (VSS shadow copies, cloud backup accounts with stored credentials) before deploying encryptors. Immutable backups (WORM - Write Once, Read Many) and physical air-gapped backups cannot be modified or deleted by compromised domain admin credentials, guaranteeing recovery.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What is the 3-2-1-1-0 backup rule variant?",
        "code_snippet": None
    }
]
