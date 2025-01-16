import time
import threading
from colorama import Fore, Style, init

init(autoreset=True)


class Spinner:
    """
    Class for managing spinner animations during long-running processes.
    """

    def __init__(self, message: str = "Processing", interval: float = 0.1) -> None:
        """
        Initializes the spinner with a message and animation interval.

        Args:
            message (str): The message to display alongside the spinner.
            interval (float): The update interval for the spinner animation.
        """
        self.message = message
        self.interval = interval
        self._stop_event = threading.Event()
        self._spinner_thread = threading.Thread(target=self._spin)
        self.status = ""
        self.spinner_sequence = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]

    def _spin(self) -> None:
        """
        Handles the spinner animation in a separate thread.
        """
        idx = 0
        while not self._stop_event.is_set():
            print(
                f"\r{Fore.CYAN}{self.message} {self.spinner_sequence[idx % len(self.spinner_sequence)]} "
                f"{Fore.YELLOW}{self.status}{Style.RESET_ALL}",
                end="",
            )
            idx += 1
            time.sleep(self.interval) 

    def update_status(self, status: str) -> None:
        """
        Updates the status message displayed alongside the spinner.

        Args:
            status (str): The status message to display.
        """
        self.status = status

    def start(self) -> None:
        """
        Starts the spinner animation.
        """
        self._stop_event.clear()
        self._spinner_thread.start()

    def stop(self) -> None:
        """
        Stops the spinner animation.
        """
        self._stop_event.set()
        self._spinner_thread.join()
        print()