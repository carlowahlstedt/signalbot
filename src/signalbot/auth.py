from __future__ import annotations

import base64

from pydantic import BaseModel


class Authentication(BaseModel):
    """
    Base class for authentication methods.
    """

    @property
    def header(self) -> str:
        """The authorization header value."""
        raise NotImplementedError

    def write_header(self, headers: dict[str, str]) -> None:
        """Adds the authorization header to the given headers.

        Args:
            headers: The dictionary to which the authorization header will be added.
        """
        headers["Authorization"] = self.header


class BasicAuthentication(Authentication):
    """
    Username and password based authentication.

    Attributes:
        username: The username for the authentication.
        password: The password used for authentication.
    """

    username: str
    password: str

    @property
    def header(self) -> str:
        credentials = f"{self.username}:{self.password}".encode()
        credential_string = base64.b64encode(credentials).decode("utf-8")
        return f"Basic {credential_string}"


class BearerAuthentication(Authentication):
    """
    Token based authentication.

    Attributes:
        token: The token used for authentication.
    """

    token: str

    @property
    def header(self) -> str:
        return f"Bearer {self.token}"
