class UserRole:
    ADMIN = 'ADM'
    RECRUITER = 'REC'
    STUDENT = 'STD'

class ErrorMessage:
    # Common error messages
    NOT_FOUND = "not_found"
    NOT_AUTHORIZED = "not_authorized"
    INTERNAL_SERVER_ERROR = "internal_server_error"
    UNEXPECTED_ERROR = "unexpected_error"

    # Sign up error messages
    ALREADY_EXISTS = "already_exists"

    # Login error messages
    INCORRECT = "incorrect"
    INACTIVE_ACCOUNT = "inactive_account"

class SuccessMessage:
    # Common success messages
    SUCCESS = "success"
    CREATED = "created"
    UPDATED = "updated"
    DELETED = "deleted"

    # Login success messages
    LOGGED_IN = "logged_in"
    LOGGED_OUT = "logged_out"

    # User verification success messages
    VERIFIED = "verified"
    DEACTIVATED = "deactivated"

    FORGOT_PASSWORD = "forgot_password"

class InfoMessage:
    # Common info messages
    MAIL_SENT = "mail_sent"
    # PENDING = "pending"
    # UPDATED = "updated"
    # DELETED = "deleted"

    # # User verification info messages
    # VERIFIED = "verified