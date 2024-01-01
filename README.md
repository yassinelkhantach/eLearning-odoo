# E_Courses - Online Course Management for Odoo

E_Courses is an Odoo module designed to provide a comprehensive online platform for managing courses. It empowers administrators to efficiently handle courses and users, while also offering users the ability to explore, enroll, and rate courses.

## Features

- **Admin Dashboard:**
  - Manage Courses: Create, edit, and delete courses easily.
  - User Management: View and manage user accounts.

- **User Interface:**
  - Explore Courses: Browse through the list of available courses.
  - Enroll in Courses: Users can enroll in courses of their choice.
  - Rate Courses: Users can provide ratings and feedback for completed courses.

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/yassinelkhantach/eLearning-odoo.git

2. Copy the `e_courses` folder to your Odoo addons directory.

3. Restart your Odoo server.

4. Install the module from the Odoo Apps menu.

## Configuration

1. Log in to your Odoo instance with administrator credentials.

2. Navigate to the 'Apps' module.

3. Search for 'E_Courses' and install the module.

4. Once installed, the module will be available in the main menu.

## Usage

### Administrator:

1. **Manage Courses:**
   - Navigate to `Courses > Courses` to manage courses.
   - Click on 'Create' to add a new course.
   - Use the 'Edit' and 'Delete' buttons to modify existing courses.

2. **User Management:**
   - Visit `Users > Users` to manage user accounts.
   - Admins can view, edit, and deactivate user accounts.

### User:

1. **Explore Courses:**
   - Access the `Courses > Explore Courses` section to view available courses.

2. **Enroll in Courses:**
   - Click on a course to view details.
   - Enroll in a course using the provided button.

3. **Rate Courses:**
   - After completing a course, users can provide ratings and feedback.

4. **User URLs:**
   - Home Page: [http://localhost:port/](http://localhost:port/)
   - Explore Courses: [http://localhost:port/courses](http://localhost:port/courses)
   - Course Details and Actions: [http://localhost:port/course/{:id}/details](http://localhost:port/course/{:id}/details)

## Contribution

We welcome contributions! If you would like to contribute to this project, please follow our [contribution guidelines](CONTRIBUTING.md).

## Issues and Support

For bug reports and feature requests, please use the [GitHub issue tracker](https://github.com/yourusername/e_courses/issues).

For general support and discussions, visit our [community forum](https://example.com/forum).

```

Make sure to customize the placeholders, such as `{port}` and `{:id}`, with the actual port number and course ID values in your URLs.
