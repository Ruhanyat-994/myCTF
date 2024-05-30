# Chapter-1 Security Principles

# CIA TRIAD:

The CIA Triad is a fundamental concept in information security, consisting of three core principles: **Confidentiality**, **Integrity**, and **Availability**. Here's a short and simple explanation with real-world examples:

1. **Confidentiality**: Information will be available for only those who have the access .
    - **Example**: Your online banking information should only be accessible to you and your bank. If someone else gains access to your account details, confidentiality has been breached.
    - When a thing  of my accessibility is going to another hand which is unauthorised is called as a confidentiality breach.
    - personal details, email communication, Healthcare records, credit card info etc.

1. **Integrity**: Ensures that information is accurate and reliable and has not been altered by unauthorized people.
    - **Example**: When sending an email, you want to make sure that the message received by the recipient is exactly what you sent, without any unauthorized changes. If someone intercepts and modifies the email before it reaches the recipient, the integrity has been compromised.
    - if someone alter the personal details, email communication, Healthcare records, credit card info . This will be an integrity breach
    
2. **Availability**: Ensures that information and resources are available to authorized users when needed.
    - **Example**: When you need to access your work files stored in the cloud, the service should be operational so you can retrieve your documents. If the cloud service is down due to a cyber attack or technical issues, availability has been affected.

These principles help ensure that sensitive information is protected, accurate, and accessible when needed.

### Attacks for breaching CIA:

Various types of attacks can breach the principles of the CIA Triad (Confidentiality, Integrity, and Availability). Here are some examples for each principle:

1. **Confidentiality Breaches**:
    - **Phishing**: Attackers trick individuals into revealing sensitive information like passwords or credit card numbers.
    - **Man-in-the-Middle (MitM) Attacks**: Attackers intercept communication between two parties to eavesdrop or steal information.
    - **Malware/Spyware**: Malicious software designed to gather sensitive information from the victim's computer without their knowledge.
2. **Integrity Breaches**:
    - **Data Tampering**: Unauthorized modifications to data, such as altering financial records or changing the contents of a transmitted message.
    - **SQL Injection**: Attackers manipulate a database query to access, alter, or delete data stored in the database.
    - **Spoofing**: Attackers pretend to be another user or system to alter data or inject malicious data into a communication channel.
3. **Availability Breaches**:
    - **Distributed Denial of Service (DDoS) Attacks**: Attackers overwhelm a system, such as a website or network, with traffic to make it unavailable to legitimate users.
    - **Ransomware**: Malware that encrypts the victim's data and demands a ransom to restore access, effectively blocking availability until the ransom is paid.
    - **Hardware/Software Failures**: Exploiting vulnerabilities to cause crashes or failures, resulting in downtime and lack of access to services.
    - **Flood Attacks**
    - **Botnet Attacks**
    - **DNS Amplification**: Exploits the DNS protocol to generate large responses to small requests, overwhelming the target with traffic.

These attacks illustrate the various ways that malicious actors can compromise the security and functionality of systems by targeting confidentiality, integrity, and availability.

# AUTHENTICATION:

### **Overview of Authentication**

**Authentication** is a security principle that ensures that an individual or system requesting access is truly who or what it claims to be. It is the first line of defence in protecting systems, data, and networks from unauthorized access.

### **Example of Authentication**

**Example**: When you log into your email account, you enter a username and password. The system checks these credentials against its database to verify your identity. If the credentials match, you are granted access to your email. This process confirms that you are the legitimate user of the account.

### **Methods of Authentication**

1. **Something You Know**: Passwords, PINs, security questions.
2. **Something You Have**: Smart cards, security tokens, mobile phones (for receiving SMS codes).
3. **Something You Are**: Biometrics like fingerprints, facial recognition, iris scans.

These methods can be combined for stronger security (e.g., two-factor authentication).

# Authenticity and Nonrepudiation:

### Authenticity:

Verifying that The  data is coming from verified source and the root of the data hasn’t tempered. 

**Method**: Digital signatures .

**Example**: When you receive an email with a digital signature, you can verify the authenticity of the sender. The digital signature confirms that the email indeed comes from the claimed sender and not from an impostor.

### Nonrepudiation:

Nonrepudiation is a process where a sender can’t deny the thing that he sent. Or parties who are involved with the process can’t deny.

**Method :** Digital Signature. 

**Example**: In an online banking transaction, a digital certificate and encryption ensure that the sender of a transfer request cannot later claim they did not initiate the transaction. The bank can prove the request came from the authorized account holder, ensuring nonrepudiation.

### **Key Differences:**

- **Authenticity** focuses on verifying the source of information.
- **Nonrepudiation** focuses on ensuring that once a transaction is completed, the parties involved cannot deny their participation.

# 

# **Information Assurance**

**Definition**: Information Assurance (IA) is the practice of ensuring the confidentiality, integrity, authenticity, availability, and nonrepudiation of information and data within an organization. It involves implementing policies, procedures, and technologies to protect sensitive information from unauthorized access, alteration, or destruction.

Frameworks and Standards:

```
ISO/IEC 27002: Provides a comprehensive framework for establishing, implementing, maintaining, and continuously improving an information security management system (ISMS).

NIST Cybersecurity Framework: Developed by the National Institute of Standards and Technology (NIST), it offers guidance on managing and reducing cybersecurity risks.

PCI DSS (Payment Card Industry Data Security Standard): A set of security standards designed to ensure that all companies that accept, process, store, or transmit credit card information maintain a secure environment.

ISACA Risk IT
```

# PRIVACY:

It is a right to protect individuals information.

# Risk Management :

**Definition**: Risk management in security programs involves the systematic process of identifying, assessing, and controlling potential threats and vulnerabilities to information assets. It aims to minimize the impact of security incidents and ensure the confidentiality, integrity, and availability of data.

### Threat Actors/Agents:

Person who exploit vulnerabilities are called as a threat agents 

`Cyber Criminals`

`Nation-states`

`Terrorist groups`

`Insiders`

`Criminal Groups`