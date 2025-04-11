# Logixx Monitoring

A comprehensive toolkit for monitoring and managing ASIC miners and GPU mining software with automated maintenance capabilities.

![Logixx Monitoring Dashboard](https://private-us-east-1.manuscdn.com/sessionFile/pxDBcFCDlMa3JnUuueKGxX/sandbox/sn3P9bRGGR3hP31ekr1nIQ-images_1744347833641_na1fn_L2hvbWUvdWJ1bnR1L2xvZ2l4eF9yZWFkbWUvaW1hZ2VzL2Rhc2hib2FyZA.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvcHhEQmNGQ0RsTWEzSm5VdXVlS0d4WC9zYW5kYm94L3NuM1A5YlJHR1IzaFAzMWVrcjFuSVEtaW1hZ2VzXzE3NDQzNDc4MzM2NDFfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwyeHZaMmw0ZUY5eVpXRmtiV1V2YVcxaFoyVnpMMlJoYzJoaWIyRnlaQS5wbmciLCJDb25kaXRpb24iOnsiRGF0ZUxlc3NUaGFuIjp7IkFXUzpFcG9jaFRpbWUiOjE3NjcyMjU2MDB9fX1dfQ__&Key-Pair-Id=K2HSFNDJXOU9YS&Signature=Kf-5ySbRhSZQ2yeGAM8jqrYZsz2HrgQTaP-RP0KJ1BH3W9Xt~c0P-8apQ7BZx7lROtSt~Zu1wh1z-NglRhaA2c71Le7fy4vZswGbEtKiWmqFL9rIw6LnhQkD0uPljpwT0v-TZicgkyvUbhrlWMN9amDEKAAnNdLTxM-HtgDo38CBg2-yULMqMW4vO0oaL9FVjHaanul8yxqZbfpUvndnds6vTml7GDWglq04NBlnyMfWBcihZSYCA~y1ogasRIKNX1zaRSsq3gMBqlDIDzWcKMvx-4rRxvGrBA0OQ9srw~LKrRWKrDLtzKHbZ09owcKuV3vKvAG9uZ36gZcTPatByg__)

## Overview

Logixx Monitoring provides a complete solution for mining operations of all sizes. The system continuously polls dozens of ASIC miners and various GPU mining software at least once per minute, updating a centralized database with critical metrics including miner types, IP/MAC addresses, hashrates, temperatures, uptimes, locations, error codes, and more.

Beyond passive monitoring, Logixx Monitoring integrates with ServerTech and Raritan smart PDUs to enable automated power cycling of machines experiencing issues such as low hashrate, high temperatures, or offline status. This automation significantly reduces downtime and maintenance overhead for mining operations.

The platform also includes onboarding scripts that can be integrated with SnipeIT inventory management, streamlining the process of adding new mining hardware to your operation.

## Key Features

### Comprehensive Monitoring
- Real-time tracking of dozens of ASIC miners and GPU mining software
- Minute-by-minute polling and database updates
- Detailed metrics collection (hashrate, temperature, uptime, etc.)
- Error code tracking and analysis
- Location-based organization

### Automated Maintenance
- Integration with ServerTech and Raritan smart PDUs
- Automatic power cycling based on configurable triggers:
  - Low hashrate detection
  - High temperature thresholds
  - Offline status monitoring
- Customizable alert thresholds and actions

### Management Tools
- Intuitive dashboard for monitoring overall mining operation health
- Detailed individual miner statistics and controls
- Remote reboot functionality through web interface
- Inventory integration with SnipeIT
- Invoicing system for service management

## Technology Stack

Logixx Monitoring is built on a robust and modern technology stack:

- **Backend**: Python-Flask
- **Database**: MySQL
- **Web Server**: Nginx
- **WSGI Server**: Gunicorn
- **Frontend Tables**: DataTables
- **Frontend Scripting**: JavaScript

This combination provides excellent performance, reliability, and scalability for mining operations of any size.

## Dashboard Overview

The main dashboard provides at-a-glance information about your entire mining operation, including:

- Total hashrate across all miners
- Online/offline status counts
- Average temperature readings
- Total cards being monitored
- Detailed table with individual miner statistics

![Dashboard View](https://private-us-east-1.manuscdn.com/sessionFile/pxDBcFCDlMa3JnUuueKGxX/sandbox/sn3P9bRGGR3hP31ekr1nIQ-images_1744347833641_na1fn_L2hvbWUvdWJ1bnR1L2xvZ2l4eF9yZWFkbWUvaW1hZ2VzL2Rhc2hib2FyZA.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvcHhEQmNGQ0RsTWEzSm5VdXVlS0d4WC9zYW5kYm94L3NuM1A5YlJHR1IzaFAzMWVrcjFuSVEtaW1hZ2VzXzE3NDQzNDc4MzM2NDFfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwyeHZaMmw0ZUY5eVpXRmtiV1V2YVcxaFoyVnpMMlJoYzJoaWIyRnlaQS5wbmciLCJDb25kaXRpb24iOnsiRGF0ZUxlc3NUaGFuIjp7IkFXUzpFcG9jaFRpbWUiOjE3NjcyMjU2MDB9fX1dfQ__&Key-Pair-Id=K2HSFNDJXOU9YS&Signature=Kf-5ySbRhSZQ2yeGAM8jqrYZsz2HrgQTaP-RP0KJ1BH3W9Xt~c0P-8apQ7BZx7lROtSt~Zu1wh1z-NglRhaA2c71Le7fy4vZswGbEtKiWmqFL9rIw6LnhQkD0uPljpwT0v-TZicgkyvUbhrlWMN9amDEKAAnNdLTxM-HtgDo38CBg2-yULMqMW4vO0oaL9FVjHaanul8yxqZbfpUvndnds6vTml7GDWglq04NBlnyMfWBcihZSYCA~y1ogasRIKNX1zaRSsq3gMBqlDIDzWcKMvx-4rRxvGrBA0OQ9srw~LKrRWKrDLtzKHbZ09owcKuV3vKvAG9uZ36gZcTPatByg__)

Each miner entry includes:
- IP and MAC addresses
- Miner type and operating system
- Site location and rack position
- Uptime statistics
- Current hashrate
- Temperature readings
- Status indicators
- Maintenance comments
- One-click restart functionality

## Invoicing System

Logixx Monitoring includes a complete invoicing system for service management, allowing you to:

- Generate professional invoices for monitoring services
- Track monitoring services by miner type (ASIC, GPU, etc.)
- Include hardware replacement parts in billing
- Process payments through multiple payment methods
- Maintain client account information
- Print-ready invoice formatting

![Invoice System](https://private-us-east-1.manuscdn.com/sessionFile/pxDBcFCDlMa3JnUuueKGxX/sandbox/sn3P9bRGGR3hP31ekr1nIQ-images_1744347833641_na1fn_L2hvbWUvdWJ1bnR1L2xvZ2l4eF9yZWFkbWUvaW1hZ2VzL2ludm9pY2U.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvcHhEQmNGQ0RsTWEzSm5VdXVlS0d4WC9zYW5kYm94L3NuM1A5YlJHR1IzaFAzMWVrcjFuSVEtaW1hZ2VzXzE3NDQzNDc4MzM2NDFfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwyeHZaMmw0ZUY5eVpXRmtiV1V2YVcxaFoyVnpMMmx1ZG05cFkyVS5wbmciLCJDb25kaXRpb24iOnsiRGF0ZUxlc3NUaGFuIjp7IkFXUzpFcG9jaFRpbWUiOjE3NjcyMjU2MDB9fX1dfQ__&Key-Pair-Id=K2HSFNDJXOU9YS&Signature=HUd51wEtKSDQaa1ULT~r3pwl7eKg2pWRDXGvcgh2QQpcn1hknx2ySBTlM9D-MFUEuzMAaYTEc9ahX2QqfYsbA4UW68GxSnTvFu043D-T~mIVJHMphWM5Xd~pp7IjAE32ZQwnvX4wouxYG2jKMn-lGXZZfYWfsvqc22eCsnOPhgRa-evmR4E8p1T-759AYld0ErvdH2BLaJwv9iDVPOSxkk~Nlaj6qSNbsrA0b8fZ0B25~0MzEyaq1-Rcwu7HxvZbaZQwhdhN6P4Fz~NyUnqbltvkrCpHcoHYuMbjS6TrDYIhHGEQMQokhhSb6WVBncJEKOiZgVl6KwWWrL7cYMmePA__)

## Authentication System

Logixx Monitoring features a secure authentication system to protect your mining operation data:

- User-friendly login interface
- Role-based access control
- Secure password management
- Session management
- Registration capabilities for new users

![Login Screen](https://private-us-east-1.manuscdn.com/sessionFile/pxDBcFCDlMa3JnUuueKGxX/sandbox/sn3P9bRGGR3hP31ekr1nIQ-images_1744347833641_na1fn_L2hvbWUvdWJ1bnR1L2xvZ2l4eF9yZWFkbWUvaW1hZ2VzL2xvZ2lu.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvcHhEQmNGQ0RsTWEzSm5VdXVlS0d4WC9zYW5kYm94L3NuM1A5YlJHR1IzaFAzMWVrcjFuSVEtaW1hZ2VzXzE3NDQzNDc4MzM2NDFfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwyeHZaMmw0ZUY5eVpXRmtiV1V2YVcxaFoyVnpMMnh2WjJsdS5wbmciLCJDb25kaXRpb24iOnsiRGF0ZUxlc3NUaGFuIjp7IkFXUzpFcG9jaFRpbWUiOjE3NjcyMjU2MDB9fX1dfQ__&Key-Pair-Id=K2HSFNDJXOU9YS&Signature=c3vG9fM7NEVrUQcQwc6aWi3H~YRRrzOPdFNK~BE2lZQdgU~HBDKPDMsz--V8bRvPcbjEZc5AXOAC4Gt6n69zVKHOSX18qhMVO71j9YlFVGKD81oFxvHGYT71FJX~wWHzmTEjYYmIUXc6tEupzEWnbImuw9uIduRQnDyRQfAtX73yxxsFpkpZPFWvTs~LTYiDhsKmgVNB~8t2AkWXHS3absu3SCM3RPGS9H17yBsPqaBEbdp8YQajOqNo2HZQLPQG8WhpZnbvapprd8R~7odwYNZpst00-Hg1Np3RB5tknnfTY2SnN5c1aP0ibnLXgv5iNCczJHIT06RxKrkt~sqwnQ__)

## Installation

*Detailed installation instructions would be included in the actual deployment package.*

## Usage

### Monitoring Dashboard

The monitoring dashboard provides real-time information about all miners in your operation. You can:

1. View overall statistics at the top of the page
2. Filter and search for specific miners
3. Sort by any column (IP, hashrate, temperature, etc.)
4. Identify problematic miners through status indicators
5. Remotely restart miners with a single click
6. Add maintenance comments for team communication

### Remote Reboot Functionality

The remote reboot feature allows administrators to:

1. Restart problematic miners directly from the web interface
2. Schedule automatic restarts based on performance thresholds
3. Configure power cycling parameters for different miner types
4. Log all restart events for maintenance records

### Invoicing System

The invoicing system enables:

1. Creating itemized bills for monitoring services
2. Tracking services by miner type and quantity
3. Including hardware replacement parts
4. Calculating taxes and shipping
5. Generating print-ready invoices
6. Maintaining client account information

## License

*License information would be included here.*

## Credits

Developed by Shawn Mullaney for Logixx LLC
