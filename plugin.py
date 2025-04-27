from flowlauncher import FlowLauncher
import subprocess
import sys

class PipInstaller(FlowLauncher):
    def run(self, param):
        try:
           
            parts = param.strip().split(" ", 2)
            if len(parts) >= 3 and parts[0] == "pip" and parts[1] == "install":
                package_name = parts[2]
                result = subprocess.run(
                    [sys.executable, "-m", "pip", "install", package_name],
                    capture_output=True,
                    text=True
                )

                if result.returncode == 0:
                    self.show_message(f"'{package_name}' installed successfully!")
                else:
                    self.show_message(f"Failed to install '{package_name}':\n{result.stderr}")
            else:
                self.show_message("Use: pip install <package_name>")
        except Exception as e:
            self.show_message(f"Error: {str(e)}")

    def show_message(self, message):
        self.show_toast("Pip Installer", message, duration=5)
