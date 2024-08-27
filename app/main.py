def format_linter_error(error: dict) -> dict:
    return {
        "line": error["line"],
        "column": error["column"],
        "message": error["message"],
        "name": error["name"],
        "source": "flake8",
    }
    pass


def format_single_linter_file(file_path: str, errors: list) -> dict:
    formated_errors = [format_linter_error(error) for error in errors]
    status = "failed" if formated_errors else "passed"
    return{
        "errors": formated_errors,
        "path": file_path,
        "status": status
    }
    pass


def format_linter_report(linter_report: dict) -> list:
    return [
        format_single_linter_file(file_path, errors)
        for file_path, errors in linter_report.items()
    ]
    pass
