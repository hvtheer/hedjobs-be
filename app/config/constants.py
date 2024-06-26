class UserRole:
    ADMIN = "ADM"
    RECRUITER = "REC"
    STUDENT = "STD"


class ErrorMessage:
    # Common error messages
    NOT_FOUND = "not_found"
    NOT_AUTHORIZED = "not_authorized"
    INTERNAL_SERVER_ERROR = "internal_server_error"
    UNEXPECTED_ERROR = "unexpected_error"
    FORBIDDEN = "forbidden"

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
    LOGIN = "logged_in"
    LOGOUT = "logged_out"

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
