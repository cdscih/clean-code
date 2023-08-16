class Logger:
    def info(self, msg: str):
        print(f"INFO: {msg}")

    def error(self, msg: str):
        print(f"ERROR: {msg}")

    def debug(self, msg: str):
        print(f"DEBUG: {msg}")
