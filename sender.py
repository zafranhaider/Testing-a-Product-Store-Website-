import smtplib
import ssl
from tkinter import *

# Setup port number and server name
smtp_port = 587
smtp_server = "smtp.gmail.com"

def create_main_window():
    # Create the main window
    root = Tk()
    root.title("Email Sender")

    # Set the GUI resolution to 1366x768
    root.geometry("1366x768")

    # Add background image
    background_image = PhotoImage(file="img.png")
    background_label = Label(root, image=background_image)
    background_label.place(relwidth=1, relheight=1)

    # Function to send the email
    def send_email():
        try:
            # Get user input
            email_from = email_from_entry.get()
            email_to = email_to_entry.get()
            pswd = password_entry.get()
            subject = subject_entry.get()  # Added line for subject
            message = message_field.get("1.0", END)

            # Create context
            simple_email_context = ssl.create_default_context()

            # Connect to the server
            print("Connecting to server...")
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls(context=simple_email_context)
            server.login(email_from, pswd)
            print("Connected to server :-)")

            # Construct the email header with subject
            email_header = f"Subject: {subject}\n"
            
            # Send the email
            print()
            print(f"Sending email to - {email_to}")
            server.sendmail(email_from, email_to, email_header + message)
            print(f"Email successfully sent to - {email_to}")

            # Clear message field and subject entry
            message_field.delete("1.0", END)
            subject_entry.delete(0, END)

            # Show success message
            success_label.config(text="Email sent successfully!", fg="green")
        except Exception as e:
            print(e)
            # Show error message
            error_label.config(text=f"Error sending email: {e}", fg="red")

    # Label and entry field for email from
    email_from_label = Label(root, text="From:", bg='green', fg='white')
    email_from_label.pack()

    email_from_entry = Entry(root, bg='#D3D3D3')
    email_from_entry.pack()

    # Label and entry field for email to
    email_to_label = Label(root, text="To:", bg='green', fg='white')
    email_to_label.pack()

    email_to_entry = Entry(root, bg='#D3D3D3')
    email_to_entry.pack()

    # Label and entry field for subject
    subject_label = Label(root, text="Subject:", bg='green', fg='white')
    subject_label.pack()

    subject_entry = Entry(root, bg='#D3D3D3')
    subject_entry.pack()

    # Label and entry field for password
    password_label = Label(root, text="Password:", bg='green', fg='white')
    password_label.pack()

    password_entry = Entry(root, show="*", bg='#D3D3D3')
    password_entry.pack()

    # Text field for message
    message_label = Label(root, text="Message:", bg='green', fg='white')
    message_label.pack()

    message_field = Text(root, height=10, bg='white')
    message_field.pack()

    # Send button
    send_button = Button(root, text="Send Email", command=send_email, bg="#D3D3D3", relief=FLAT)
    send_button.pack(pady=10)

    # Label for success or error message
    success_label = Label(root, text="", bg='black', fg='white')
    success_label.pack()

    error_label = Label(root, text="", bg='black', fg='white')
    error_label.pack()

    # Back to Menu button
    back_to_menu_button = Button(root, text="Back to Menu", command=root.destroy, bg="#D3D3D3", relief=FLAT)
    back_to_menu_button.pack(pady=10)

    # Run the main loop
    root.mainloop()

# Create the main window
create_main_window()
