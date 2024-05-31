# Project Documentation: Sending Emails with Attachments in Django

## Introduction
This project demonstrates how to send emails with attachments using Django. The implementation includes handling different types of attachments such as images and PDFs, as well as adding recipients in CC and BCC fields.

## Project Structure

### ALLOWED_HOSTS and CSRF_TRUSTED_ORIGINS
In the `settings.py` file, we define the allowed hosts and the CSRF trusted origins to ensure security and proper configuration.

### send_email_function View
The `send_email_function` handles the request to send an email with attachments. It processes the POST request, extracts the necessary data, and sends the email using Django's `EmailMessage` class.

1. **Handling POST Request**: Extract data from the POST request including subject, recipient email, CC email, BCC email, message, image files, and a PDF file.
2. **Creating EmailMessage Object**: Create an `EmailMessage` object with the extracted data.
3. **Adding Attachments**: Attach image files and PDF file to the email if provided.
4. **Sending Email**: Use the `send` method to send the email.
5. **Rendering Template**: If the request method is GET, render the email form template.

### HTML Template: email_with_attachments.html
The HTML template provides a form to input the email details and upload attachments.

1. **Form Fields**: Fields for subject, recipient email, CC email, BCC email, message, image files, and PDF file.
2. **CSRF Token**: Ensure the form is secure by including a CSRF token.
3. **File Upload**: Allow multiple image file uploads and a single PDF file upload.

### Steps and Approach

1. **Define Allowed Hosts and CSRF Trusted Origins**:
   - Configure `ALLOWED_HOSTS` to include your deployment domain and localhost for testing.
   - Set `CSRF_TRUSTED_ORIGINS` to include your deployment URL for secure form submissions.

2. **Create View to Handle Email Sending**:
   - In your Django app, define a view function `send_email_function`.
   - Check if the request method is POST.
   - Extract necessary data from the request.
   - Create an `EmailMessage` object with the subject, message, and recipient.
   - Attach any image files and PDF file if provided.
   - Send the email.
   - Render the form template if the request method is GET.

3. **Design HTML Form for Email Input**:
   - Create an HTML template `email_with_attachments.html`.
   - Include fields for subject, recipient email, CC email, BCC email, message, image files, and PDF file.
   - Add CSRF token for security.
   - Allow multiple image file uploads and a single PDF file upload.

## Conclusion
This documentation outlines the approach for creating a Django project that sends emails with attachments. By following the described steps, you can effectively send emails with various types of attachments while ensuring secure and efficient handling of data and files.
