## Meta Back-End Developer Capstone Project: LittleLemon Restaurant Booking System

This project implements a backend API for a restaurant booking system. It includes functionality for managing restaurants, menus, reservations, and user authentication.

**API Endpoints:**

- **`/auth/users`**: DRF View that lists the users of the application. You can create new users from here
- **`/auth/token/login/`**: DRF View that allows you to input the username and password of created user. This will return the token for the user
- **`/auth/token/logout/`**: Logout the user and invalidate the token
- **`/restaurant/`**: View the static page of littlelemon restaurant which displays the welcome text and static image of the logo
- **`/restaurant/menu/`**: DRF view that manages restaurant menus (functionalities include creating, retrieving, updating, or deleting menu items).
- **`/restaurant/menu/<int>`**: DRF Single Menu Item view that manages single menu item (functionalities include retrieving, updating, or deleting single menu item).
- **`/restaurant/booking/tables/`**: DRF View which manages restaurant tables for bookings (functionalities include retriving booked tables list, reserving tables, etc.).
- **`/restaurant/booking/tables/<int>`**: DRF View which manages single restaurant table booking (functionalities include retriving booked table details, updating values, deleting the record etc.).

**Testing with Insomnia:**

As recommended in the course, use Insomnia [https://insomnia.rest/](https://insomnia.rest/) to test the API endpoints. Here's how to get started:

1. **Install Insomnia:** Download and install Insomnia from [https://insomnia.rest/](https://insomnia.rest/).
2. **Clone the Project:** Clone this project repository to your local machine.
3. **Set Up Dependencies:**
   - Ensure you have pipenv installed (`pip install pipenv`).
   - Navigate to the project directory and run `pipenv install` to install the project dependencies.
4. **Configure Database Credentials:**
   - Update the `settings.py` file inside `littlelemon` with your local MySQL username, password, and database name.
