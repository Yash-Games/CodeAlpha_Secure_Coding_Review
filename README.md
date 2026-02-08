# Secure Coding Review

This project is part of the CodeAlpha Cyber Security Internship.

The objective of this task is to review a simple Python login program and identify
common security vulnerabilities.

## Identified Issues
- Hardcoded credentials
- Plain text password handling
- Lack of security controls

## Improvements
A more secure version of the login system was implemented using password hashing
to reduce the risk of credential exposure.

# Secure Coding Recommendations

Never hardcode credentials in source code

Use password hashing and salting

Store secrets in environment variables

Implement login attempt limits

Follow secure coding standards


This task helped in understanding the importance of secure coding practices
and basic application security.
